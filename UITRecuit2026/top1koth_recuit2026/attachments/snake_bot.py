from collections import deque

W = 25
H = 25
DIRS = ((0, -1), (1, 0), (0, 1), (-1, 0))
TURNS = (0, -1, 1)

# The runner keeps this module alive for the full match. Reconstruct both
# bodies one turn at a time from the previous actions.
_me = None
_enemy = None
_me_dir = 0
_enemy_dir = 0
_last_action = 0
_old_apples = set()


def _point(p):
    return (int(p[0]), int(p[1]))


def _step(p, d):
    dx, dy = DIRS[d]
    return (p[0] + dx, p[1] + dy)


def _inside(p):
    return 0 <= p[0] < W and 0 <= p[1] < H


def _advance(body, direction, action, apples):
    nd = (direction + TURNS[action]) % 4
    head = _step(body[0], nd)
    grew = head in apples
    result = [head] + body[:]
    if not grew:
        result.pop()
    return result, nd, grew


def _plan_to_apple(head, direction, body, enemy, apples, enemy_d):
    """Time-expanded BFS to the nearest currently visible apple."""
    if not apples:
        return None
    length = len(body)
    # A segment at index i leaves its square after length-i moves.
    release = {p: length - i for i, p in enumerate(body)}
    enemy_cells = set(enemy)
    enemy_next = {_step(enemy[0], (enemy_d + turn) % 4) for turn in TURNS}
    enemy_next = {p for p in enemy_next if _inside(p)}

    # Each node carries the recent planned head path. This prevents the search
    # from routing through its own newly-created body.
    queue = deque([(head, direction, 0, -1, (head,))])
    seen = {(head, direction, 0)}
    max_depth = 22
    while queue:
        pos, d, depth, first, path = queue.popleft()
        if depth >= max_depth:
            continue
        nt = depth + 1
        for turn in TURNS:
            nd = (d + turn) % 4
            nxt = _step(pos, nd)
            if not _inside(nxt):
                continue
            if nxt in enemy_cells or (nt == 1 and nxt in enemy_next):
                continue
            if nxt in release and nt < release[nxt]:
                continue
            # A planned head square remains occupied until it has left the tail.
            tail_start = max(0, len(path) - length)
            if nxt in path[tail_start:]:
                continue
            action = 1 if turn == -1 else (2 if turn == 1 else 0)
            if first < 0:
                first = action
            if nxt in apples:
                return first
            key = (nxt, nd, nt)
            if key in seen:
                continue
            seen.add(key)
            queue.append((nxt, nd, nt, first, path + (nxt,)))
    return None


def _safe_fallback(head, direction, body, enemy, enemy_d, apples):
    enemy_cells = set(enemy)
    enemy_next = {_step(enemy[0], (enemy_d + turn) % 4) for turn in TURNS}
    enemy_next = {p for p in enemy_next if _inside(p)}
    best_action = 0
    best_score = -10**9
    for action, turn in ((0, 0), (1, -1), (2, 1)):
        nd = (direction + turn) % 4
        nxt = _step(head, nd)
        if not _inside(nxt) or nxt in enemy_cells or nxt in enemy_next:
            continue
        ate = nxt in apples
        occupied = set(body if ate else body[:-1])
        occupied.add(nxt)
        occupied.update(enemy_cells)
        q = deque([nxt])
        reached = {nxt}
        while q:
            p = q.popleft()
            for dd in range(4):
                z = _step(p, dd)
                if _inside(z) and z not in occupied and z not in reached:
                    reached.add(z)
                    q.append(z)
        nearest = min((abs(nxt[0] - a[0]) + abs(nxt[1] - a[1]) for a in apples), default=50)
        score = len(reached) * 100 - nearest * 10
        if score > best_score:
            best_score = score
            best_action = action
    return best_action


def decide(state):
    global _me, _enemy, _me_dir, _enemy_dir, _last_action, _old_apples

    apples = {_point(p) for p in state.apples}
    if state.last_opponent_action is None or _me is None:
        _me = [_point(p) for p in state.initial_self_body]
        _enemy = [_point(p) for p in state.initial_opponent_body]
        delta = (_me[0][0] - _me[1][0], _me[0][1] - _me[1][1])
        _me_dir = DIRS.index(delta)
        delta = (_enemy[0][0] - _enemy[1][0], _enemy[0][1] - _enemy[1][1])
        _enemy_dir = DIRS.index(delta)
    else:
        _me, _me_dir, _ = _advance(_me, _me_dir, _last_action, _old_apples)
        opp_action = int(state.last_opponent_action)
        if opp_action not in (0, 1, 2):
            opp_action = 0
        _enemy, _enemy_dir, _ = _advance(_enemy, _enemy_dir, opp_action, _old_apples)

    head = _me[0]
    action = _plan_to_apple(head, _me_dir, _me, _enemy, apples, _enemy_dir)
    if action is None:
        action = _safe_fallback(head, _me_dir, _me, _enemy, _enemy_dir, apples)
    _last_action = action
    _old_apples = apples
    return action


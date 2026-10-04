# top1koth_recuit2026 — UITRecuit2026

- **Challenge:** Our Long Snake
- **Event:** UITRecuit2026
- **Type:** King of the Hill / programming bot

I started with a simple idea: reach food when there is a safe route, and leave myself room to move when there is not. The Python bot attached below is the version exported alongside these notes in the original solve session.

## Attachments

- [Python bot](attachments/snake_bot.py)
- [Original writeup notes](evidence/original-writeup.md)

## Overview

Our Long Snake is a two-player snake game on a 25x25 board. Each turn, the bot chooses one of three actions: go straight (`0`), turn left (`1`), or turn right (`2`). Eating an apple grows the snake. A snake dies when it hits a wall, its own body, or the opponent's body.

A match can run for up to 1,000 turns. The ranking is decided by scored apples, final length, total apples, and kills, in that order. Because this is a KOTH-style challenge, the goal is not to recover a single flag but to write a bot that consistently survives and scores well.

## Tracking the Game State

The API gives the starting bodies for both snakes, the apples on the board, and the opponent's previous move. It does not send a complete updated board every turn, so the bot must keep its own model of the board.

At the beginning of a match, the bot derives each snake's direction from its head and neck. On later turns, it applies its own previous move and the opponent's reported move, inserts the new head at the front of each body, and removes the tail unless the snake just ate an apple. This local simulation gives the bot enough information to avoid walls, itself, and the opponent.

## Pathfinding to Apples

The main strategy is breadth-first search. A search state contains the head position, current direction, and step count. From each state, the bot tries the three legal actions: straight, left, and right.

The search rejects routes that leave the board, enter the opponent's body, or collide with one of our own body segments before that segment moves away. It also avoids squares that the opponent could reach on its next move, which reduces immediate head-on deaths.

To stay within the per-turn time limit, the bot searches no more than 22 moves ahead. Once it finds a safe apple route, it returns the first action on that route and replans on the next turn.

## Fallback Survival Mode

When no safe apple route is available within the search limit, the bot switches to survival. It evaluates each legal next action with flood fill and estimates how much open space would remain reachable after that move.

The selected move is the one that leaves the most space. If two moves are close, distance to the nearest apple is used as a tie-breaker. For longer planning, the opponent's body is treated as a fixed obstacle. That is conservative, but it avoids relying on the opponent moving out of the way.

## Verification Notes

The attached file exposes `decide(state)` and uses only the Python standard library. The runner must keep the module alive between turns because the reconstructed bodies are stored in module globals.

To check the syntax locally, run this from the challenge folder:

```sh
python -m py_compile attachments/snake_bot.py
```

Upload `attachments/snake_bot.py` through the arena's bot submission form. The arena supplies the state object, so running the file directly does not start a game. Try the built-in opponents, `winky` and `iamabighotdog`, and inspect the diagnostics for runtime errors and timeouts.

This is the source exported with the original notes, rather than a later experimental bot. Those notes record a successful syntax check but no completed practice match for this particular export. I would not use that check alone as evidence of tournament performance.

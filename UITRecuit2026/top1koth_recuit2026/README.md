# top1koth_recuit2026 — UITRecuit2026

- **Challenge:** Our Long Snake
- **Event:** UITRecuit2026
- **Type:** King of the Hill / programming bot

This writeup is based on the original notes in `D:/ctf/top1koth_recuit2026/writeup.md`. The source folder currently contains only the writeup file; the referenced `snake_bot.py` implementation was not present in the provided folder, so it is not attached here.

## Attachments

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

The original notes say the Python implementation passed syntax compilation, but a practice match was not run in that session because the browser file picker did not open. Before using the bot in a live tournament, run it against both built-in opponents, `winky` and `iamabighotdog`, and check for runtime errors or timeouts.

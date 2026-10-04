# Our Long Snake — Write-up

## Overview

Our Long Snake is a two-player snake game on a 25×25 board. Each turn, a bot chooses to go straight (`0`), turn left (`1`), or turn right (`2`). Eating an apple makes the snake grow. A snake dies if it hits a wall or either snake's body. Matches can last up to 1,000 turns, and the result is decided by scored apples, final length, total apples, and kills, in that order.

## Keeping track of the board

The bot API gives us both snakes' starting bodies, the apples currently on the board, and the opponent's previous move. It does not send a fresh copy of both bodies on every turn. That means the bot has to remember where the snakes were and update their positions as the match progresses.

At the start of a match, the bot reads each snake's head and neck to work out its direction. On later turns, it applies its own previous move and the opponent's reported move. The new head position is added to the front of each body. If that head moved onto an apple, the tail stays in place and the snake grows; otherwise, the tail is removed. This gives the bot an estimate of the current bodies, which it needs to plan moves without running into itself or the other snake.

## Finding a route to food

The bot uses breadth-first search to look for the nearest apple it can reach safely. Its search state includes the head position, direction, and number of steps taken. At each step it considers only the three legal actions: straight, left, and right.

A route is discarded if it leaves the board, enters the opponent's body, or runs into one of our own segments before that segment has moved away. The bot also avoids squares the opponent could reach on its very next move, which helps prevent immediate head-on collisions. To keep the search small enough for the per-turn time limit, it looks no more than 22 moves ahead. Once it finds an apple, it returns the first move along that route and searches again on the next turn.

## Staying alive when food is out of reach

Sometimes there is no apple on a safe route within the search limit. In that case, the bot considers each legal next move and uses flood fill to estimate how much open space remains reachable. It chooses the move that leaves the most room, using distance to the nearest apple as a tie-breaker.

For longer routes, the bot treats the opponent's current body as a fixed obstacle. This is conservative: the opponent may move away, but the bot does not rely on that happening. It only predicts the opponent's possible head positions for the next move.

## Files and verification

The implementation is in `snake_bot.py`. It follows the Python `decide(state)` interface and returns `0`, `1`, or `2` using only the standard library.

The file passed Python syntax compilation. I could not run a Practice match in this session because the integrated browser did not open its file picker, so I have no match results to report. Before using the bot in the tournament, run it against both built-in opponents, `winky` and `iamabighotdog`, and check the diagnostics for runtime errors or timeouts.

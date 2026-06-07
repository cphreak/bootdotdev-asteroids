# Asteroids

A classic Asteroids arcade game built with Python and [Pygame](https://www.pygame.org/). Pilot a triangle-shaped ship through space, destroy incoming asteroids, and avoid collisions.

## Features

- Player ship with rotation, thrust, and shooting
- Asteroids that spawn from screen edges and drift across the playfield
- Collision detection between ship, shots, and asteroids
- Asteroids split into smaller pieces when hit
- Game state logging for debugging and analysis

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Installation

### With uv (recommended)

```bash
uv sync
```

### With pip

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the game

```bash
uv run python main.py
```

Or, if using a virtual environment:

```bash
python main.py
```

Close the game window or press the window close button to quit.

## Controls

| Key | Action |
|-----|--------|
| `W` | Thrust forward |
| `S` | Thrust backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Shoot |

## How to play

- Destroy asteroids by shooting them. Each hit splits a large asteroid into two smaller ones.
- Asteroids that are already at minimum size are destroyed outright.
- If your ship collides with an asteroid, the game ends.
- New asteroids spawn periodically from random edges of the screen.

## Project structure

```
.
├── main.py           # Game loop, sprite groups, and collision handling
├── constants.py      # Screen size, speeds, spawn rates, and other tuning values
├── circleshape.py    # Base sprite class with position, velocity, and collision
├── player.py         # Player ship (triangle) with movement and shooting
├── shot.py           # Projectiles fired by the player
├── asteroid.py       # Asteroid sprites with splitting behavior
├── asteroidfield.py  # Spawns asteroids from screen edges
└── logger.py         # Writes periodic game state snapshots to JSONL
```

## Configuration

Game parameters live in `constants.py`:

- Screen resolution: 1280×720
- Asteroid spawn rate, sizes, and split speed
- Player turn speed, movement speed, and shoot cooldown

## Logging

During each run, `logger.py` writes game state snapshots to `game_state.jsonl` (once per second for the first 16 seconds). Each entry includes sprite counts, positions, velocities, and other metadata useful for debugging.

This file is gitignored and recreated on each run.

## License

Part of the [Boot.dev](https://www.boot.dev/) Python curriculum.

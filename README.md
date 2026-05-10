# Cellular Automata

Conway's Game of Life implemented using:

- CellPyLib
- Pure Python + Pygame

## Demos

### CellPyLib Version

![CellPyLib Demo](assets/cellpylib_demo.gif)

### Pygame From-Scratch Version

![Pygame Demo](assets/pygame_demo.gif)

## What is Cellular Automata?

Cellular automata are grid-based computational systems where
simple local rules create complex emergent behavior.

This project implements **Conway's Game of Life**,
one of the most famous cellular automata systems ever created.

The simulation demonstrates how:
- simple rules,
- local interactions,
- and discrete states

can generate highly complex global patterns.

## Conway's Game of Life Rules

Each cell exists in one of two states:

- Alive
- Dead

At every generation:

- Alive cell with fewer than 2 neighbors dies
- Alive cell with 2 or 3 neighbors survives
- Alive cell with more than 3 neighbors dies
- Dead cell with exactly 3 neighbors becomes alive

## Implementations

### 1. CellPyLib Implementation

High-level implementation using the CellPyLib cellular automata library.

Features:
- Random initialization
- Text injection
- Animated evolution

![CellPyLib Screenshot](assets/cellpylib_demo.png)

### 2. Pure Python + Pygame Implementation

Low-level implementation built completely from scratch using Pygame.

![Pygame Screenshot](assets/pygame_demo.png)

## Project Structure

```text
cellular-automata/
│
├── README.md
├── requirements.txt
│
├── cellpylib_version/
│   └── mothers_day.py
│
├── pygame_from_scratch/
│   └── conways_game_of_life.py
│
├── assets/
│   ├── cellpylib_demo.gif
│   ├── pygame_demo.gif
│   ├── cellpylib_demo.png
│   └── pygame_demo.png
│
└── docs/
```

## Future Improvements

- Custom rule systems
- GPU acceleration
- Infinite grid support
- Zoom and pan camera
- Pattern loader
- Music-reactive automata
- Performance optimizations
- Pattern saving/loading
- Interactive drawing tools

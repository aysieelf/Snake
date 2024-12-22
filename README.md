# 🐍 Snake

A classic Snake game built with PyGame - my second game!

## 📑 Table of Contents
- [Installation](#-installation)
  - [Prerequisites](#prerequisites)
  - [Step-by-Step Installation](#step-by-step-installation)
  - [Running the Game](#running-the-game)
  - [Controls](#controls)
- [Current Progress](#-current-progress)
- [Project Goals](#-project-goals)
- [Features](#-features)
- [Documentation](#-documentation)
- [What I Learned](#-what-i-learned)
- [First Time Achievements](#-first-time-achievements)
- [Screenshots](#-screenshots)
- [Demo](#-demo)
- [Technical Details](#-technical-details)

## 🚀 Installation

### Prerequisites
- Python 3.12 or higher
- pip (Python package installer)

### Step-by-Step Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/aysieelf/Snake.git
   cd Snake
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   # On Windows
   python -m venv .venv
   .venv\Scripts\activate

   # On macOS/Linux
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Game
```bash
python main.py
```

### Controls
- WASD/Arrow keys - Move snake
- R - Restart game
- Q - Quit to main menu / Exit game
- Space - Start game / Pause/Resume game

## ⏳ Current Progress
[▓▓▓▓▓░░░░░] 50%

- [x] Project setup
- [x] Snake implementation
- [x] Food & Growth mechanics
- [x] Collision & Game Over
- [x] Pause & Restart
- [ ] UI & Polish

## 🎯 Project Goals
- Create a classic Snake game with smooth controls
- Master PyGame collision detection
- Practice game state management
- Learn grid-based movement systems

## 🚀 Features
- Smooth snake movement with arrow key controls
- Growing snake mechanics
- Score system based on food collection
- Collision detection with walls and self
- Game over & restart functionality
- Pause/Resume game option
- Food spawning system

## 📚 Documentation
- [User Guide](docs/user-guide.md) - Detailed instructions on how to play the game

## 📚 What I Learned
- pygame.time.Clock for frame rate control - `pygame.time.Clock.tick()`
  - this is used to control the speed of the game
- Grid-based movement system
- Collision detection with walls and self
- Game state management
- Pause/Resume game functionality
- Food spawning system
- Clean code organization in game development

## 💡 First Time Achievements
- First time implementing a grid-based movement system
- First time using PyGame's `pygame.time.Clock` for frame rate control
- First time implementing a pause/resume game functionality
- First time implementing a food spawning system
- First time implementing a growing snake mechanic

## 📸 Screenshots
...

## 🎥 Demo
...

## 🛠️ Technical Details
- Python version: 3.12
- PyGame version: 2.6.1

---
Part of my [Game Development Journey](https://github.com/aysieelf/Game-Dev-Journey) 🎮

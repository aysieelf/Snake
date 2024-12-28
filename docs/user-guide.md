# 🐍 Snake User Guide

## Game Overview
Snake is a classic arcade game where the player controls 
a growing snake to eat food and score points. 

The snake moves in a grid-based system and grows longer with each food item consumed. 
The game ends if the snake collides with the walls or itself. 
Bonus food items provide extra points and add a challenge to the gameplay.

## Getting Started
1. Launch the game by running `python main.py`
2. Click the "start game" button on the welcome screen to begin

## Game Interface
- **Welcome Screen**: The initial screen with the game title and start button
- **Instructions**: Information on how to play the game and control the snake
- **Snake**: The player-controlled snake that grows in length
- **Food**: The target for the snake to eat and increase its score (pink squares): 1 pt
- **Bonus Food**: Special food items that provide extra points (green squares): 3 pts
- **Score**: The current score of the player
- **Particles**: Visual effects that appear when the snake eats food
- **Game Over**: Message displayed when the snake collides with a wall or itself

## How to Play
1. Use the arrow keys or WASD to move the snake
2. Eat food to grow the snake and increase your score
3. Avoid colliding with the walls or the snake's body
4. Collect bonus food for extra points (3 pts)
5. Pause the game by pressing the space bar
6. Restart the game by pressing the "R" key
7. Quit the game by pressing the "Q" key

## Controls
- **WASD/Arrow keys**: Move the snake
- **R**: Restart the game
- **Q**: Quit to main menu / Exit game
- **Space**: Start game / Pause/Resume game
- **Mouse Click**: Interact with buttons

## Game Features
- Welcome screen with start button
- Smooth snake movement with arrow key controls
- Growing snake mechanics
- Food spawning system
- Particle effects when collecting food
- Real-time score tracking
- Collision detection with walls and self
- Game over & restart functionality
- Pause/Resume game option

## Tips for Playing
- Try to anticipate the snake's movements to avoid collisions
- Note that bonus food items appear every 20 seconds and disappear after 5 seconds
- Use the pause feature to take a break or strategize your next move
- The game speeds up as the snake grows longer, so be prepared for faster gameplay

## Troubleshooting
**Game does not start:**
- Ensure Python 3.12+ is installed
- Check if PyGame is properly installed
- Verify all game files are present

**Can't control the snake:**
- Make sure the game window is active
- Check if the arrow keys or WASD are functioning correctly
- Restart the game if the issue persists

**Game seems frozen:**
- Press the space bar to pause/resume the game
- Check if the game window is in focus
- Restart the game if necessary

**Game crashes or displays errors:**
- Check the terminal/console for error messages
- Verify that all game files are intact
- Restart the game and try again

## Need Help?
If you encounter any issues not covered in this guide, please:

1. Check the project's GitHub Issues page
2. Create a new issue with detailed problem description
3. Include your system information and error messages if any
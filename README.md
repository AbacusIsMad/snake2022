# ELEC1005 PROJECT2
It's a snake game.
We were provided with `Gluttonous`, it is now `Gluttonous++`.

<p align="center">
  <img src="https://github.com/AbacusIsMad/snake2022/blob/master/README_images/pretty.png" />
</p>

### Features
- Smooth snake connections and animation (borders and connections are clearly shown)
- Lots of different tile types!
    - Wall tiles
    - Empty space that doesn't allow strawberries to spawn
    - Pressure plates: some activate when the snake is on them, the others deactivate
    - Wrap walls: makes the snake go through it and come out of the closest opposite-facing wrap wall
    <p align="center">
        <img src="https://github.com/AbacusIsMad/snake2022/blob/master/README_images/clone1.png" />
    </p>
    - Padded walls: the snake doesn't die when it collides with it
    - Clone plates: generates a copy of the snake with their natural orientation
        - The clone follows the same movements as the original
        - Has an option to generate a clone with different orientation (ie left->right)
        <p align="center">
          <img src="https://github.com/AbacusIsMad/snake2022/blob/master/README_images/clone2.png" />
        </p>
- Level-based gameplay
    - Levels have a requirement to eat `n` strawberries, activate all pressure plates, or both
    - Levels are marked as completed once won (can be reset)
    - 50 homebrewed levels of varying difficulties!
    <p align="center">
          <img src="https://github.com/AbacusIsMad/snake2022/blob/master/README_images/levels.png" />
    </p>
- Level maker
    <p align="center">
        <img src="https://github.com/AbacusIsMad/snake2022/blob/master/README_images/levelmaker.png" />
    </p>
    - Hotkeys to allow easy edits
    - Rectangular and flood select allows for easy manipulation of large areas
        - Select two corners to select a retangle
        - Selecting the same space twice selects all adjacent tiles with of the same type
        <p align="center">
            <img src="https://github.com/AbacusIsMad/snake2022/blob/master/README_images/select1.png" />
        </p>
        <p align="center">
          <img src="https://github.com/AbacusIsMad/snake2022/blob/master/README_images/select2.png" />
        </p>
    - Snake mode allows placment of a snake, and gives hints on where the next segment needs to be
    <p align="center">
        <img src="https://github.com/AbacusIsMad/snake2022/blob/master/README_images/snakemode.png" />
    </p>
- Texture packs, can be configured in `styles`

### Requirements
- Python 3
- pygame

### Running the game
`python3 main.py`

### Packing to an executable
`pyinstaller -F -n BingQi_Ling --add-data "levels:levels" --add-data "sound:sound" --add-data "styles:styles" --add-data "snakeData:snakeData" main.py`

`python3 -m nuitka --onefile --include-data-dir=.=. main.py`

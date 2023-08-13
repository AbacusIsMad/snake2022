# ELEC1005 PROJECT2
It's a snake game.
We were provided with `Gluttonous`, it is now `Gluttonous++`.

![image](https://github.com/AbacusIsMad/snake2022/assets/101756598/9c859b82-7930-4496-95dd-4c5a36f0224d)

### Features
- Smooth snake connections and animation (borders and connections are clearly shown)
![image](https://github.com/AbacusIsMad/snake2022/assets/101756598/42276059-7d53-45d8-83f7-74bb56b271df)
- Lots of different tile types!
    ![image](https://github.com/AbacusIsMad/snake2022/assets/101756598/968269ec-3d1d-480c-b812-a51592fd27b7)
    - Wall tiles
    - Empty space that doesn't allow strawberries to spawn
    - Pressure plates: some activate when the snake is on them, the others deactivate
    - Wrap walls: makes the snake go through it and come out of the closest opposite-facing wrap wall
    - Padded walls: the snake doesn't die when it collides with it
    - Clone plates: generates a copy of the snake with their natural orientation
        - The clone follows the same movements as the original
        - Has an option to generate a clone with different orientation (ie left->right)
        ![clone plates in action - note that while the orientation is preserved the physical location may be very different](https://github.com/AbacusIsMad/snake2022/assets/101756598/45433519-ad95-4a42-8991-78b69c43d52a)
- Level-based gameplay
    - Levels have a requirement to eat `n` strawberries, activate all pressure plates, or both
    - Levels are marked as completed once won (can be reset)
    - 50 homebrewed levels of varying difficulties!
    ![image](https://github.com/AbacusIsMad/snake2022/assets/101756598/3073ef09-eb7c-4db2-9a60-4390e387d731)
- Level maker
    - Hotkeys to allow easy edits
    - Rectangular and flood select allows for easy manipulation of large areas
        - Select two corners to select a retangle
        ![image](https://github.com/AbacusIsMad/snake2022/assets/101756598/52a1068a-a89e-4ded-90ce-db4d763c744c)
        - Selecting the same space twice selects all adjacent tiles with of the same type
        ![image](https://github.com/AbacusIsMad/snake2022/assets/101756598/05930643-d413-4cd2-a298-cd02709c919d)
    - Snake mode allows placment of a snake, and gives hints on where the next segment needs to be
    ![image](https://github.com/AbacusIsMad/snake2022/assets/101756598/88fcfee8-fb10-48fb-b1df-cbbace28f3a8)
- Texture packs, can be configured in `styles`

### Requirements
- Python 3
- pygame

### Running the game
`python3 main.py`

### Packing to an executable
`pyinstaller -F -n BingQi_Ling --add-data "levels:levels" --add-data "sound:sound" --add-data "styles:styles" --add-data "snakeData:snakeData" main.py`

`python3 -m nuitka --onefile --include-data-dir=.=. main.py`

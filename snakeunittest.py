from game import Snake
import pygame, random, unittest 

class TestSnakeMethods(unittest.TestCase): 

    def test_initialiseSnake(self): 
        snake = Snake()
        self.assertEqual(snake.facing, "right", "snake was not initialised in the right position, initialisation test failed")
        self.assertEqual(snake.facing,"right", "snake was not initialised in the right position, initialisation test failed")
        self.assertEqual(snake.position, [6,6], "snake was not initialised in the correct position, initialisation test failed")
        self.assertEqual(snake.segments[0], [6, 6], "snake head was not initialised in the correct position")
        self.assertEqual(snake.segments[1],[5, 6], "snake body was not intiailised in the correct position")
        self.assertEqual(snake.segments[2],[4, 6], "snake tail was not initialised in the correct position")
        self.assertEqual(snake.score, 0, "snake should start with a score of 0, initalisation test failed")

    def test_update(self): 
        snake = Snake()
        snake.update()
        self.assertEqual(snake.position, [7, 6], "Snake did not move right a position, update test failed")

        snake.facing = "left"
        snake.update()
        self.assertEqual(snake.position, [6, 6], "Snake did not move left a position, update test failed")

        snake.facing = "down"
        snake.update()
        self.assertEqual(snake.position, [6, 7], "Snake did not move down a position, update test failed")

        snake.facing = "up"
        snake.update()
        self.assertEqual(snake.position, [6, 6], "Snake did not move upwards a position, update test failed")

if __name__ == "__main__":
    unittest.main()

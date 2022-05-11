from game import Snake, Strawberry, Settings
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

    # Unable to test the graphics (any blit functions) through unit testing, therefore these will be left for end-to-end testing
    
class TestSettings(unittest.TestCase): 

    def test_initialisation(self): 
        settings = Settings()
        self.assertEqual(settings.width, 28, "Width setting not initialised correctly")
        self.assertEqual(settings.height, 28, "Height setting not initialised correctly")
        self.assertEqual(settings.rect_len, 15, "Rectangle length setting not initialised correctly")

class TestStrawberryMethods(unittest.TestCase):

    def test_initialisation(self):
        settings = Settings()
        straw = Strawberry(settings)
        self.assertEqual(straw.settings, settings, "Settings not initialised correctly")
        self.assertEqual(straw.position, [15, 10], "Position was not set correctly for the food item")

    def test_position(self): 
        # hard to test because the function itself uses a random number generator- will simply instead check whether it is in the correct range
        settings = Settings()
        snake = Snake()
        straw = Strawberry(settings)
        straw.random_pos(snake)
        self.assertTrue(straw.position[0] in range(9, 20), "Strawberry was not corrrectly allocated a random position")
        self.assertTrue(straw.position[1] in range(9, 20), "strabwerry was not correctly allocated a random position")

class TestGameMethods(unittest.TestCase): 
    
if __name__ == "__main__":
    unittest.main()
    # coverage run -m unittest snakeunittest.py
    # coverage report

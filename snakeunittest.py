from game import Strawberry, Settings, Game
from snake import Snake
from map import Map
import pygame, random, unittest 

class TestSnakeMethods(unittest.TestCase): 

    def test_initialiseSnake(self): 
        game = Game()
        snake = game.snake


        self.assertEqual(snake.facing, "right", "snake was not initialised in the right position, initialisation test failed")
        self.assertEqual(snake.facing,"right", "snake was not initialised in the right position, initialisation test failed")
        self.assertEqual(snake.segments,[[6, 6], [-1, 0], [-1, 0], [-1, 0]],  "Snake did not have correct segments")
        self.assertEqual(snake.segmentd,[[6, 6], [5, 6], [4, 6], [3, 6]], "Snake did not have correct segments")
        
        self.assertEqual(snake.score, 0, "snake should start with a score of 0, initalisation test failed")

    def test_update(self): 
        game = Game()
        snake = game.snake
        game.map = Map()
        
        # we need to have an arbitrary map directory for testing now 
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
    
# class TestSettings(unittest.TestCase): 

#     def test_initialisation(self): 
#         settings = Settings()
#         self.assertEqual(settings.width, 28, "Width setting not initialised correctly")
#         self.assertEqual(settings.height, 28, "Height setting not initialised correctly")
#         self.assertEqual(settings.rect_len, 15, "Rectangle length setting not initialised correctly")

# class TestStrawberryMethods(unittest.TestCase):

#     def test_initialisation(self):
#         settings = Settings()
#         straw = Strawberry(settings)
#         self.assertEqual(straw.settings, settings, "Settings not initialised correctly")
#         self.assertEqual(straw.position, [15, 10], "Position was not set correctly for the food item")

#     def test_position(self): 
#         # hard to test because the function itself uses a random number generator- will simply instead check whether it is in the correct range
#         settings = Settings()
#         game = Game()
#         snake = game.snake
#         straw = Strawberry(settings)
#         straw.random_pos(snake)
#         self.assertTrue(straw.position[0] in range(9, 20), "Strawberry was not corrrectly allocated a random position")
#         self.assertTrue(straw.position[1] in range(9, 20), "strawberry was not correctly allocated a random position")

# class TestGameMethods(unittest.TestCase): 

#     def test_initialisation(self): 
#         game = Game()
#         self.assertEqual(game.move_dict, {0: 'up', 1: 'down', 2: 'left', 3: 'right'}, "Move dictionary not properly defined")
    
#     def test_restartinggame(self): 
#         game = Game()
#         # set the snake position to an arbitrary value and see if it resets properly
#         game.snake.position = [5, 7]
#         self.assertEqual(game.snake.position, [5, 7])

#         # same for strawberry 
#         game.strawberry.position = [10, 9]
#         self.assertEqual(game.strawberry.position, [10, 9])

#         game.restart_game()
#         self.assertEqual(game.snake.position, [6, 6], "Snake position did not reset when game was reset")
#         self.assertEqual(game.strawberry.position, [15, 10], "Strawbverry position did not reset when game was reset")

#     def test_direction_to_int(self): 
#         game = Game()
#         self.assertEqual(game.direction_to_int('up'), 0, "Did not give correct int for up direction")
#         self.assertEqual(game.direction_to_int('down'), 1, "Did not give correct int for down direction") 
#         self.assertEqual(game.direction_to_int("left"), 2, "Did not give correct int for left direction")
#         self.assertEqual(game.direction_to_int("right"), 3, "Did not give correct int for right direction")


#     #  unable to test blitting the map or the score, this will be left for end to end testing 



if __name__ == "__main__":
    unittest.main()
    # coverage run -m unittest snakeunittest.py
    # coverage report

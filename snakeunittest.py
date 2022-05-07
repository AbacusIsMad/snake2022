from game import Snake
import pygame, random

def initialiseSnake(): 
    snake = Snake()
    assert snake.facing == "right", "snake was not initialised in the right position, initialisation test failed"
    assert snake.position == [6,6], "snake was not initialised in the correct position, initialisation test failed"
    assert snake.score == 0, "snake should start with a score of 0, initalisation test failed"
    print("Initialistion test passed")

if __name__ == "__main__":
    initialiseSnake()
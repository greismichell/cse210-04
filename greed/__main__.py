from game.casting.actor import Actor
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point
from game.casting.gems import Gem
from game.casting.rocks import Rock


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
GAME_OVER_FONT_SIZE = 130
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ITEMS = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    x = int(10)
    y = int(10)
    position = Point(x, y)

    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(position)
    cast.add_actor("banners", banner)

    #create the banner game over
    x = int(MAX_X - 850)
    y = int(MAX_Y - 380)
    
    position = Point(x, y)
    color = Color(255, 0, 0)


    banner_GO = Actor()
    banner_GO.set_text("")
    banner_GO.set_font_size(GAME_OVER_FONT_SIZE)
    banner_GO.set_color(color)
    banner_GO.set_position(position)
    cast.add_actor('game_over',banner_GO )

    #create the level banner
    x = int(MAX_X - 890)
    y = int(MAX_Y - 590)
    
    position = Point(x, y)

    banner_l = Actor()
    banner_l.set_text("")
    banner_l.set_font_size(FONT_SIZE)
    banner_l.set_color(WHITE)
    banner_l.set_position(position)
    cast.add_actor('level',banner_l )
    
    # create the robot
    x = int(MAX_X/2)
    y = int(MAX_Y - CELL_SIZE)
    position = Point(x, y)

    robot = Actor()
    robot.set_font_size(FONT_SIZE-1)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)


    for n in range(DEFAULT_ITEMS):
      
      gem = Gem(CELL_SIZE, FONT_SIZE)
      cast.add_actor("gems",gem)

      rock = Rock(CELL_SIZE, FONT_SIZE)
      cast.add_actor("rocks",rock)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
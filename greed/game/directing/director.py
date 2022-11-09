from game.shared.color import Color
from game.shared.point import Point

WHITE = Color(255, 255, 255)
GREEN = Color(0, 255, 0)
RED = Color(255, 0, 0)

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._level = 0
        self._score = 0
        self._actors = {}
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(Point(velocity.get_x(), 0)) 

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        
        gems = cast.get_actors("gems")
        
        rocks = cast.get_actors("rocks")
        robot = cast.get_first_actor("robots")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
            
        for item in gems + rocks:
            item.set_velocity(Point(0, 1))
            item.move_next(max_x, max_y)
            if robot.get_position().equals(item.get_position()):
                cast.remove_actor(item.get_group(), item) 
                score = self._score + item.get_value()
                if score < 0:
                    self._score = 0
                else:
                    self._score = score
                robot.set_text('/\\')
                if item.get_value() > 0 :
                    robot.set_color(GREEN)
                else:
                    robot.set_color(RED)
                break
            else:
                robot.set_color(WHITE)
                robot.set_text('\./')


    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        
        gems = cast.get_actors("gems")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        rocks = cast.get_actors("rocks")
        gems = cast.get_actors("gems")

       #create 6 levels
        if self._score in range(10, 20):
            self._level = self._score
            self._level = self._level/self._score + 1
            for item in  gems + rocks:
                item.set_velocity(Point(0, 2))
                item.move_next(max_x, max_y)
        
        elif self._score in range(20, 30):
            self._level = self._score
            self._level = self._level/self._score + 2
            for item in  gems + rocks:
                item.set_velocity(Point(0, 3))
                item.move_next(max_x, max_y)

        elif self._score in range(30, 40):
            self._level = self._score
            self._level = self._level/self._score + 3
            for item in  gems + rocks:
                item.set_velocity(Point(0, 4))
                item.move_next(max_x, max_y)
        
        elif self._score in range(40, 50):
            self._level = self._score
            self._level = self._level/self._score + 4
            for item in  gems + rocks:
                item.set_velocity(Point(0, 4))
                item.move_next(max_x, max_y)

        elif self._score >= 50:
            self._level = self._score
            self._level = self._level/self._score + 5
            for item in  gems + rocks:
                item.set_velocity(Point(0, 6))
                item.move_next(max_x, max_y)
        
        
        if len(gems) == 0:
            banner_GO = cast.get_first_actor("game_over")
            banner_GO.set_text("GAME OVER")
            robot = cast.get_first_actor("robots")
            robot.move_next(1, -100)
            
        else: 
            banner_l = cast.get_first_actor("level")
            banner_l.set_text(f"LEVEL: {int(self._level)}")
            banner = cast.get_first_actor("banners")
            banner.set_text(f"Score: {self._score}")

        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
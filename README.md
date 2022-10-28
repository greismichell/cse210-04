> cse210-04
# Greed Game: 
 - [Porpuse](http://github.com/greismichell/cse210-04/blob/main/README.md#Porpuse)
 - [Game Specificatiom](https://github.com/greismichell/cse210-04/blob/main/README.md#Game-Specification)
 - [Game Design](https://github.com/greismichell/cse210-04/blob/main/README.md#Game-Design)
 - [Project Structure](https://github.com/greismichell/cse210-04/blob/main/README.md#Project-Structure)
 - [Getting Started](https://github.com/greismichell/cse210-04/blob/main/README.md#Getting-Started)
 - [Required Technologies](https://github.com/greismichell/cse210-04/blob/main/README.md#Required-Technologies)
 - [Autors](https://github.com/greismichell/cse210-04/blob/main/README.md#Autors)

## Porpuse
---
Develop and demostrate the mastery of the:
- Design software using the principales of programing with classes (abstraction, encapsulation, and inheritance)
  - Design a program using the principal of inheritance

## Game Specification
---
Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!
 ### Greed Rules
   * Gems(*) and rocks(o) randomly apper and fall from the top of the screen.
   * The player(#) can move left or right along the bottom of the screen.
   * If the player touches a gem they earn a point.
   * If the player touches a rock they lose a point.
   * Gems and rocks are removed when the player touches them.
   * The game countinues until the player closes the window.

## Game Design
---
```
Object: Match:
    "Direct a new game."
 
    Responsibility:
    - Control the sequence of play.

    Behaviors:
    - Create a new match game using the keyboard and video services

    State: 

    - Start_game:  Starts the game using the given cast. Runs the main game loop.

    - Get_inputs: Gets directional input from the keyboard and applies it to the user.

    - Do_updates: Updates  the user position and resolves any collision with rocks.

    - Do_outputs: Draws the actors on the screen.


Object: Artifact:
    "A visible, moveable thing that participates in the game."

    Responsibility:  
    - Keep track of its appearance, position and velocity in 2d space.

    Behavior: 
    - Construct news artifacts.

    State: 

    - text (string): The text to display
    - font_size (int): The font size to use.
    - color (Color): The color of the text.
    - position (Point): The screen coordinates.
    - velocity (Point): The speed and direction.


Object: Presentation(Artifact):
    "The message to display"

    Responsibility:
    - provide a message about the artifact.
    Behavior: 
    - message (string): A short description about the artifact.

    State:
    - Get_message: gets the artifac´s message.
    - Set_message: Updates the message to the given one.



Object: Cast:
    "A collection of artifacts."

    Responsibility:
    - keep track of a collection of artifacts. It has methods for adding, removing and getting them by a group name.

    Behavior:  
    - A dictionary of actors { key: group_name, value: a list of  artifacts}

    States:

    - Add_artifact: adss an artifact to the given group.
    - Get_artifacts: get the artifacts in the given group.
    - Get_ all_ the_artifacts: gets all the artifacts in the cast.
    - Get_first_artifact: gets the first artifact in the given group.
    - Remove_artifact: removes an artifact from the given group.


Object: KeyboardService:
    "Detects player input."
   
    Responsibility:
    - Dectect player key presses and translate them into a point representing a direction.

    Behavior:
    - Scalling directional intput to a grip.
   States:
    - Get_ direction: gets the slected direction based on the currently pressed keys.
                  


Object: Video Service:
    "Outputs the game state"

    Responsibility: 
    - The responsibility of the class of objects is to draw the game state on the screen.

    Behaviors:
    - Debug (bool): wheter or not to draw in debug mode.

    States:

    - Clase_window: Closes the window and releases all computing resources.
    - Clear_buffer: Clears the buffer in preparation for the next rendering. This method   should be called at the beginning of the game's output phase.
    - Draw_artifact: Draws the given artifact's text on the screen.
    - Draw_artifacs: Draws the text for the given list of artifacts on the screen.
    - Flush_buffer: Copies the buffer contents to the screen. This method should be called at the end of  the game's output phase.
    - Get_cell_size: Gets the video screen's cell size.
    - Get_height: Gets the video screen's height.
    - Get_width: Gets the video screen's width.
    - Is_window_open: Whether or not the window was closed by the user.
    - Open_window: Opens a new window with the provided title.
    - Draw_grid: Draws a grid on the screen.


Object: Color:
    "A color"

    Responsibility:
    - Hold and provide information about itself. Color has a few convenience methods for comparing them and converting to a tuple.

    Behaviors:
    - Put color through:
        - red (int): The red value.
        - green (int): The green value.
        - blue (int): The blue value.
        - alpha (int): The alpha or opacity.

    Staste:
    - To_tuple: Gets the color as a tuple of four values (red, green, blue, alpha).


Object: Point:
    "A distance from a relative origin (0, 0)."

    Responsinility:
    - Hold and provide information about itself. Point has a few convenience methods for adding, scaling, and comparing them.

    Behaviors:
    - Constructs a new Point using the specified x and y values.

    State:

    - Add:  Gets a new point that is the sum of this and the given one.
    - Equals: Whether or not this Point is equal to the given one.
    - Get_x: "Gets the horizontal distance.
    - Get_y: Gets the vertical distance.
    - Scale: Scales the point by the provided factor.
```

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- greed                 (source code for game)
  +-- data              (data files for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 greed 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Autors
---
- Greis Michell Garcia Villanueva
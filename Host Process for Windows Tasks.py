import pyautogui
import random
import time
import keyboard


class Standard:
    def __init__(self):
        self.min_x_range = 15
        self.max_x_range = 25
        self.min_y_range = 15
        self.max_y_range = 25
        self.min_duration = 1.2
        self.max_duration = 2
        #Must be greater than max duration
        self.check_interval = 2.2
        self.pause_duration = 5
        #Set sensitivity of negation
        self.movement_threshold = 20
        
class IncreasedMovement:
    def __init__(self):
        self.min_x_range = 150
        self.max_x_range = 250
        self.min_y_range = 150
        self.max_y_range = 250
        self.min_duration = 1.2
        self.max_duration = 2
        #Must be greater than max duration
        self.check_interval = 2.2
        self.pause_duration = 5
        #Set sensitivity of negation
        self.movement_threshold = 20
        
# Example of calling the function
def get_user_preset():
    while True:
        preset_run = input("Would you like to use a preset class? (y/n) ").lower()
        if preset_run == "y":
            preset_selection = input("Please choose from the following three preset classes: [Standard]  ||  [IncreasedMovement]")
            
            if preset_selection == "Standard" or preset_selection == "IncreasedMovement":
                
            #need to do something here
            # need to return the choice as a numerical value passed
        elif preset_run == "n":
            return 0
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def get_user_input():
    #If preset was chosen, skip manual player input
    if get_user_preset() != 0:
        return

    try:
        min_x_range = int(input("Enter the minimum range for X direction movement: "))
        max_x_range = int(input("Enter the maximum range for X direction movement: "))
        min_y_range = int(input("Enter the minimum range for Y direction movement: "))
        max_y_range = int(input("Enter the maximum range for Y direction movement: "))
        min_duration = float(input("\nEnter the minimum duration for each movement (in seconds): "))
        max_duration = float(input("Enter the maximum duration for each movement (in seconds): "))
        check_interval = float(input("\nEnter the user input detection interval (in seconds): "))
        pause_duration = float(input("Enter the pause duration after detecting user input (in seconds): "))
        movement_threshold = float(input("\nEnter the movement threshold to detect user input: "))
        return min_x_range, max_x_range, min_y_range, max_y_range, min_duration, max_duration, check_interval, pause_duration, movement_threshold
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get_user_input()

def move_mouse_randomly(min_x_range, max_x_range, min_y_range, max_y_range, min_duration, max_duration):
    # Randomly choose a movement distance within the specified range for X and Y directions
    x_move = random.randint(min_x_range, max_x_range) * random.choice([-1, 1])
    y_move = random.randint(min_y_range, max_y_range) * random.choice([-1, 1])
    
    # Randomly choose a duration for the movement within the specified range
    duration = random.uniform(min_duration, max_duration)
    
    # Move the mouse relative to its current position by the chosen distances over the chosen duration
    pyautogui.moveRel(x_move, y_move, duration)
    
    return pyautogui.position()

def main():
    min_x_range, max_x_range, min_y_range, max_y_range, min_duration, max_duration, check_interval, pause_duration, movement_threshold = get_user_input()
    last_mouse_position = pyautogui.position()
    script_moving = False
    paused = False

    print("Press Ctrl+Shift+P to pause/resume the script.")

    while True:
        # Check if the pause/resume hotkey is pressed
        if keyboard.is_pressed('ctrl+shift+p'):
            paused = not paused
            if paused:
                print("Script paused. Press Ctrl+Shift+P to resume.")
            else:
                print("Script resumed. Press Ctrl+Shift+P to pause.")
            time.sleep(1)  # Prevents rapid toggling

        if paused:
            continue

        # Wait for the specified check interval before checking for user input
        time.sleep(check_interval)
        current_mouse_position = pyautogui.position()
        
        # Calculate the distance moved by the mouse since the last check
        distance_moved = ((current_mouse_position[0] - last_mouse_position[0]) ** 2 + (current_mouse_position[1] - last_mouse_position[1]) ** 2) ** 0.5
        
        # If the distance moved is greater than the threshold, assume user input and pause the program
        if distance_moved > movement_threshold:
            print("Mouse input detected. Pausing program.")
            time.sleep(pause_duration)
            last_mouse_position = current_mouse_position
            continue
        
        # If no significant user input is detected, move the mouse randomly
        script_moving = True
        last_mouse_position = move_mouse_randomly(min_x_range, max_x_range, min_y_range, max_y_range, min_duration, max_duration)

if __name__ == "__main__":
    main()

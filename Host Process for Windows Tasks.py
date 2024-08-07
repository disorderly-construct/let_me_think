import pyautogui
import random
import time

# Using error handling to initiate function
def get_user_input():
    try:
        min_x_range = int(input("Enter the minimum range for X direction movement: "))
        max_x_range = int(input("Enter the maximum range for X direction movement: "))
        min_y_range = int(input("Enter the minimum range for Y direction movement: "))
        max_y_range = int(input("Enter the maximum range for Y direction movement: "))
        min_duration = float(input("\nEnter the minimum duration for each movement (in seconds): "))
        max_duration = float(input("Enter the maximum duration for each movement (in seconds): \n"))
        check_interval = float(input("Enter the user input detection interval (in seconds): \n"))
        pause_duration = float(input("Enter the pause duration after detecting user input (in seconds): "))
        movement_threshold = float(input("Enter the movement threshold to detect user input: "))
        return min_x_range, max_x_range, min_y_range, max_y_range, min_duration, max_duration, check_interval, pause_duration, movement_threshold
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get_user_input()

def move_mouse_randomly(min_x_range, max_x_range, min_y_range, max_y_range, min_duration, max_duration):
    # Randomly choose a movement distance within the specified range for X and Y directions, extending from -1 to 1
    # creating a diameter from range values :D
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

    while True:
        # Wait for the specified check interval before checking for user input
        time.sleep(check_interval)
        current_mouse_position = pyautogui.position()
        
        # Calculate the distance moved by the mouse since the last check
        distance_moved = ((current_mouse_position[0] - last_mouse_position[0]) ** 2 + (current_mouse_position[1] - last_mouse_position[1]) ** 2) ** 0.5
        
        # If the script moved the mouse, skip the user input check
        if script_moving:
            script_moving = False
        else:
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

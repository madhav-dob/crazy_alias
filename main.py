import keyboard
from pynput.keyboard import Key, Controller
import time
target_keys = {"alt", "9"}

# Define the text you want to type when the combination is detected
text_to_type = "Hello, World!"
typer = Controller()
# Initialize a set to keep track of the currently pressed keys
pressed_keys = set()
# Define the action to be performed when the combination is detected
def perform_action():
    print("Key combination detected")
    time.sleep(0.1)

    typer.press('a')
    typer.release('a')


# Create a listener to monitor key events
def key_event_handler(e):
    if e.event_type == keyboard.KEY_DOWN:
        pressed_keys.add(e.name)
        if all(key in pressed_keys for key in target_keys):
            perform_action()
    elif e.event_type == keyboard.KEY_UP:
        pressed_keys.discard(e.name)

# Start the keyboard listener
keyboard.hook(key_event_handler)

# Keep the program running
keyboard.wait("esc")  # You can change "esc" to any key to exit the program

# Clean up
keyboard.unhook_all()

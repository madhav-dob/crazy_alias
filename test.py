from pynput import keyboard
import pyautogui

def on_key_press(key):
    try:
        # Check if the pressed key is 'a'
        if key.char == 'a':
            print("The 'a' key was pressed.")
            # Type the letter 'X' using pyautogui
            pyautogui.typewrite('X')
    except AttributeError:
        # Handle special keys like Shift, Ctrl, etc.
        pass

def on_key_release(key):
    # Implement this function if needed.
    pass

# Create a keyboard listener
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
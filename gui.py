import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from mousejiggler import MouseJiggler
import sys, os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

mouse_jiggler = MouseJiggler()

def validate_input_boxes(input):
    return input.isdigit() or input == ""

def on_press(event):
    global mouse_jiggler
    print(f"key {event.keysym} pressed!")
    if event.keysym == 'Escape' and mouse_jiggler.is_alive():
        mouse_jiggler.stop()
        mouse_jiggler.join()

def get_ponsuke():
    img = Image.open(resource_path("./ponsuke.jpeg"))
    max_size = (600,300)
    img.thumbnail(max_size)
    return ImageTk.PhotoImage(img)

window = tk.Tk()
window.title("wacho's mouse jiggler")
window.geometry("600x450")

input_label = ttk.Label(window, text="how long should i jiggle for?")

reg = (window.register(validate_input_boxes), "%P")

hours_label = ttk.Label(window, text="hrs")
hours_input = ttk.Entry(window, validate="key", validatecommand=reg)
hours_input.insert(0, "0")
def zero_hours(event):
    if hours_input.get() == '':
        hours_input.insert(0, "0")
hours_input.bind('<FocusOut>', zero_hours)

minutes_label = ttk.Label(window, text="mins")
minutes_input = ttk.Entry(window, validate="key", validatecommand=reg)
minutes_input.insert(0, "0")
def zero_minutes(event):
    if minutes_input.get() == '':
        minutes_input.insert(0, "0")
minutes_input.bind('<FocusOut>', zero_minutes)

seconds_label = ttk.Label(window, text="secs")
seconds_input = ttk.Entry(window, validate="key", validatecommand=reg)
seconds_input.insert(0, "0")
def zero_seconds(event):
    if seconds_input.get() == '':
        seconds_input.insert(0, "0")
seconds_input.bind('<FocusOut>', zero_seconds)

def start():
    global mouse_jiggler
    if not mouse_jiggler.is_alive():
        hrs = int(hours_input.get())
        mins = int(minutes_input.get())
        secs = int(seconds_input.get())
        total_time = secs + mins*60 + hrs*3600

        mouse_jiggler = MouseJiggler(total_time)
        mouse_jiggler.start()

start_button = ttk.Button(window, text="start!", command=start)

def start_infinite():
    global mouse_jiggler
    if not mouse_jiggler.is_alive():
        mouse_jiggler = MouseJiggler()
        mouse_jiggler.start()

start_infinite_label = ttk.Label(window, text="or just jiggle until you tell it to stop (press esc)")
start_infinite_button = ttk.Button(window, text="jiggle infinitely!", command=start_infinite)

ponsuke = get_ponsuke()
ponsuke_label = ttk.Label(window, image=ponsuke)

input_label.grid(column=1, row=0)

hours_label.grid(column=0, row=1)
hours_input.grid(column=0, row=2)
minutes_label.grid(column=1, row=1)

minutes_input.grid(column=1, row=2)
seconds_label.grid(column=2, row=1)
seconds_input.grid(column=2, row=2)

start_button.grid(column=1, row=3)

start_infinite_label.grid(column=0, row=4, columnspan=3)
start_infinite_button.grid(column=1, row=5)

ponsuke_label.grid(column=0, row=6, columnspan=3)

window.bind('<Key>', on_press)

window.mainloop()
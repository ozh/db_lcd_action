import os
import sys
from datetime import datetime

from PIL import Image,ImageDraw,ImageFont

from utils.params import LCD_SCREEN, get_db_thresholds

if sys.platform == "win32":
    # On windows, we will use tkinter to display the image
    from tkinter import Tk, Label
    from PIL import ImageTk


def show_image_from_db_level(db_level: int):
    """
    Show an image based on the decibel level on the LCD screen.
    :param db_level: Decibel level to display.
    """
    image = make_image_from_db_level(db_level)
    lcd_show_image(image)


def make_image_from_db_level(db_level: int) -> Image:
    """
    Create an image based on the decibel level.
    :param db_level:
    :return:
    """
    db_thresh_low, db_thresh_medium = get_db_thresholds()

    # Create image on the fly
    if db_level < db_thresh_low:
        image_filename = "assets/db_levels/green.jpg"
        whitish = (144, 191, 174)
    elif db_level < db_thresh_medium:
        image_filename = "assets/db_levels/orange.jpg"
        whitish = (235, 185, 145)
    else:
        image_filename = "assets/db_levels/red.jpg"
        whitish = (235, 141, 141)

    image = Image.open(image_filename)
    draw = ImageDraw.Draw(image)

    # DB level text
    draw_text(draw=draw, text=f"{db_level} dB", text_size=46, color="white", position={'y': 117}, font='assets/fonts/Verdana.ttf')

    # Update min / max level
    min_level, max_level = get_min_max(db_level)
    draw_text(draw=draw, text=min_level, text_size=18, color=whitish, position={'x': 78, 'y': 28}, font='assets/fonts/Verdana.ttf')
    draw_text(draw=draw, text=max_level, text_size=18, color=whitish, position={'x': 143, 'y': 28}, font='assets/fonts/Verdana.ttf')

    # Update hour in hh:mm:ss format
    current_time = datetime.now().strftime("%H:%M:%S")
    draw_text(draw=draw, text=current_time, text_size=24, color="white", position={'y': 186}, font='assets/fonts/DejaVuSansMono.ttf')

    return image




def draw_text(draw, text, text_size, color, position, font):
    """
    Draw text on the image with specified parameters.
    :param draw:  ImageDraw object to draw on the image
    :param text:  Text to draw on the image
    :param text_size:  Size of the text to draw
    :param color:  Color of the text to draw
    :param position:  Position to draw the text on the image, can be a dict with one or both 'x' and 'y' keys
    :param font:  Font file to use for the text
    :return:  None
    """
    text = str(text)
    font = ImageFont.truetype(font, text_size)
    _, _, text_width, text_height = font.getbbox(text)

    if 'x' in position:
        x = position['x']
    else:
        x = (240 - text_width) // 2

    if 'y' in position:
        y = position['y']
    else:
        y = (240 - text_height) // 2

    position = (x, y)
    draw.text(position, text, fill=color, font=font)


def get_min_max(level):
    """
    Get the minimum and maximum decibel levels so far

    :param level:
    :return: min, max
    """
    try:
        if level < get_min_max.min:
            get_min_max.min = level
    except AttributeError:
        get_min_max.min = level

    try:
        if level > get_min_max.max:
            get_min_max.max = level
    except AttributeError:
        get_min_max.max = level

    return get_min_max.min, get_min_max.max


def lcd_backlight(level: int = 50):
    """
    Set the backlight of the LCD screen.
    :param level: Backlight level (0-100).
    """
    LCD_SCREEN.bl_DutyCycle(level)


def lcd_clear():
    """
    Clear the LCD screen.
    """
    LCD_SCREEN.clear()


def lcd_show_image(image: Image):
    """
    Show an image on the LCD screen.
    :param image: Image to display.
    """
    if sys.platform == "win32":
        windows_display_image(image)
    else:
        LCD_SCREEN.ShowImage(image)


def windows_display_image(image: Image):
    """
    Display image on Windows using tkinter.
    If the tkinter window is already open, it will update the image.
    :param image: Image to display.
    """
    root = Tk()
    root.title("Decibel Level Display")
    root.geometry(f"{image.width}x{image.height}")

    # Convert the image to a format tkinter can use
    tk_image = ImageTk.PhotoImage(image)

    label = Label(root, image=tk_image)
    label.pack()

    # Start the tkinter main loop
    root.mainloop()

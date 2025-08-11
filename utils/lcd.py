import os
import sys
from datetime import datetime

from PIL import Image,ImageDraw,ImageFont

from utils.constants import LCD_SCREEN, DB_THRESH_LOW, DB_THRESH_MEDIUM

if sys.platform == "win32":
    # On windows, we will use tkinter to display the image
    from tkinter import *
    from PIL import ImageTk, Image


def show_image_from_db_level(db_level: int):
    """
    Show an image based on the decibel level on the LCD screen.
    :param db_level: Decibel level to display.
    """
    image = get_or_make_image_from_db_level(db_level)
    lcd_show_image(image)


def get_or_make_image_from_db_level(db_level: int) -> Image:
    """
    Create an image based on the decibel level.
    :param db_level:
    :return:
    """
    # Check if "db_level_XXX.jpg" exists in assets/db_levels/
    image_filename = f"assets/db_levels/db_level_{db_level}.jpg"

    # if os.path.exists(image_filename):
    #     return Image.open(image_filename)

    # Create image on the fly
    if db_level < DB_THRESH_LOW:
        image_filename = "assets/db_levels/green.jpg"
        whitish = (144, 191, 174)
    elif db_level < DB_THRESH_MEDIUM:
        image_filename = "assets/db_levels/orange.jpg"
        whitish = (235, 185, 145)
    else:
        image_filename = "assets/db_levels/red.jpg"
        whitish = (235, 141, 141)

    image = Image.open(image_filename)
    draw = ImageDraw.Draw(image)

    # DB level text
    draw_text(draw=draw, text=f"{db_level} dB", text_size=35, color="white", position={'y': 125}, font='assets/fonts/Verdana.ttf')

    # Update min / max level
    min_level, max_level = get_min_max(db_level)
    draw_text(draw=draw, text=min_level, text_size=12, color=whitish, position={'x': 79, 'y': 32}, font='assets/fonts/Verdana.ttf')
    draw_text(draw=draw, text=max_level, text_size=12, color=whitish, position={'x': 147, 'y': 32}, font='assets/fonts/Verdana.ttf')

    # Update hour in hh:mm:ss format
    current_time = datetime.now().strftime("%H:%M:%S")
    draw_text(draw=draw, text=current_time, text_size=18, color="white", position={'y': 186}, font='assets/fonts/DejaVuSansMono.ttf')

    return image


def draw_text(draw, text, text_size, color, position, font):
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

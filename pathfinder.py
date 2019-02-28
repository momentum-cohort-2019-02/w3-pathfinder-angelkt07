from PIL import Image, ImageDraw
import os

def get_elevation_lists(file_name):
    """
    given a file with elevation data, read each line and return a list for each line.
    """

    with open(file_name) as file:
        elevation_list = [line.strip().lower() for line in file]

    return elevation_list


if __name__ == "__main__":
    pass
from PIL import Image, ImageDraw, ImageColor
import os


def get_elevation_lists(file_name):
    """
    given a file with elevation data, read each line and return a new number for the percentage of color for each line.
    """
    elevation_list = []
    with open(file_name) as file:
        for item in file:
            elevation_list = [int((int(item)-3139)/(5648-3139) * 255) for item in file.read().split()]
            elevation_list = zip(elevation_list, elevation_list, elevation_list)

    return elevation_list



def get_map_image(mapIm):
    """
    takes the range of the picture and creates all possible points
    """
    elevation_list_junior = []
    for top in range(0, height):
        for left in range(0, width):
            elevation_list_junior.append((left, top))
            # print(left, top)
        
    return elevation_list_junior

def get_dictionary(elevation_list_junior, elevation_list):
    """
    creates a dictonairy with all of the points and associated color percentage
    """
    elevation_dictionary = dict(zip(elevation_list_junior, elevation_list))
    return elevation_dictionary


class MapImage:

    def __init__(self, width, height):
        self.width = width
        self.height = height


if __name__ == "__main__":
    file_name = 'elevation_small.txt'
    mapIm = Image.new('RGBA', (600, 600))

    width, height = mapIm.size

    # # print(get_elevation_lists(file_name))
    # print(get_map_image(mapIm))
    # print(get_dictionary(get_map_image(mapIm), get_elevation_lists(file_name)))

    for key, value in get_dictionary(get_map_image(mapIm), get_elevation_lists(file_name)).items():
        mapIm.putpixel(key, value)

    mapIm.save('map.png')





# # https://www.w3resource.com/python-exercises/file/python-io-exercise-9.php for how to figure out lines. I drew a blank and found enumerate. 
# def file_lengthy(file_name):
#     with open(file_name) as f:
#             for items, line in enumerate(f):
#                 pass
#     return items + 1



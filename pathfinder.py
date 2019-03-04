from PIL import Image, ImageDraw, ImageColor
import pprint
import math
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

# def get_elevations(file_name_two):
# """
# given a file with elevation data, read each line and return a new number for the percentage of color for each line.
# """
file_name_two = 'elevation_small.txt'
elevations = []
with open(file_name_two) as file:
    for line in file:
        elevations.append([int((int(item)-3139)/(5648-3139) * 255) for item in line.split()])

# return elevations

def get_dictionary_two(elevation_list_junior, elevations):
    """
    creates a dictonairy with all of the points and associated elevation
    """
    elevation_dictionary_two = dict(zip(elevation_list_junior, elevations))
    return elevation_dictionary_two



def possibly_path(cur_x, cur_y):
    pass



if __name__ == "__main__":
    file_name = 'elevation_small.txt'
    file_name_two = 'elevation_small.txt'
    mapIm = Image.new('RGBA', (600, 600))

    width, height = mapIm.size


    for key, value in get_dictionary(get_map_image(mapIm), get_elevation_lists(file_name)).items():
        mapIm.putpixel(key, value)
        print(key, value)

    # print(elevations)

    # for key, value in get_dictionary(get_map_image(mapIm), get_elevation_lists(file_name)).items():
    #     print(key, value)

    # for key in get_dictionary(get_map_image(mapIm), get_elevation_lists(file_name)).get((598, 0)):
    # print(get_dictionary(get_map_image(mapIm), get_elevation_lists(file_name))[(598, 0)])

    

    mapIm.save('map.png')





# # https://www.w3resource.com/python-exercises/file/python-io-exercise-9.php for how to figure out lines. I drew a blank and found enumerate. 
# def file_lengthy(file_name):
#     with open(file_name) as f:
#             for items, line in enumerate(f):
#                 pass
#     return items + 1


# print(get_elevation_lists(file_name))
# print(get_map_image(mapIm))
# print(get_dictionary(get_map_image(mapIm), get_elevation_lists(file_name)))



from PIL import Image, ImageDraw
import os


class ElevationList:

    def get_elevation_lists(file_name):
        """
        given a file with elevation data, read each line and return a list for each line.
        """

        with open(file_name) as file:
            elevation_list = [line.strip().lower() for line in file]

        return elevation_list

class CreateMap:
    pass
    # def create_image():
    #     #TODO: the lab says the area of the mountians is 90m x 90m and the is 8100 meters according to Google. Not entirely sure how to make this into (top, left) = (0,0) and (bottom, right) = (??)
    #     os.makedirs('forMap', exist_ok=True)

    #     elevation_map = Image.new('RGBA', (90, 90))
    #     elevation_map.getpixel((0, 0))

    #     for x in range(100):
    #         for y in range(50):
    #             elevation_map.putpixel((x, y), (210, 210, 210))
        
    #     for x in range(100):
    #         for y in range(50, 100):
    #             elevation_map.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
        
    #     elevation_map.save(os.path.join('forMap','map.png'))

    def create_map(elevation_list):
        pass


if __name__ == "__main__":
    pass
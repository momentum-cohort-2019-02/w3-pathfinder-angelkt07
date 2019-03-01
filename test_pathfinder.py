from pathfinder import get_elevation_lists
from PIL import Image


def test_get_elevation_lists():
    run_file = get_elevation_lists('elevation_small.txt')
    assert type(run_file) == zip




# def test_get_map_image():
#     run_image = get_map_image('RGBA', (600, 600))
#     assert type(run_image) == list


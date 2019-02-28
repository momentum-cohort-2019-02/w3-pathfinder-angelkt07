from pathfinder import get_elevation_lists

def test_get_elevation_lists():
    run_file = get_elevation_lists('elevation_small.txt')
    assert type(run_file) == list
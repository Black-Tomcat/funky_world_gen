import json
import random
import itertools


from src.rangeDict import RangeDict
from src.terrain import Terrain

WORLD_WIDTH = 100
WORLD_HEIGHT = 100

world = []
TERRAIN_RANGES = RangeDict({
    range(1, 3): Terrain("DEEP WATER", "ACCBE1", range(1, 3)),
    range(3, 5): Terrain("SHALLOW WATER", "CEE5F2", range(3, 5)),
    range(5, 7): Terrain("GRASSLANDS", "588157", range(5, 7)),
    range(7, 9): Terrain("HILLS", "B2987B", range(7, 9)),
    range(9, 11): Terrain("MOUNTAINS", "4C5459", range(9, 11))
})


def generate_world(func):
    def wrapper():
        for x in range(WORLD_WIDTH):
            world.append([])
            for y in range(WORLD_HEIGHT):
                world[x].append(func(x, y))
    return wrapper


@generate_world
def generate_random_world(*args):
    terrain_height = random.randint(1, 10)
    terrain_type = TERRAIN_RANGES[terrain_height]

    final = terrain_type.create_copy(terrain_height).__dict__
    return final


@generate_world
def generate_gradient_world(x, y):
    terrain_height = (x + y) / (WORLD_HEIGHT + WORLD_WIDTH) * 10 + 1
    terrain_type = TERRAIN_RANGES[terrain_height]

    final = terrain_type.create_copy(terrain_height).__dict__
    return final


def return_world():
    print(json.dumps(
        {
            "metadata": {
                "width": WORLD_WIDTH,
                "height": WORLD_HEIGHT
            },
            "world": world
        }
    ))


if __name__ == '__main__':
    generate_gradient_world()
    return_world()

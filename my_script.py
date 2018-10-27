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


def generate__random_world():
    for x in range(WORLD_WIDTH):
        world.append([])
        for y in range(WORLD_HEIGHT):
            terrain_height = random.randint(1, 10)
            terrain_type = TERRAIN_RANGES[terrain_height]

            final = terrain_type.create_copy(terrain_height).__dict__
            world[x].append(final)


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
    generate__random_world()
    return_world()

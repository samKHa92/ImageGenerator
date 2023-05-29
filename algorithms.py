import random
import functions
import utils


def random_algorithm(width, height, colors, count, gen_path, new_dir):
    for i in range(count):
        array = functions.generate_empty_2d_array(height)
        for h in range(height):
            for w in range(width):
                array[h].append(colors[random.randint(0, len(colors)-1)])
        utils.generate_image(f"{gen_path}/{new_dir}", i, array)



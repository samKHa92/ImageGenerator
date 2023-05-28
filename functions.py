def generate_colors(red_max_depth, green_max_depth, blue_max_depth):
    colors = []
    for r in range(0, 256, 256 // red_max_depth):
        for g in range(0, 256, 256 // green_max_depth):
            for b in range(0, 256, 256 // blue_max_depth):
                colors.append((r, g, b))
    return colors


def generate_flat_dictionary(width, height, colors):
    flat_dictionary = {}
    for h in range(height):
        for w in range(width):
            for c in colors:
                if (h, w) in flat_dictionary.keys():
                    flat_dictionary[(h, w)].append(c)
                else:
                    flat_dictionary[(h, w)] = [c]
    return flat_dictionary


def generate_empty_2d_array(height):
    array = []
    for h in range(height):
        array.append([])
    return array

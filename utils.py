import json
import cv2
import numpy


def generate_image(path, identifier, array):
    array = numpy.array(array)
    cv2.imwrite(f"{path}/img{identifier}.png", array)


def last_logged_id(path):
    file = open(path)
    data = json.loads(file.read())
    return len(data["logs"])


def add_log(path, new_data):
    with open(path, 'r+') as file:
        file_data = json.load(file)
        file_data["logs"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

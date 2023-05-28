import datetime
import os
from datetime import datetime
import algorithms
import functions
import utils


def run(red_max_depth, green_max_depth, blue_max_depth, width, height, count, algorithm, gen_path, log_path):
    gen_id = utils.last_logged_id(log_path) + 1
    new_dir = f"gen_{gen_id}"
    os.makedirs(f"{gen_path}/{new_dir}")
    start_time = datetime.now()

    colors = functions.generate_colors(red_max_depth, green_max_depth, blue_max_depth)

    if algorithm == "random":
        algorithms.random_algorithm(
            width=width,
            height=height,
            colors=colors,
            count=count,
            gen_path=gen_path,
            new_dir=new_dir
        )

    end_time = datetime.now()
    diff = end_time - start_time
    log_data = {
        "id": gen_id,
        "count": count,
        "photos": {
            "height": height,
            "width": width,
            "red_depth": red_max_depth,
            "green_depth": green_max_depth,
            "blue_depth": blue_max_depth
        },
        "algorithm_used": algorithm,
        "start_date": str(start_time),
        "end_date": str(end_time),
        "time used": str(diff)
    }
    utils.add_log(log_path, log_data)

    print(log_data)

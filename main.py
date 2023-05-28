import run

if __name__ == '__main__':
    run.run(
        red_max_depth=32,
        green_max_depth=32,
        blue_max_depth=32,
        width=128,
        height=128,
        count=3,
        algorithm="random",
        gen_path="generated_images",
        log_path="logs.json"
    )

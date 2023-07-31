import json

# resize grid ||| start
"""
YOUR CODE HERE
"""
# resize grid ||| end


def print_grid(config):
    grid = ''
    for folder_id, value in config["front"]["buttons"].items():
        for count, button_config in enumerate(config["front"]["buttons"][folder_id], start=1):
            if len(str(count)) == 1:
                countstr = f' {count} '
            elif len(str(count)) == 2:
                countstr = f'{count} '
            else:
                countstr = f'{count}'

            grid += '[   ]' if 'VOID' in button_config else f'[{countstr}]'
            # \n
            if count % int(config['front']['width']) == 0:
                grid += '\n'
        grid += '\n\n'
    print(grid)
                
                
while True:
    print('==========================================================')
    with open('config.json', encoding="utf-8") as f:
        config = json.load(f)

    print(f"Current Height : {config['front']['height']}")
    print(f"Current Width  : {config['front']['width']}")
    print(f"{config['front']['height']}x{config['front']['width']}")

    input_ = input("new gridsize (example:4x8): ")
    if input_.lower() not in ['print','p','']:
        newGridSize = input_.lower().strip().split('x')
        config['front']['height'] = newGridSize[0]
        config['front']['width'] = newGridSize[1]
        with open('config.json', 'w', encoding="utf-8") as json_file:
            json.dump(config, json_file, indent=4)
        update_gridsize(config)

        print(f"New Height : {config['front']['height']}")
        print(f"New Width  : {config['front']['width']}")
        print(f"{config['front']['height']}x{config['front']['width']}")

    print_grid(config)

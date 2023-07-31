import json

# resize grid ||| start

def create_matrix(buttons, height, width):
    matrix = [[{"VOID": "VOID"} for _ in range(width)] for _ in range(height)]
    for index, button in enumerate(buttons):
        row = index // width
        col = index % width
        if row < height and col < width:
            matrix[row][col] = button
    return matrix

def is_void_line(line):
    return all(button == {"VOID": "VOID"} for button in line)

def delete_void_lines(matrix):
    matrix = [line for line in matrix if not is_void_line(line)]
    transposed_matrix = list(map(list, zip(*matrix)))
    transposed_matrix = [line for line in transposed_matrix if not is_void_line(line)]
    return list(map(list, zip(*transposed_matrix)))

def resize_grid(matrix, height, width):
    current_height = len(matrix)
    current_width = len(matrix[0]) if matrix else 0

    if current_height > height:
        matrix = delete_void_lines(matrix)
        current_height = len(matrix)
        if current_height > height:
            raise ValueError(f"The grid has {current_height} non-void rows which is more than the desired height of {height}. Please reduce the number of non-void rows.")
    elif current_height < height:
        for _ in range(height - current_height):
            matrix.append([{"VOID": "VOID"} for _ in range(current_width)])

    if current_width > width:
        matrix = list(map(list, zip(*matrix)))
        matrix = delete_void_lines(matrix)
        current_width = len(matrix[0]) if matrix else 0
        if current_width > width:
            raise ValueError(f"The grid has {current_width} non-void columns which is more than the desired width of {width}. Please reduce the number of non-void columns.")
        matrix = list(map(list, zip(*matrix)))
    elif current_width < width:
        for line in matrix:
            line.extend([{"VOID": "VOID"} for _ in range(width - current_width)])

    return matrix

def update_gridsize(config):
    buttons = config["front"]["buttons"]["index"]
    new_height = int(config['front']['height'])
    new_width = int(config['front']['width'])

    matrix = create_matrix(buttons, new_height, new_width)
    matrix = resize_grid(matrix, new_height, new_width)

    config["front"]["buttons"]["index"] = [button for line in matrix for button in line]
    config["front"]["height"] = str(len(matrix))
    config["front"]["width"] = str(len(matrix[0]) if matrix else 0)

    with open('config.json', 'w', encoding="utf-8") as json_file:
        json.dump(config, json_file, indent=4)
        
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
                
                
                
with open('config.json', encoding="utf-8") as f:
    config = json.load(f)

print(f"Current Height : {config['front']['height']}")
print(f"Current Width  : {config['front']['width']}")
print(f"{config['front']['height']}x{config['front']['width']}")

input_ = input("new gridsize (example:`4x8`): ")
if input_.lower() not in ['print','p']:
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

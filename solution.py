import json

# resize grid ||| start

def create_matrix(config):
    matrix = []
    for folder_count, (folder_name, folder_content) in enumerate(config["front"]["buttons"].items()):
        row_count = 0
        matrix.append([])
        for count, button in enumerate(folder_content, start=1):
            if row_count >= len(matrix[folder_count]):
                matrix[folder_count].append([])
            matrix[folder_count][row_count].append(button)
            if count % int(config['front']['width']) == 0:
                row_count += 1
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    return matrix

def unmatrix(matrix):
    
    for folder_count, folder in enumerate(matrix):
        folderName = list(config['front']['buttons'])[folder_count]
        config["front"]["buttons"][folderName] = []
        for row in folder:
            for button in row:
                config["front"]["buttons"][folderName].append(button)
            
            
    return config

def update_gridsize(config, new_height, new_width):
    new_height, new_width = int(new_height), int(new_width)
    matrix = create_matrix(config)
    old_height, old_width = int(config['front']['height']), int(config['front']['width'])

    # if height has changed
    if old_height != new_height:


        # if the height has increased
        if new_height > old_height:
            difference = new_height - old_height
            for count, _ in enumerate(range(difference), start=1):
                for folder_name, folder_content in config["front"]["buttons"].items():
                    for _ in range(old_width):
                        # if count % 2 == 0:
                        #     folder_content.insert(0, {"VOID": "VOID"})
                        # else:
                        folder_content.append({"VOID": "VOID"})
            matrix = create_matrix(config)


        # if the height has decreased
        if old_height > new_height:
            difference = old_height - new_height
            print('height decreased')
            for count, _ in enumerate(range(difference), start=1):
                for folder_count, folder in enumerate(matrix):
                    for row_count, row in enumerate(reversed(folder)):
                        if all(element == {"VOID": "VOID"} for element in row):
                            folder.remove(row)
                            break
                            
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # we need to be able to remove à row even if theres no row full of voids.
        # and I DON'T KNOW how to do that I need help


    # if width has changed
    if old_width != new_width:
        
        # if the width has increased
        if new_width > old_width:
            
            
            difference = new_width - old_width
            new_matrix = matrix
            for count, _ in enumerate(range(difference), start=1):
                for folder_count, folder in enumerate(matrix):
                    for row_count, row in enumerate(folder):
                        # if count % 2 == 0:
                        #     new_matrix[folder_count][row_count].insert(0, {"VOID": "VOID"})
                        # else:
                        new_matrix[folder_count][row_count].append({"VOID": "VOID"})
            matrix = new_matrix
            
            
        if new_width < old_width:
            print('width decreased')



    config = unmatrix(matrix)
    print(old_height, new_height)
    print(old_width, new_width)
    return config


# resize grid ||| end



# you don't have to touch that
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

    input_ = input("new gridsize (example:'4x8' or press enter to just print): ")
    if input_.lower() not in ['print','p','']:
        newGridSize = input_.lower().strip().split('x')
        
        config = update_gridsize(config, newGridSize[0], newGridSize[1])
        
        config['front']['height'] = newGridSize[0]
        config['front']['width'] = newGridSize[1]
        with open('config2.json', 'w', encoding="utf-8") as json_file:
            json.dump(config, json_file, indent=4)

        print(f"New Height : {config['front']['height']}")
        print(f"New Width  : {config['front']['width']}")
        print(f"{config['front']['height']}x{config['front']['width']}")

    print_grid(config)

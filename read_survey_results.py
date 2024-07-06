import json
import pandas as pd

# Path to the JSON file
file_path = 'export_1720008724702.json'

llava_wins = 0
cogvlm_wins = 0
deepseek_wins = 0

no_votes = 0
with_votes = 0

composition_llava = 0
composition_cogvlm = 0
composition_deepseek = 0

balance_llava = 0
balance_cogvlm = 0
balance_deepseek = 0

movement_llava = 0
movement_cogvlm = 0
movement_deepseek = 0

contrast_llava = 0
contrast_cogvlm = 0
contrast_deepseek = 0

ground_llava = 0
ground_cogvlm = 0
ground_deepseek = 0

symmetry_llava = 0
symmetry_cogvlm = 0
symmetry_deepseek = 0

eye_llava = 0
eye_cogvlm = 0
eye_deepseek = 0

focus_llava = 0
focus_cogvlm = 0
focus_deepseek = 0

proportion_llava = 0
proportion_cogvlm = 0
proportion_deepseek = 0

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)


# Iterate through each dictionary in the list and print key-value pairs
for item in data:
    for key, value in item.items():
        # print(f'{key}: {value}')
        if '.jpg' in key and 'highlight' not in key:
            print('Field:', key)
            print('Value:', value)
            print('\n')

            # Find out what kind of field this is
            if 'composition' in key:
                composition_llava += value.count('llava')
                composition_cogvlm += value.count('cogvlm')
                composition_deepseek += value.count('deepseek')

            if 'balance' in key:
                balance_llava += value.count('llava')
                balance_cogvlm += value.count('cogvlm')
                balance_deepseek += value.count('deepseek')

            if 'movement' in key:
                movement_llava += value.count('llava')
                movement_cogvlm += value.count('cogvlm')
                movement_deepseek += value.count('deepseek')

            if 'contrast' in key:
                contrast_llava += value.count('llava')
                contrast_cogvlm += value.count('cogvlm')
                contrast_deepseek += value.count('deepseek')

            if 'ground' in key:
                ground_llava += value.count('llava')
                ground_cogvlm += value.count('cogvlm')
                ground_deepseek += value.count('deepseek')

            if 'symmetry' in key:
                symmetry_llava += value.count('llava')
                symmetry_cogvlm += value.count('cogvlm')
                symmetry_deepseek += value.count('deepseek')

            if 'eye' in key:
                eye_llava += value.count('llava')
                eye_cogvlm += value.count('cogvlm')
                eye_deepseek += value.count('deepseek')

            if 'focus' in key:
                focus_llava += value.count('llava')
                focus_cogvlm += value.count('cogvlm')
                focus_deepseek += value.count('deepseek')

            if 'proportion' in key:
                proportion_llava += value.count('llava')
                proportion_cogvlm += value.count('cogvlm')
                proportion_deepseek += value.count('deepseek')

            # Count how many times llava, cogvlm, and deepseek are in the list of values
            llava_wins_image = value.count('llava')
            cogvlm_wins_image = value.count('cogvlm')
            deepseek_wins_image = value.count('deepseek')

            if llava_wins_image + cogvlm_wins_image + deepseek_wins_image == 0:
                print('No votes for this image')
                no_votes += 1
                continue

            with_votes += 1

            # Add the counts to the total
            llava_wins += llava_wins_image
            cogvlm_wins += cogvlm_wins_image
            deepseek_wins += deepseek_wins_image

            print('llava wins:', llava_wins_image)
            print('cogvlm wins:', cogvlm_wins_image)
            print('deepseek wins:', deepseek_wins_image)
            print('\n')

    print('\n')  # Print a new line for better readability between items

# Print the results
print('llava wins:', llava_wins)
print('cogvlm wins:', cogvlm_wins)
print('deepseek wins:', deepseek_wins)

print('No votes:', no_votes)
print('With votes:', with_votes)

print('\n')

# Print the results for each field
print('Composition:')
print('llava wins:', composition_llava)
print('cogvlm wins:', composition_cogvlm)
print('deepseek wins:', composition_deepseek)

print('\n')
print('Balance:')
print('llava wins:', balance_llava)
print('cogvlm wins:', balance_cogvlm)
print('deepseek wins:', balance_deepseek)

print('\n')
print('Movement:')
print('llava wins:', movement_llava)
print('cogvlm wins:', movement_cogvlm)
print('deepseek wins:', movement_deepseek)

print('\n')
print('Contrast:')
print('llava wins:', contrast_llava)
print('cogvlm wins:', contrast_cogvlm)
print('deepseek wins:', contrast_deepseek)

print('\n')
print('Ground:')
print('llava wins:', ground_llava)
print('cogvlm wins:', ground_cogvlm)
print('deepseek wins:', ground_deepseek)

print('\n')
print('Symmetry:')
print('llava wins:', symmetry_llava)
print('cogvlm wins:', symmetry_cogvlm)
print('deepseek wins:', symmetry_deepseek)

print('\n')
print('Eye:')
print('llava wins:', eye_llava)
print('cogvlm wins:', eye_cogvlm)
print('deepseek wins:', eye_deepseek)

print('\n')
print('Focus:')
print('llava wins:', focus_llava)
print('cogvlm wins:', focus_cogvlm)
print('deepseek wins:', focus_deepseek)

print('\n')
print('Proportion:')
print('llava wins:', proportion_llava)
print('cogvlm wins:', proportion_cogvlm)
print('deepseek wins:', proportion_deepseek)


highlight_data = []


# Iterate through each dictionary in the list and print key-value pairs
for item in data:
    for key, value in item.items():
        # print(f'{key}: {value}')
        if '.jpg' in key and 'highlight' in key:
            print('Field:', key)
            print('Value:', value)
            print('\n')

            # Find which model is in the key
            model = ''
            if 'llava' in key:
                model = 'llava'
            elif 'cogvlm' in key:
                model = 'cogvlm'
            elif 'deepseek' in key:
                model = 'deepseek'

            # Find which question is in the key
            question = ''
            # Find out what kind of field this is
            if 'composition' in key:
                question = 'composition'
            elif 'balance' in key:
                question = 'balance_elements'
            elif 'movement' in key:
                question = 'movement'
            elif 'contrast' in key:
                question = 'contrast_elements'
            elif 'foreground_background_4' in key:
                question = 'ground'
            elif 'symmetry' in key:
                question = 'symmetry_asymmetry_1'
            elif 'eye' in key:
                question = 'eye_movement_2'
            elif 'focus' in key:
                question = 'focus_point'
            elif 'proportion' in key:
                question = 'proportion'

            image_filename = key.split(f"{question}_")[-1]

            highlight_data.append({
                'model': model,
                'question': question,
                'image_filename': image_filename,
                'highlight': value
            })

            print('Model:', model)
            print('Question:', question)
            print('Image Filename:', image_filename)
            print('Highlight:', value)

import read_write_json

pinterest_data = read_write_json.read_json('survey_pinterest_data.js')
renaissance_data = read_write_json.read_json('survey_renaissance_data.js')

highlight_data_processed = []
counts = {}

json_data_pinterest = {}
json_data_renaissance = {}

print('Highlight Data')
for item in highlight_data:
    print('Item')

    image_filename = item['image_filename']
    question = item['question']
    model = item['model']
    highlights = item['highlight']

    print('Image Filename:', image_filename)
    print('Question:', question)
    print('Model:', model)
    print('Highlights:', highlights)

    if model == '':
        continue

    story = ''
    data_type = ''

    # print(pinterest_data)
    # print(renaissance_data)

    if image_filename in pinterest_data:
        print('Pinterest item found')
        story = pinterest_data[image_filename][f"{model}_answers"][question]
        data_type = 'pinterest'
    elif image_filename in renaissance_data:
        print('Renaissance item found')
        story = renaissance_data[image_filename][f"{model}_answers"][question]
        data_type = 'renaissance'
    else:
        print(f"Item not found: {image_filename} {model} {question}")
        continue

    # story = data[image_filename][f"{model}_answers"][question]

    hightlight_list = highlights.split('|')

    print('Story:', story)
    print('Highlights:', hightlight_list)
    print('Data Type:', data_type)

    for hightlight in hightlight_list:
        if hightlight in story:
            if hightlight == '':
                continue
            story = story.replace(hightlight, f"<span class='hightlight'>{hightlight}</span>")

    highlight_data_processed.append({
        'data_type': data_type,
        'model': model,
        'question': question,
        'image_filename': image_filename,
        'highlight': story
    })

    if data_type == 'pinterest':
        # Check if the image filename is in the data, if not, add it
        if image_filename not in json_data_pinterest:
            json_data_pinterest[image_filename] = {f"{model}_answers": {}}

        # Check if the model is not yet in the data structure
        if f"{model}_answers" not in json_data_pinterest[image_filename]:
            json_data_pinterest[image_filename][f"{model}_answers"] = {}

        # Check if the question is already answered
        if question in json_data_pinterest[image_filename][f"{model}_answers"]:
            json_data_pinterest[image_filename][f"{model}_answers"][question] = json_data_pinterest[image_filename][f"{model}_answers"][question] + "<br\><br\>" + story
        else:
            # Answer the question and update the data
            json_data_pinterest[image_filename][f"{model}_answers"][question] = story
    elif data_type == 'renaissance':
        # Check if the image filename is in the data, if not, add it
        if image_filename not in json_data_renaissance:
            json_data_renaissance[image_filename] = {f"{model}_answers": {}}

        # Check if the model is not yet in the data structure
        if f"{model}_answers" not in json_data_renaissance[image_filename]:
            json_data_renaissance[image_filename][f"{model}_answers"] = {}

        # Check if the question is already answered
        if question in json_data_renaissance[image_filename][f"{model}_answers"]:
            json_data_renaissance[image_filename][f"{model}_answers"][question] = json_data_renaissance[image_filename][f"{model}_answers"][question] + "<br\><br\>" + story
        else:
            # Answer the question and update the data
            json_data_renaissance[image_filename][f"{model}_answers"][question] = story


    counts[f"{model}_{question}_{image_filename}"] = counts.get(f"{model}_{question}_{image_filename}", 0) + 1

# Save the data to a JSON file
read_write_json.write_json('survey_highlight_data.json', highlight_data_processed)

read_write_json.write_json('survey_pinterest_data_hightlighted.js', json_data_pinterest)
read_write_json.write_json('survey_renaissance_data_hightlighted.js', json_data_renaissance)

# Write all the stories to a text file
with open('survey_highlight_stories.txt', 'w') as file:
    for item in highlight_data_processed:
        file.write(f"Data Type: {item['data_type']}\n")
        file.write(f"Model: {item['model']}\n")
        file.write(f"Question: {item['question']}\n")
        file.write(f"Image Filename: {item['image_filename']}\n")
        file.write(f"Highlight: {item['highlight']}\n")

ones = 0
twos = 0
threes = 0
fours = 0

for count in counts:
    if counts[count] == 1:
        ones += 1
    elif counts[count] == 2:
        twos += 1
    elif counts[count] == 3:
        threes += 1
    elif counts[count] == 4:
        fours += 1

print('Counts')
print('Ones:', ones)
print('Twos:', twos)
print('Threes:', threes)
print('Fours:', fours)
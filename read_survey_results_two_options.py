import json
import pandas as pd

# Path to the JSON file
file_path = 'export_1720445297387.json'

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

import read_write_json

pinterest_data = read_write_json.read_json('survey_pinterest_data.js')
renaissance_data = read_write_json.read_json('survey_renaissance_data.js')

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

two_options_data = []

# Iterate through each dictionary in the list and print key-value pairs
for item in data:
    for key, value in item.items():
        # print(f'{key}: {value}')
        if '.jpg' in key and 'highlight' not in key:

            print('Field:', key)
            print('Value:', value)
            print('\n')

            question = ''
            # Find out what kind of field this is
            if 'composition' in key:
                question = 'composition'
            elif 'balance_elements' in key:
                question = 'balance_elements'
            elif 'eye_movement_2' in key:
                question = 'eye_movement_2'
            elif 'movement' in key:
                question = 'movement'
            elif 'contrast_elements' in key:
                question = 'contrast_elements'
            elif 'foreground_background_4' in key:
                question = 'foreground_background_4'
            elif 'symmetry_asymmetry_1' in key:
                question = 'symmetry_asymmetry_1'
            elif 'focus_point' in key:
                question = 'focus_point'
            elif 'proportion' in key:
                question = 'proportion'

                
            key = key.replace(f"{question}_", '')

            match_contestants = []
            if 'llava' in key:
                key = key.replace('llava_', '')
                match_contestants.append('llava')
            if 'cogvlm' in key:
                key = key.replace('cogvlm_', '')
                match_contestants.append('cogvlm')
            if 'deepseek' in key:
                key = key.replace('deepseek_', '')
                match_contestants.append('deepseek')

            if key in pinterest_data:
                print('Pinterest item found: ', key)
                data_type = 'pinterest'
            elif key in renaissance_data:
                print('Renaissance item found: ', key)
                data_type = 'renaissance'
            else:
                print(f'Item not found: {key}')
                continue

            # Find out what kind of field this is
            if question == 'composition':
                composition_llava += value.count('llava')
                composition_cogvlm += value.count('cogvlm')
                composition_deepseek += value.count('deepseek')

            if question == 'balance_elements':
                balance_llava += value.count('llava')
                balance_cogvlm += value.count('cogvlm')
                balance_deepseek += value.count('deepseek')

            if question == 'movement':
                movement_llava += value.count('llava')
                movement_cogvlm += value.count('cogvlm')
                movement_deepseek += value.count('deepseek')

            if question == 'contrast_elements':
                contrast_llava += value.count('llava')
                contrast_cogvlm += value.count('cogvlm')
                contrast_deepseek += value.count('deepseek')

            if question == 'foreground_background_4':
                ground_llava += value.count('llava')
                ground_cogvlm += value.count('cogvlm')
                ground_deepseek += value.count('deepseek')

            if question == 'symmetry_asymmetry_1':
                symmetry_llava += value.count('llava')
                symmetry_cogvlm += value.count('cogvlm')
                symmetry_deepseek += value.count('deepseek')

            if question == 'eye_movement_2':
                eye_llava += value.count('llava')
                eye_cogvlm += value.count('cogvlm')
                eye_deepseek += value.count('deepseek')

            if question == 'focus_point':
                focus_llava += value.count('llava')
                focus_cogvlm += value.count('cogvlm')
                focus_deepseek += value.count('deepseek')

            if  question == 'proportion':
                proportion_llava += value.count('llava')
                proportion_cogvlm += value.count('cogvlm')
                proportion_deepseek += value.count('deepseek')

            # Count how many times llava, cogvlm, and deepseek are in the list of values
            llava_wins_image = value.count('llava')
            cogvlm_wins_image = value.count('cogvlm')
            deepseek_wins_image = value.count('deepseek')

            two_options_data.append({
                'image_filename': key,
                'question': question,
                'model': value,
                'contestant_1': match_contestants[0] if len(match_contestants) > 0 else '',
                'contestant_2': match_contestants[1] if len(match_contestants) > 1 else '',
                'data_type': data_type
            })

            if llava_wins_image + cogvlm_wins_image + deepseek_wins_image == 0:
                print('No votes for this image')
                no_votes += 1
                continue

            with_votes += 1

            # Add the counts to the total
            llava_wins += llava_wins_image
            cogvlm_wins += cogvlm_wins_image
            deepseek_wins += deepseek_wins_image

            # print('llava wins:', llava_wins_image)
            # print('cogvlm wins:', cogvlm_wins_image)
            # print('deepseek wins:', deepseek_wins_image)
            # print('\n')



            # two_options_data.append({
            #     'image_filename': key,
            #     'question': question,
            #     'model': 'llava',
            #     'highlight': value,
            #     'score': llava_wins_image
            # })

            # two_options_data.append({
            #     'image_filename': key,
            #     'question': question,
            #     'model': 'cogvlm',
            #     'highlight': value,
            #     'score': cogvlm_wins_image
            # })

            # two_options_data.append({
            #     'image_filename': key,
            #     'question': question,
            #     'model': 'deepseek',
            #     'highlight': value,
            #     'score': deepseek_wins_image
            # })

    print('\n')  # Print a new line for better readability between items

# # Print the results
# print('llava wins:', llava_wins)
# print('cogvlm wins:', cogvlm_wins)
# print('deepseek wins:', deepseek_wins)

# print('No votes:', no_votes)
# print('With votes:', with_votes)

# print('\n')

# # Print the results for each field
# print('Composition:')
# print('llava wins:', composition_llava)
# print('cogvlm wins:', composition_cogvlm)
# print('deepseek wins:', composition_deepseek)

# print('\n')
# print('Balance:')
# print('llava wins:', balance_llava)
# print('cogvlm wins:', balance_cogvlm)
# print('deepseek wins:', balance_deepseek)

# print('\n')
# print('Movement:')
# print('llava wins:', movement_llava)
# print('cogvlm wins:', movement_cogvlm)
# print('deepseek wins:', movement_deepseek)

# print('\n')
# print('Contrast:')
# print('llava wins:', contrast_llava)
# print('cogvlm wins:', contrast_cogvlm)
# print('deepseek wins:', contrast_deepseek)

# print('\n')
# print('Ground:')
# print('llava wins:', ground_llava)
# print('cogvlm wins:', ground_cogvlm)
# print('deepseek wins:', ground_deepseek)

# print('\n')
# print('Symmetry:')
# print('llava wins:', symmetry_llava)
# print('cogvlm wins:', symmetry_cogvlm)
# print('deepseek wins:', symmetry_deepseek)

# print('\n')
# print('Eye:')
# print('llava wins:', eye_llava)
# print('cogvlm wins:', eye_cogvlm)
# print('deepseek wins:', eye_deepseek)

# print('\n')
# print('Focus:')
# print('llava wins:', focus_llava)
# print('cogvlm wins:', focus_cogvlm)
# print('deepseek wins:', focus_deepseek)

# print('\n')
# print('Proportion:')
# print('llava wins:', proportion_llava)
# print('cogvlm wins:', proportion_cogvlm)
# print('deepseek wins:', proportion_deepseek)

# Create csv file
csv = "image_filename;question;model;contestant_1;contestant_2;data_type\n"
for item in two_options_data:
    csv += f"{item['image_filename']};{item['question']};{item['model']};{item['contestant_1']};{item['contestant_2']};{item['data_type']}\n"

# with open('survey_two_options_csv.csv', 'w') as file:
#     file.write(csv)

# import read_write_json

# pinterest_data = read_write_json.read_json('survey_pinterest_data.js')
# renaissance_data = read_write_json.read_json('survey_renaissance_data.js')

# two_options_data_processed = []
# counts = {}

# json_data_pinterest = {}
# json_data_renaissance = {}

# # print('Two Options Data')
# for item in two_options_data:
#     # print('Item')

#     image_filename = item['image_filename']
#     question = item['question']
#     model = item['model']
#     highlights = item['highlight']
#     score = item['score']

#     # print('Image Filename:', image_filename)
#     # print('Question:', question)
#     # print('Model:', model)
#     # print('Highlights:', highlights)
#     # print('Score:', score)

#     if model == '':
#         continue

#     story = ''
#     data_type = ''

#     # print(pinterest_data)
#     # print(renaissance_data)

#     if image_filename in pinterest_data:
#         # print('Pinterest item found')
#         story = pinterest_data[image_filename][f"{model}_answers"][question]
#         data_type = 'pinterest'
#     elif image_filename in renaissance_data:
#         # print('Renaissance item found')
#         story = renaissance_data[image_filename][f"{model}_answers"][question]
#         data_type = 'renaissance'
#     else:
#         # print(f"Item not found: {image_filename} {model} {question}")
#         continue

#     # story = data[image_filename][f"{model}_answers"][question]

#     hightlight_list = highlights.split('|')

#     # print('Story:', story)
#     # print('Highlights:', hightlight_list)
#     # print('Data Type:', data_type)

#     if (score == 1):
#         story = f'<<voted>>' + story

#     two_options_data_processed.append({
#         'data_type': data_type,
#         'model': model,
#         'question': question,
#         'image_filename': image_filename,
#         'highlight': story
#     })

#     if data_type == 'pinterest':
#         # Check if the image filename is in the data, if not, add it
#         if image_filename not in json_data_pinterest:
#             json_data_pinterest[image_filename] = {f"{model}_answers": {}}

#         # Check if the model is not yet in the data structure
#         if f"{model}_answers" not in json_data_pinterest[image_filename]:
#             json_data_pinterest[image_filename][f"{model}_answers"] = {}

#         # Check if the question is already answered
#         if question in json_data_pinterest[image_filename][f"{model}_answers"]:
#             json_data_pinterest[image_filename][f"{model}_answers"][question] = json_data_pinterest[image_filename][f"{model}_answers"][question] + "<br\><br\>" + story
#         else:
#             # Answer the question and update the data
#             json_data_pinterest[image_filename][f"{model}_answers"][question] = story
#     elif data_type == 'renaissance':
#         # Check if the image filename is in the data, if not, add it
#         if image_filename not in json_data_renaissance:
#             json_data_renaissance[image_filename] = {f"{model}_answers": {}}

#         # Check if the model is not yet in the data structure
#         if f"{model}_answers" not in json_data_renaissance[image_filename]:
#             json_data_renaissance[image_filename][f"{model}_answers"] = {}

#         # Check if the question is already answered
#         if question in json_data_renaissance[image_filename][f"{model}_answers"]:
#             json_data_renaissance[image_filename][f"{model}_answers"][question] = json_data_renaissance[image_filename][f"{model}_answers"][question] + "<br\><br\>" + story
#         else:
#             # Answer the question and update the data
#             json_data_renaissance[image_filename][f"{model}_answers"][question] = story


#     counts[f"{model}_{question}_{image_filename}"] = counts.get(f"{model}_{question}_{image_filename}", 0) + 1

# # Save the data to a JSON file
# read_write_json.write_json('survey_two_options_data_updated.json', two_options_data_processed)

# read_write_json.write_json('survey_pinterest_data_two_options_updates.js', json_data_pinterest)
# read_write_json.write_json('survey_renaissance_data_two_options_updated.js', json_data_renaissance)

# # Write all the stories to a text file
# with open('survey_two_options_stories_updated.txt', 'w') as file:
#     for item in two_options_data_processed:
#         file.write(f"Data Type: {item['data_type']}\n")
#         file.write(f"Model: {item['model']}\n")
#         file.write(f"Question: {item['question']}\n")
#         file.write(f"Image Filename: {item['image_filename']}\n")
#         file.write(f"Highlight: {item['highlight']}\n")

# ones = 0
# twos = 0
# threes = 0
# fours = 0

# for count in counts:
#     if counts[count] == 1:
#         ones += 1
#     elif counts[count] == 2:
#         twos += 1
#     elif counts[count] == 3:
#         threes += 1
#     elif counts[count] == 4:
#         fours += 1

# print('Counts')
# print('Ones:', ones)
# print('Twos:', twos)
# print('Threes:', threes)
# print('Fours:', fours)

from trueskill import Rating, quality_1vs1, rate_1vs1

# Give all the models a default rating
llava = Rating()
cogvlm = Rating()
deepseek = Rating()

csv = "llava;cogvlm;deepseek\n"

for item in two_options_data:
    if item['contestant_1'] != '' and item['contestant_2'] != '' and item['model'] != '':
        csv += f"{llava};{cogvlm};{deepseek}\n"

        concat = item['contestant_1'] + item['contestant_2']
        winner = item['model']
        loser = concat.replace(winner, '')

        if winner == 'llava':
            winner_ts = llava
        elif winner == 'cogvlm':
            winner_ts = cogvlm
        elif winner == 'deepseek':
            winner_ts = deepseek

        if loser == 'llava':
            loser_ts = llava
        elif loser == 'cogvlm':
            loser_ts = cogvlm
        elif loser == 'deepseek':
            loser_ts = deepseek

        winner_ts, loser_ts = rate_1vs1(winner_ts, loser_ts)

        if winner == 'llava':
            llava = winner_ts
        elif winner == 'cogvlm':
            cogvlm = winner_ts
        elif winner == 'deepseek':
            deepseek = winner_ts

        if loser == 'llava':
            llava = loser_ts
        elif loser == 'cogvlm':
            cogvlm = loser_ts
        elif loser == 'deepseek':
            deepseek = loser_ts

# csv += "\n\n\n"
# csv += f"quality_llava_cogvlm: {quality_1vs1(llava, cogvlm)}\n"
# csv += f"quality_llava_deepseek: {quality_1vs1(llava, deepseek)}\n"
# csv += f"quality_cogvlm_deepseek: {quality_1vs1(cogvlm, deepseek)}\n"
# csv += f"quality_cogvlm_llava: {quality_1vs1(cogvlm, llava)}\n"
# csv += f"quality_deepseek_llava: {quality_1vs1(deepseek, llava)}\n"
# csv += f"quality_deepseek_cogvlm: {quality_1vs1(deepseek, cogvlm)}\n"

csv += "\n\n\n"
csv += '{:.1%} chance to draw between llava and cogvlm'.format(quality_1vs1(llava, cogvlm))
csv += '{:.1%} chance to draw between llava and deepseek'.format(quality_1vs1(llava, deepseek))
csv += '{:.1%} chance to draw between cogvlm and deepseek'.format(quality_1vs1(cogvlm, deepseek))


import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the three Gaussians

# Generate x-values
x = np.linspace(17.5, 32.5, 1000)

# Function to compute the Gaussian distribution
def gaussian(x, mean, variance):
    return (1 / np.sqrt(2 * np.pi * variance)) * np.exp(-(x - mean) ** 2 / (2 * variance))

# Generate y-values for each Gaussian
y1 = gaussian(x, llava.mu, llava.sigma)
y2 = gaussian(x, cogvlm.mu, cogvlm.sigma)
y3 = gaussian(x, deepseek.mu, deepseek.sigma)

# Plot the Gaussians
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label=f'LLaVA')
plt.plot(x, y2, label=f'CogVLM')
plt.plot(x, y3, label=f'Deepseek')

# Add titles and labels
plt.title('Gaussian Distributions')
plt.xlabel('TrueSkill Rating')
plt.ylabel('Probability Density')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

# Save image to file
plt.savefig('gaussian_distributions.png')



# Write the ratings to a csv file
# with open('survey_two_options_ratings.csv', 'w') as file:
#     file.write(csv)
        
        
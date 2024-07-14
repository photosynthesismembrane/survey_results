import json
import pandas as pd
import time

# Path to the JSON file
file_path = 'export_1720445297387_refined.json'
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

            if len(match_contestants) == 2:
                two_options_data.append({
                    'image_filename': key,
                    'question': question,
                    'model': value,
                    'contestant_1': match_contestants[0],
                    'contestant_2': match_contestants[1],
                    'data_type': data_type
                })
            else:
                two_options_data.append({
                    'image_filename': key,
                    'question': question,
                    'model': value,
                    'contestant_1': '',
                    'contestant_2': '',
                    'data_type': data_type
                })


from trueskill import Rating, quality_1vs1, rate_1vs1
import plot_gaussians

def create_table_entry(data, task, set):
    llava_wins = 0
    cogvlm_wins = 0
    deepseek_wins = 0

    llava_loses = 0
    cogvlm_loses = 0
    deepseek_loses = 0

    llava_rating = Rating()
    cogvlm_rating = Rating()
    deepseek_rating = Rating()

    llava_rating_list = []
    cogvlm_rating_list = []
    deepseek_rating_list = []

    for item in data:
        if set == 'all' or item['data_type'] == set:
            if item['question'] == task or task == 'all':
                if item['model'] == 'llava':
                    llava_wins += 1
                    winner_rating = llava_rating
                elif item['model'] == 'cogvlm':
                    cogvlm_wins += 1
                    winner_rating = cogvlm_rating
                elif item['model'] == 'deepseek':
                    deepseek_wins += 1
                    winner_rating = deepseek_rating

                loser = (item['contestant_1'] + item['contestant_2']).replace(item['model'], '')

                if loser == 'llava':
                    winner_rating, llava_rating = rate_1vs1(winner_rating, llava_rating)
                    llava_loses += 1
                    llava_rating_list.append(llava_rating.mu)
                elif loser == 'cogvlm':
                    winner_rating, cogvlm_rating = rate_1vs1(winner_rating, cogvlm_rating)
                    cogvlm_loses += 1
                    cogvlm_rating_list.append(cogvlm_rating.mu)
                elif loser == 'deepseek':
                    winner_rating, deepseek_rating = rate_1vs1(winner_rating, deepseek_rating)
                    deepseek_loses += 1
                    deepseek_rating_list.append(deepseek_rating.mu)

                if item['model'] == 'llava':
                    llava_rating = winner_rating
                    llava_rating_list.append(llava_rating.mu)
                elif item['model'] == 'cogvlm':
                    cogvlm_rating = winner_rating
                    cogvlm_rating_list.append(cogvlm_rating.mu)
                elif item['model'] == 'deepseek':
                    deepseek_rating = winner_rating
                    deepseek_rating_list.append(deepseek_rating.mu)

    plot_gaussians.plot_gaussians({
        'llava': llava_rating_list,
        'cogvlm': cogvlm_rating_list,
        'deepseek': deepseek_rating_list
    }, f'{set.capitalize()} {task} Ratings', 'Rating', 'Density', f'{set}_{task}_ratings')

    return f"<tr><td>{task}</td><td>{llava_wins}/{llava_wins+llava_loses}</td><td>{cogvlm_wins}/{cogvlm_wins+cogvlm_loses}</td><td>{deepseek_wins}/{deepseek_wins+deepseek_loses}</td><td>{llava_rating.mu:.2f}</td><td>{llava_rating.sigma:.2f}</td><td>{cogvlm_rating.mu:.2f}</td><td>{cogvlm_rating.sigma:.2f}</td><td>{deepseek_rating.mu:.2f}</td><td>{deepseek_rating.sigma:.2f}</td></tr>"


sets = ['all', 'pinterest', 'renaissance']
tasks = ['all', 'composition', 'balance_elements', 'eye_movement_2', 'movement', 'contrast_elements', 'foreground_background_4', 'symmetry_asymmetry_1', 'focus_point', 'proportion']

html = """
    <div class="survey-score-container">
"""	

for set in sets:
    html += f"""
    <div class="survey-comparison-data-container">
        <table>
            <caption>{set.capitalize()} Ratings</caption>
            <thead>
                <tr>
                    <th>Task</th>
                    <th>llava Wins</th>
                    <th>cogvlm Wins</th>
                    <th>deepseek Wins</th>
                    <th>llava Mean</th>
                    <th>llava Sigma</th>
                    <th>cogvlm Mean</th>
                    <th>cogvlm Sigma</th>
                    <th>deepseek Mean</th>
                    <th>deepseek Sigma</th>
                </tr>
            </thead>
            <tbody>
    """
    for task in tasks:
        html += create_table_entry(two_options_data, task, set)
    
    html += "</tbody></table>"

    html += f""""
            <div class="main-plot-container">
                <img src="{set}_all_ratings.png" alt="{set} all ratings">
            </div>
        </div>
        <div class="sub-plot-container">
            <img src="{set}_composition_ratings.png" alt="{set} composition ratings">
            <img src="{set}_balance_elements_ratings.png" alt="{set} balance elements ratings">
            <img src="{set}_eye_movement_2_ratings.png" alt="{set} eye movement 2 ratings">
            <img src="{set}_movement_ratings.png" alt="{set} movement ratings">
            <img src="{set}_contrast_elements_ratings.png" alt="{set} contrast elements ratings">
            <img src="{set}_foreground_background_4_ratings.png" alt="{set} foreground background 4 ratings">
            <img src="{set}_symmetry_asymmetry_1_ratings.png" alt="{set} symmetry asymmetry 1 ratings">
            <img src="{set}_focus_point_ratings.png" alt="{set} focus point ratings">
            <img src="{set}_proportion_ratings.png" alt="{set} proportion ratings">
        </div>
    </div>
    """

html += "</div>"

with open(f'ratings.html', 'w') as file:
    file.write(html)
        


import read_write_json

pinterest_data = read_write_json.read_json('survey_pinterest_data.js')
renaissance_data = read_write_json.read_json('survey_renaissance_data.js')

two_options_data_processed = []

json_data_pinterest = {}
json_data_renaissance = {}

# print('Two Options Data')
for index, item in enumerate(two_options_data):
    # print('Item')

    image_filename = f"{item['image_filename']}{index}"
    question = item['question']
    winner = item['model']
    loser = (item['contestant_1'] + item['contestant_2']).replace(winner, '')
    other = ''

    if winner == '':
        continue

    story_winner = ''
    story_loser = ''
    story_other = ''
    data_type = ''

    if item['image_filename'] in pinterest_data:
        story_winner = "<<voted>>" + pinterest_data[item['image_filename']][f"{winner}_answers"][question]
        if loser != '':
            story_loser = pinterest_data[item['image_filename']][f"{loser}_answers"][question]
        else:
            loser = [contestant for contestant in ['llava', 'cogvlm', 'deepseek'] if contestant not in [winner]][0]
            other = [contestant for contestant in ['llava', 'cogvlm', 'deepseek'] if contestant not in [winner, loser]][0]
            story_loser = pinterest_data[item['image_filename']][f"{loser}_answers"][question]
            story_other = pinterest_data[item['image_filename']][f"{other}_answers"][question]
        data_type = 'pinterest'
        print(f"Winner {winner} Loser {loser} Other {other}")
    elif item['image_filename'] in renaissance_data:
        story_winner = "<<voted>>" + renaissance_data[item['image_filename']][f"{winner}_answers"][question]
        if loser != '':
            story_loser = renaissance_data[item['image_filename']][f"{loser}_answers"][question]
        else:
            loser = [contestant for contestant in ['llava', 'cogvlm', 'deepseek'] if contestant not in [winner]][0]
            other = [contestant for contestant in ['llava', 'cogvlm', 'deepseek'] if contestant not in [winner, loser]][0]
            story_loser = renaissance_data[item['image_filename']][f"{loser}_answers"][question]
            story_other = renaissance_data[item['image_filename']][f"{other}_answers"][question]
        data_type = 'renaissance'
        print(f"Winner {winner} Loser {loser} Other {other}")
    else:
        continue

    if data_type == 'pinterest':
        # Check if the image filename is in the data, if not, add it
        if image_filename not in json_data_pinterest:
            json_data_pinterest[image_filename] = {f"{winner}_answers": {}}

        # Check if the model is not yet in the data structure
        if f"{winner}_answers" not in json_data_pinterest[image_filename]:
            json_data_pinterest[image_filename][f"{winner}_answers"] = {}

        # Answer the question and update the data
        json_data_pinterest[image_filename][f"{winner}_answers"][question] = story_winner

        # Check if the image filename is in the data, if not, add it
        if image_filename not in json_data_pinterest:
            json_data_pinterest[image_filename] = {f"{loser}_answers": {}}

        # Check if the model is not yet in the data structure
        if f"{loser}_answers" not in json_data_pinterest[image_filename]:
            json_data_pinterest[image_filename][f"{loser}_answers"] = {}

        # Answer the question and update the data
        json_data_pinterest[image_filename][f"{loser}_answers"][question] = story_loser

        if other != '':
            # Check if the image filename is in the data, if not, add it
            if image_filename not in json_data_pinterest:
                json_data_pinterest[image_filename] = {f"{other}_answers": {}}

            # Check if the model is not yet in the data structure
            if f"{other}_answers" not in json_data_pinterest[image_filename]:
                json_data_pinterest[image_filename][f"{other}_answers"] = {}

            # Answer the question and update the data
            json_data_pinterest[image_filename][f"{other}_answers"][question] = story_other


    elif data_type == 'renaissance':
        # Check if the image filename is in the data, if not, add it
        if image_filename not in json_data_renaissance:
            json_data_renaissance[image_filename] = {f"{winner}_answers": {}}

        # Check if the model is not yet in the data structure
        if f"{winner}_answers" not in json_data_renaissance[image_filename]:
            json_data_renaissance[image_filename][f"{winner}_answers"] = {}

        # Answer the question and update the data
        json_data_renaissance[image_filename][f"{winner}_answers"][question] = story_winner

        # Check if the image filename is in the data, if not, add it
        if image_filename not in json_data_renaissance:
            json_data_renaissance[image_filename] = {f"{loser}_answers": {}}

        # Check if the model is not yet in the data structure
        if f"{loser}_answers" not in json_data_renaissance[image_filename]:
            json_data_renaissance[image_filename][f"{loser}_answers"] = {}

        # Answer the question and update the data
        json_data_renaissance[image_filename][f"{loser}_answers"][question] = story_loser

        if other != '':
            # Check if the image filename is in the data, if not, add it
            if image_filename not in json_data_renaissance:
                json_data_renaissance[image_filename] = {f"{other}_answers": {}}

            # Check if the model is not yet in the data structure
            if f"{other}_answers" not in json_data_renaissance[image_filename]:
                json_data_renaissance[image_filename][f"{other}_answers"] = {}

            # Answer the question and update the data
            json_data_renaissance[image_filename][f"{other}_answers"][question] = story_other


read_write_json.write_json('survey_pinterest_data_two_options_updates_v2.js', json_data_pinterest)
read_write_json.write_json('survey_renaissance_data_two_options_updated_v2.js', json_data_renaissance)

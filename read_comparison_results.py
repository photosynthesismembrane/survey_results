import json
import read_write_json
from trueskill import Rating, rate_1vs1
import plot_gaussians

def create_comparison_data():
    # Path to the JSON file
    file_path = 'export_1721421209861_refined.json'

    pinterest_data = read_write_json.read_json('survey_pinterest_data.js')
    renaissance_data = read_write_json.read_json('survey_renaissance_data.js')

    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    two_options_data = []

    # Iterate participants
    for item in data:
        # Iterate fields
        for key, value in item.items():
            # Only process side-by-side comparison fields
            if '.jpg' in key and 'highlight' not in key:

                # What topic is the narrative about
                question = ''
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

                # Field name: <question>_<vlm_name>_<vlm_name>_<image_filename>
                key = key.replace(f"{question}_", '')

                # Contestants
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

                # Imageset
                if key in pinterest_data:
                    data_type = 'pinterest'
                elif key in renaissance_data:
                    data_type = 'renaissance'
                else:
                    continue

                # Early versions of the survey did not submit two contestants
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

    read_write_json.write_json('two_options_data.js', two_options_data)

    return two_options_data

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
                loser = (item['contestant_1'] + item['contestant_2']).replace(item['model'], '')

                if loser == '':
                    continue

                if item['model'] == 'llava':
                    llava_wins += 1
                    winner_rating = llava_rating
                elif item['model'] == 'cogvlm':
                    cogvlm_wins += 1
                    winner_rating = cogvlm_rating
                elif item['model'] == 'deepseek':
                    deepseek_wins += 1
                    winner_rating = deepseek_rating

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
    }, f"{task.split('_')[0].capitalize()}", 'Rating', 'Density', f'plots\\{set}_{task}_ratings')

    return f"<tr><td>{task.split('_')[0]}</td><td>{llava_wins} / {llava_wins+llava_loses}</td><td>{cogvlm_wins} / {cogvlm_wins+cogvlm_loses}</td><td>{deepseek_wins} / {deepseek_wins+deepseek_loses}</td><td>{llava_rating.mu:.2f} &pm; {llava_rating.sigma:.2f}</td><td>{cogvlm_rating.mu:.2f} &pm; {cogvlm_rating.sigma:.2f}</td><td>{deepseek_rating.mu:.2f} &pm; {deepseek_rating.sigma:.2f}</td></tr>"

def create_combined_sets_plot(data, task, model):
    sets = ['pinterest', 'renaissance']

    data_dict = {}
    for set in sets:

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
            if item['data_type'] == set:
                if item['question'] == task or task == 'all':
                    loser = (item['contestant_1'] + item['contestant_2']).replace(item['model'], '')

                    if loser == '':
                        continue

                    if item['model'] == 'llava':
                        llava_wins += 1
                        winner_rating = llava_rating
                    elif item['model'] == 'cogvlm':
                        cogvlm_wins += 1
                        winner_rating = cogvlm_rating
                    elif item['model'] == 'deepseek':
                        deepseek_wins += 1
                        winner_rating = deepseek_rating

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

        rating_list = []
        if model == 'llava':
            rating_list = llava_rating_list
        elif model == 'cogvlm':
            rating_list = cogvlm_rating_list
        elif model == 'deepseek':
            rating_list = deepseek_rating_list

        if set == 'pinterest':
            data_dict['pinterest'] = rating_list
        elif set == 'renaissance':
            data_dict['renaissance'] = rating_list

    plot_gaussians.plot_gaussians(data_dict, f"{model.capitalize()} {task.split('_')[0].capitalize()}", 'Rating', 'Density', f'plots\\combined_sets_{model}_{task}_ratings')

def create_plots_and_html(two_options_data):
    sets = ['all', 'pinterest', 'renaissance']
    tasks = ['all', 'composition', 'balance_elements', 'eye_movement_2', 'movement', 'contrast_elements', 'foreground_background_4', 'symmetry_asymmetry_1', 'focus_point', 'proportion']

    html = """
        <div class="sub-tabs">
            <button class="sub-tab-button active" onclick="openSubTab('sub-tab1')">All</button>
            <button class="sub-tab-button" onclick="openSubTab('sub-tab2')">Pinterest</button>
            <button class="sub-tab-button" onclick="openSubTab('sub-tab3')">Renaissance</button>
            <button class="sub-tab-button" onclick="openSubTab('sub-tab4')">Sets</button>
            <div class="horizontal-fill-sub-tab-buttons"></div>
        </div>
    """	

    for index, set in enumerate(sets):
        tab_open = 'block' if index == 0 else 'none'
        html += f"""
        <div id="sub-tab{index+1}" class="sub-tab-content" style="display: {tab_open};">
        <div class="survey-comparison-data-container">
            <table>
                <thead>
                    <tr>
                        <th>Task</th>
                        <th>Llava wins</th>
                        <th>Cogvlm wins</th>
                        <th>Deepseek wins</th>
                        <th>Llava rating</th>
                        <th>Cogvlm rating</th>
                        <th>Deepseek rating</th>
                    </tr>
                </thead>
                <tbody>
        """
        for task in tasks:
            html += create_table_entry(two_options_data, task, set)
        
        html += "</tbody></table>"

        html += f""""
                <div class="main-plot-container">
                    <img src="plots/{set}_all_ratings.png" alt="{set} all ratings">
                </div>
            </div>
            <div class="sub-plot-container">
                <img src="plots/{set}_composition_ratings.png" alt="{set} composition ratings">
                <img src="plots/{set}_balance_elements_ratings.png" alt="{set} balance elements ratings">
                <img src="plots/{set}_eye_movement_2_ratings.png" alt="{set} eye movement 2 ratings">
                <img src="plots/{set}_movement_ratings.png" alt="{set} movement ratings">
                <img src="plots/{set}_contrast_elements_ratings.png" alt="{set} contrast elements ratings">
                <img src="plots/{set}_foreground_background_4_ratings.png" alt="{set} foreground background 4 ratings">
                <img src="plots/{set}_symmetry_asymmetry_1_ratings.png" alt="{set} symmetry asymmetry 1 ratings">
                <img src="plots/{set}_focus_point_ratings.png" alt="{set} focus point ratings">
                <img src="plots/{set}_proportion_ratings.png" alt="{set} proportion ratings">
            </div>
        </div>
        """

    for model in ['llava', 'cogvlm', 'deepseek']:
        for task in tasks:
            create_combined_sets_plot(two_options_data, task, model)

    html += f"""
        <div id="sub-tab4" class="sub-tab-content">
            <div class="sub-plot-container">
                <img src="plots/combined_sets_llava_all_ratings.png" alt="combined sets llava all ratings">
                <img src="plots/combined_sets_cogvlm_all_ratings.png" alt="combined sets cogvlm all ratings">
                <img src="plots/combined_sets_deepseek_all_ratings.png" alt="combined sets deepseek all ratings">
                <img src="plots/combined_sets_llava_composition_ratings.png" alt="combined sets llava composition ratings">
                <img src="plots/combined_sets_cogvlm_composition_ratings.png" alt="combined sets cogvlm composition ratings">
                <img src="plots/combined_sets_deepseek_composition_ratings.png" alt="combined sets deepseek composition ratings">
                <img src="plots/combined_sets_llava_balance_elements_ratings.png" alt="combined sets llava balance elements ratings">
                <img src="plots/combined_sets_cogvlm_balance_elements_ratings.png" alt="combined sets cogvlm balance elements ratings">
                <img src="plots/combined_sets_deepseek_balance_elements_ratings.png" alt="combined sets deepseek balance elements ratings">
                <img src="plots/combined_sets_llava_eye_movement_2_ratings.png" alt="combined sets llava eye movement 2 ratings">
                <img src="plots/combined_sets_cogvlm_eye_movement_2_ratings.png" alt="combined sets cogvlm eye movement 2 ratings">
                <img src="plots/combined_sets_deepseek_eye_movement_2_ratings.png" alt="combined sets deepseek eye movement 2 ratings">
                <img src="plots/combined_sets_llava_movement_ratings.png" alt="combined sets llava movement ratings">
                <img src="plots/combined_sets_cogvlm_movement_ratings.png" alt="combined sets cogvlm movement ratings">
                <img src="plots/combined_sets_deepseek_movement_ratings.png" alt="combined sets deepseek movement ratings">
                <img src="plots/combined_sets_llava_contrast_elements_ratings.png" alt="combined sets llava contrast elements ratings">
                <img src="plots/combined_sets_cogvlm_contrast_elements_ratings.png" alt="combined sets cogvlm contrast elements ratings">
                <img src="plots/combined_sets_deepseek_contrast_elements_ratings.png" alt="combined sets deepseek contrast elements ratings">
                <img src="plots/combined_sets_llava_foreground_background_4_ratings.png" alt="combined sets llava foreground background 4 ratings">
                <img src="plots/combined_sets_cogvlm_foreground_background_4_ratings.png" alt="combined sets cogvlm foreground background 4 ratings">
                <img src="plots/combined_sets_deepseek_foreground_background_4_ratings.png" alt="combined sets deepseek foreground background 4 ratings">
                <img src="plots/combined_sets_llava_symmetry_asymmetry_1_ratings.png" alt="combined sets llava symmetry asymmetry 1 ratings">
                <img src="plots/combined_sets_cogvlm_symmetry_asymmetry_1_ratings.png" alt="combined sets cogvlm symmetry asymmetry 1 ratings">
                <img src="plots/combined_sets_deepseek_symmetry_asymmetry_1_ratings.png" alt="combined sets deepseek symmetry asymmetry 1 ratings">
                <img src="plots/combined_sets_llava_focus_point_ratings.png" alt="combined sets llava focus point ratings">
                <img src="plots/combined_sets_cogvlm_focus_point_ratings.png" alt="combined sets cogvlm focus point ratings">
                <img src="plots/combined_sets_deepseek_focus_point_ratings.png" alt="combined sets deepseek focus point ratings">
                <img src="plots/combined_sets_llava_proportion_ratings.png" alt="combined sets llava proportion ratings">
                <img src="plots/combined_sets_cogvlm_proportion_ratings.png" alt="combined sets cogvlm proportion ratings">
                <img src="plots/combined_sets_deepseek_proportion_ratings.png" alt="combined sets deepseek proportion ratings">
            </div>
        </div>
    """

    with open(f'ratings.html', 'w') as file:
        file.write(html)

    return html
        
def create_js_variable(two_options_data):
    pinterest_data = read_write_json.read_json('survey_pinterest_data.js')
    renaissance_data = read_write_json.read_json('survey_renaissance_data.js')

    json_data_pinterest = {}
    json_data_renaissance = {}

    for index, item in enumerate(two_options_data):

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

    read_write_json.write_json('pinterest_data_comparison.js', json_data_pinterest, 'pinterest_data_comparison')
    read_write_json.write_json('renaissance_data_comparison.js', json_data_renaissance, 'renaissance_data_comparison')

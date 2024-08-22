import json
import read_write_json

def get_highlight_data():
    # Narratives created by the VLM's for the Pinterest and Renaissance images
    pinterest_data = read_write_json.read_json('survey_pinterest_data.js')
    renaissance_data = read_write_json.read_json('survey_renaissance_data.js')

    # Path to the JSON file
    file_path = 'export_1721421209861_refined.json'

    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    highlight_data = []
    highlight_data_processed = []
    counts = {}
    json_data_pinterest = {}
    json_data_renaissance = {}
    json_all_data = {}

    # Iterate each participant
    for item in data:
        # Iterate each field
        for key, value in item.items():
            # Only process highlight fields
            if '.jpg' in key and 'highlight' in key:

                # Which VLM created the narrative
                model = ''
                if 'llava' in key:
                    model = 'llava'
                elif 'cogvlm' in key:
                    model = 'cogvlm'
                elif 'deepseek' in key:
                    model = 'deepseek'
                else:
                    continue

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

                # Field name: <vlm_name>_highlight_<question>_<image_filename>
                image_filename = key.split(f"{question}_")[-1]
                
                # Highlighted text is the field value
                highlights = value

                # Imageset + Narrative
                story = ''
                data_type = ''
                if image_filename in pinterest_data:
                    story = pinterest_data[image_filename][f"{model}_answers"][question]
                    data_type = 'pinterest'
                elif image_filename in renaissance_data:
                    story = renaissance_data[image_filename][f"{model}_answers"][question]
                    data_type = 'renaissance'
                else:
                    continue

                # Later version submitted the complete text
                if highlights.startswith('<span>') and highlights.endswith('</span>'):
                    story = highlights[6:-7]
                    hightlight_list = [story]
                # Earlier version submitted only highlighted parts
                else:
                    hightlight_list = highlights.split(' | ')
                    hightlight_list.sort(key=len, reverse=True)

                    # Truncate the narrative to 1000 characters
                    story = story[:1000]

                    # Change it to a complete text with highlights tags
                    for hightlight in hightlight_list:
                        if hightlight in story:
                            if hightlight == '':
                                continue
                            story = story.replace(hightlight, f"<span class=\"highlighted\">{hightlight}</span>")
                
                def add_highlight_item(json_data, image_filename, model, question, story):
                    # Check if the image filename is in the data, if not, add it
                    if image_filename not in json_data:
                        json_data[image_filename] = {f"{model}_answers": {}}

                    # Check if the model is not yet in the data structure
                    if f"{model}_answers" not in json_data[image_filename]:
                        json_data[image_filename][f"{model}_answers"] = {}

                    # Check if the question is already answered
                    if question in json_data[image_filename][f"{model}_answers"]:
                        json_data[image_filename][f"{model}_answers"][question] = json_data[image_filename][f"{model}_answers"][question] + "<br\><br\>" + story
                    else:
                        # Answer the question and update the data
                        json_data[image_filename][f"{model}_answers"][question] = story

                if data_type == 'pinterest':
                    add_highlight_item(json_data_pinterest, image_filename, model, question, story)
                elif data_type == 'renaissance':
                    add_highlight_item(json_data_renaissance, image_filename, model, question, story)

                add_highlight_item(json_all_data, image_filename, model, question, story)

                # Count how many times the image, VLM, question combination is highlighted
                counts[f"{model}_{question}_{image_filename}"] = counts.get(f"{model}_{question}_{image_filename}", 0) + 1

    # Histogram of how many times a image, VLM, question combination is highlighted
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

    # Save the data to a JSON file
    read_write_json.write_json('pinterest_data_highlight.js', json_data_pinterest, 'pinterest_data_highlighted')
    read_write_json.write_json('renaissance_data_highlight.js', json_data_renaissance, 'renaissance_data_highlighted')
    read_write_json.write_json('all_data_highlight.js', json_all_data, 'all_data_highlighted')

    return json_data_pinterest, json_data_renaissance, json_all_data



import re
from collections import defaultdict

def calculate_highlight_percentage(text):
    """Calculate the percentage of text that is within <span class='highlight'></span> tags."""
    highlighted_texts = re.findall(r"<span class=\"highlighted\">(.*?)</span>", text)
    highlighted_length = sum(len(ht) for ht in highlighted_texts)
    total_length = len(re.sub(r'<[^>]+>', '', text))  # Remove all HTML tags to get the total length of text
    print(f"Highlighted Length: {highlighted_length}")
    print(f"Total Length: {total_length}")
    return (highlighted_length / total_length) * 100 if total_length > 0 else 0

def analyze_data(data, model, task):

    text = ""
    for item in data:
        if f"{model}_answers" in data[item] and f"{task}" in data[item][f"{model}_answers"]:
            text += data[item][f"{model}_answers"][f"{task}"]

    # Calculate the percentage of highlighted text
    results = calculate_highlight_percentage(text)

    # Print the analysis results
    print(f"Model: {model}")
    print(f"  Task: {task} - Highlight Percentage: {results:.2f}%")


import read_write_json

models = ["llava", "cogvlm", "deepseek"]


# const survey_questions = [
#     {"label": "composition", "question": "What can you say about the composition of this work?"},
#     {"label": "balance_elements", "question": "On the subject of this painting's composition, what can you say about the balance between the elements?"},
#     {"label": "movement", "question": "On the subject of this painting's composition, what can you say about the movement depicted?"},
#     {"label": "focus_point", "question": "On the subject of this painting's composition, what can you say about the focus point?"},
#     {"label": "contrast_elements", "question": "On the subject of this painting's composition, what can you say about the contrast between the elements?"},
#     {"label": "proportion", "question": "On the subject of this painting's composition, what can you say about the proportion between the elements?"},
#     {"label": "foreground_background_4", "question": "What can you say about the foreground/background relationship in the composition?"},
#     {"label": "symmetry_asymmetry_1", "question": "Describe whether the composition is symmetrical or asymmetrical and why."},
#     {"label": "eye_movement_2", "question": "How is the viewer's eye movement guided in this composition?"}
# ];

tasks = ["composition", "balance_elements", "movement", "focus_point", "contrast_elements", "proportion", "foreground_background_4", "symmetry_asymmetry_1", "eye_movement_2"]

# Load the Pinterest data
pinterest_data = read_write_json.read_json("survey_pinterest_data_hightlighted_updated copy.js")

print("Pinterest Data")
# Analyze the data
for model in models:
    for task in tasks:
        analyze_data(pinterest_data, model, task)

# Load the Renaissance data
renaissance_data = read_write_json.read_json("survey_renaissance_data_hightlighted_updated copy.js")

print("Renaissance Data")
# Analyze the data
for model in models:
    for task in tasks:
        analyze_data(renaissance_data, model, task)

import re
from collections import defaultdict

def calculate_highlight_percentage(text):
    """Calculate the percentage of text that is within <span class='highlight'></span> tags."""
    highlighted_texts = re.findall(r"<span class=\"highlighted\">(.*?)</span>", text)
    highlighted_length = sum(len(ht) for ht in highlighted_texts)
    total_length = len(re.sub(r'<[^>]+>', '', text))  # Remove all HTML tags to get the total length of text
    percentage = (highlighted_length / total_length) * 100 if total_length > 0 else 0
    return {
        "highlighted_length": highlighted_length,
        "total_length": total_length,
        "percentage": round(percentage, 2)
    }

def analyze_all_data(data):
    models = ["llava", "cogvlm", "deepseek"]
    tasks = ["composition", "balance_elements", "movement", "focus_point", "contrast_elements", "proportion", "foreground_background_4", "symmetry_asymmetry_1", "eye_movement_2"]

    text = ""
    for item in data:
        for model in models:
            for task in tasks:
                if f"{model}_answers" in data[item] and f"{task}" in data[item][f"{model}_answers"]:
                    text += data[item][f"{model}_answers"][f"{task}"]
                
    # Calculate the percentage of highlighted text
    results = calculate_highlight_percentage(text)

    return results

def analyze_model_data(data, model):
    tasks = ["composition", "balance_elements", "movement", "focus_point", "contrast_elements", "proportion", "foreground_background_4", "symmetry_asymmetry_1", "eye_movement_2"]

    text = ""
    for item in data:
        for task in tasks:
            if f"{model}_answers" in data[item] and f"{task}" in data[item][f"{model}_answers"]:
                text += data[item][f"{model}_answers"][f"{task}"]

    # Calculate the percentage of highlighted text
    results = calculate_highlight_percentage(text)

    return results

def analyze_data(data, model, task):

    text = ""
    for item in data:
        if f"{model}_answers" in data[item] and f"{task}" in data[item][f"{model}_answers"]:
            text += data[item][f"{model}_answers"][f"{task}"]

    # Calculate the percentage of highlighted text
    results = calculate_highlight_percentage(text)

    return results

def create_html_latex(data, header):
    models = ["llava", "cogvlm", "deepseek"]
    tasks = ["composition", "balance_elements", "movement", "focus_point", "contrast_elements", "proportion", "foreground_background_4", "symmetry_asymmetry_1", "eye_movement_2"]

    html = f"""
        <table>
            <caption>{header}</caption>
            <thead>
                <tr>
                    <th>Model</th>
                    <th>Task</th>
                    <th>Highlighted Length</th>
                    <th>Total Length</th>
                    <th>Highlight Percentage</th>
                </tr>
            </thead>"""
    
    latex = f"""
        \\begin{{table}}[ht]
            \\centering
            \\caption{{{header}}}
            \\begin{{tabular}}{{lllll}}
                \\toprule
                \\textbf{{Model}} & \\textbf{{Task}} & \\textbf{{Highlighted Length}} & \\textbf{{Total Length}} & \\textbf{{Highlight Percentage}} \\\\
                \\midrule
        """
    
    result = analyze_all_data(data)
    html += f"""
                <tr>
                    <td>All</td>
                    <td>All</td>
                    <td>{result['highlighted_length']}</td>
                    <td>{result['total_length']}</td>
                    <td>{result['percentage']}%</td>
                </tr>"""
    
    latex += f"All & All & {result['highlighted_length']} & {result['total_length']} & {result['percentage']} \\\\"

    for model in models:
        result = analyze_model_data(data, model)
        html += f"""
                <tr>
                    <td>{model}</td>
                    <td>All</td>
                    <td>{result['highlighted_length']}</td>
                    <td>{result['total_length']}</td>
                    <td>{result['percentage']}%</td>
                </tr>"""

        latex += f"{model} & All & {result['highlighted_length']} & {result['total_length']} & {result['percentage']} \\\\"

    for model in models:
        for task in tasks:
            result = analyze_data(data, model, task)
            task_text = task.replace("fore", "").replace("_background_4", "").replace("_elements", "").replace("_asymmetry_1", "").replace("_movement_2", "")
            html += f"""
                <tr>
                    <td>{model}</td>
                    <td>{task_text}</td>
                    <td>{result['highlighted_length']}</td>
                    <td>{result['total_length']}</td>
                    <td>{result['percentage']}%</td>
                </tr>"""

            latex += f"{model} & {task_text} & {result['highlighted_length']} & {result['total_length']} & {result['percentage']} \\\\"

    html += f"""
            </tbody>
        </table>"""

    latex += f"""
            \\bottomrule
            \\end{{tabular}}
        \\end{{table}}"""

    return html, latex




import read_write_json


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

# Load the Pinterest data
pinterest_data = read_write_json.read_json("survey_pinterest_data_hightlighted_updated_v2 copy.js")

# write html to file
html, latex = create_html_latex(pinterest_data, "Pinterest Data")

with open('survey_highlight_html_table_pinterest.txt', 'w') as file:
    file.write(html)

with open('survey_highlight_latex_table_pinterest.txt', 'w') as file:
    file.write(latex)


# Load the Renaissance data
renaissance_data = read_write_json.read_json("survey_renaissance_data_hightlighted_updated_v2 copy.js")

# write html to file
html, latex = create_html_latex(renaissance_data, "Renaissance Data")

with open('survey_highlight_html_table_renaissance.txt', 'w') as file:
    file.write(html)

with open('survey_highlight_latex_table_renaissance.txt', 'w') as file: 
    file.write(latex)


all_data = read_write_json.read_json("survey_all_data_hightlighted_updated_v2 copy.js")

# write html to file
html, latex = create_html_latex(all_data, "All Data")

with open('survey_highlight_html_table_all.txt', 'w') as file:
    file.write(html)

with open('survey_highlight_latex_table_all.txt', 'w') as file:
    file.write(latex)


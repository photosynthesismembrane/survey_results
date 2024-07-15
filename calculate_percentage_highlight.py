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


def analyze_all_data_items(data):
    models = ["llava", "cogvlm", "deepseek"]
    tasks = ["composition", "balance_elements", "movement", "focus_point", "contrast_elements", "proportion", "foreground_background_4", "symmetry_asymmetry_1", "eye_movement_2"]

    results = []
    for item in data:
        for model in models:
            for task in tasks:
                if f"{model}_answers" in data[item] and f"{task}" in data[item][f"{model}_answers"]:
                    result = calculate_highlight_percentage(data[item][f"{model}_answers"][f"{task}"])
                    results.append({
                            "model": model,
                            "task": task,
                            "item": item,
                            "highlighted_length": result["highlighted_length"],
                            "total_length": result["total_length"],
                            "percentage": result["percentage"]
                    })
                
    return results

def analyze_model_data_items(data, model):
    tasks = ["composition", "balance_elements", "movement", "focus_point", "contrast_elements", "proportion", "foreground_background_4", "symmetry_asymmetry_1", "eye_movement_2"]

    results = []
    for item in data:
        for task in tasks:
            if f"{model}_answers" in data[item] and f"{task}" in data[item][f"{model}_answers"]:
                result = calculate_highlight_percentage(data[item][f"{model}_answers"][f"{task}"])
                results.append({
                        "model": model,
                        "task": task,
                        "item": item,
                        "highlighted_length": result["highlighted_length"],
                        "total_length": result["total_length"],
                        "percentage": result["percentage"]
                })

    return results

def analyze_data_items(data, model, task):

    results = []
    for item in data:
        if f"{model}_answers" in data[item] and f"{task}" in data[item][f"{model}_answers"]:
            result = calculate_highlight_percentage(data[item][f"{model}_answers"][f"{task}"])
            results.append({
                    "model": model,
                    "task": task,
                    "item": item,
                    "highlighted_length": result["highlighted_length"],
                    "total_length": result["total_length"],
                    "percentage": result["percentage"]
            })

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
                    <td>all</td>
                    <td>all</td>
                    <td>{result['total_length']}</td>
                    <td>{result['percentage']}%</td>
                </tr>"""
    
    latex += f"all & all & {result['total_length']} & {result['percentage']} \\\\"

    for model in models:
        result = analyze_model_data(data, model)
        html += f"""
                <tr>
                    <td>{model}</td>
                    <td>all</td>
                    <td>{result['total_length']}</td>
                    <td>{result['percentage']}%</td>
                </tr>"""

        latex += f"{model} & all & {result['total_length']} & {result['percentage']} \\\\"

    for model in models:
        for task in tasks:
            result = analyze_data(data, model, task)
            task_text = task.split('_')[0]
            html += f"""
                <tr>
                    <td>{model}</td>
                    <td>{task_text}</td>
                    <td>{result['total_length']}</td>
                    <td>{result['percentage']}%</td>
                </tr>"""

            latex += f"{model} & {task_text} & {result['total_length']} & {result['percentage']} \\\\"

    html += f"""
            </tbody>
        </table>"""

    latex += f"""
            \\bottomrule
            \\end{{tabular}}
        \\end{{table}}"""

    return html, latex


def create_csv(data, header):
    models = ["llava", "cogvlm", "deepseek"]
    tasks = ["composition", "balance_elements", "movement", "focus_point", "contrast_elements", "proportion", "foreground_background_4", "symmetry_asymmetry_1", "eye_movement_2"]

    csv = f"Model;Task;Item;highlight;total;percentage\n"

    result = analyze_all_data_items(data)
    for item in result:
        csv += f"{item['model']};{item['task']};{item['item']};{item['highlighted_length']};{item['total_length']};{str(item['percentage']).replace('.',',')}\n"

    csv += "\n\n\n"
    
    for model in models:
        result = analyze_model_data_items(data, model)
        for item in result:
            csv += f"{item['model']};{item['task']};{item['item']};{item['highlighted_length']};{item['total_length']};{str(item['percentage']).replace('.',',')}\n"
        csv += "\n\n\n"

    csv += "\n\n\n"

    for model in models:
        for task in tasks:
            result = analyze_data_items(data, model, task)
            for item in result:
                csv += f"{item['model']};{item['task']};{item['item']};{item['highlighted_length']};{item['total_length']};{str(item['percentage']).replace('.',',')}\n"
            csv += "\n\n\n"
        csv += "\n\n\n"

    return csv

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
pinterest_data = read_write_json.read_json("survey_pinterest_data_hightlighted_updated_v4 copy.js")

# write html to file
html_pinterest, latex_pinterest = create_html_latex(pinterest_data, "Pinterest highlights")

# with open('survey_highlight_html_table_pinterest_v3.txt', 'w') as file:
#     file.write(html)

with open('survey_highlight_latex_table_pinterest_v4.txt', 'w') as file:
    file.write(latex_pinterest)


# Load the Renaissance data
renaissance_data = read_write_json.read_json("survey_renaissance_data_hightlighted_updated_v4 copy.js")

# write html to file
html_renaissance, latex_renaissance = create_html_latex(renaissance_data, "Renaissance highlights")

# with open('survey_highlight_html_table_renaissance_v3.txt', 'w') as file:
#     file.write(html)

with open('survey_highlight_latex_table_renaissance_v4.txt', 'w') as file: 
    file.write(latex_renaissance)


all_data = read_write_json.read_json("survey_all_data_hightlighted_updated_v4 copy.js")

# write html to file
html_all, latex_all = create_html_latex(all_data, "All highlights")

# with open('survey_highlight_html_table_all_v3.txt', 'w') as file:
#     file.write(html)



with open('survey_highlight_latex_table_all_v4.txt', 'w') as file:
    file.write(latex_all)

csv_pinterest = create_csv(pinterest_data, "Pinterest Data")
csv_renaissance = create_csv(renaissance_data, "Renaissance Data")
csv_all = create_csv(all_data, "All Data")

with open('survey_highlight_csv_pinterest_v4.csv', 'w') as file:
    file.write(csv_pinterest)

with open('survey_highlight_csv_renaissance_v4.csv', 'w') as file:
    file.write(csv_renaissance)

with open('survey_highlight_csv_all_v4.csv', 'w') as file:
    file.write(csv_all)

import plot_gaussians

def create_plots(data, dataset_name):
    models = ["llava", "cogvlm", "deepseek"]
    tasks = ["composition", "balance_elements", "movement", "focus_point", "contrast_elements", "proportion", "foreground_background_4", "symmetry_asymmetry_1", "eye_movement_2"]
    
    data_dict = {
        'llava': [],
        'cogvlm': [],
        'deepseek': []
    }
    for model in models:
        result = analyze_model_data_items(data, model)
        for item in result:
            data_dict[model].append(item['percentage'])
            
    plot_gaussians.plot_gaussians(data_dict, f"Models", "Percentage", "Density", f"{dataset_name.lower().replace(' ', '_')}_model_gaussians")

    for model in models:
        data_dict = {
        }
        for task in tasks:
            task_label = task.split('_')[0]
            if task not in data_dict:
                data_dict[task_label] = []
            result = analyze_data_items(data, model, task)
            for item in result:
                data_dict[task_label].append(item['percentage'])

        plot_gaussians.plot_gaussians(data_dict, f"{model.capitalize()}", "Percentage", "Density", f"{dataset_name.lower().replace(' ', '_')}_{model}_gaussians")

    for task in tasks:
        data_dict = {
        }
        for model in models:
            if model not in data_dict:
                data_dict[model] = []
            result = analyze_data_items(data, model, task)
            for item in result:
                data_dict[model].append(item['percentage'])

        task_label = task.split('_')[0].capitalize()
        plot_gaussians.plot_gaussians(data_dict, f"{task_label}", "Percentage", "Density", f"{dataset_name.lower().replace(' ', '_')}_{task}_gaussians")

create_plots(pinterest_data, "Pinterest")
create_plots(renaissance_data, "Renaissance")
create_plots(all_data, "All")

html_full = f"""
    <div class="highlight-percentage-data-container">
        {html_all}
        <div class="main-plot-container">
            <img src="all_model_gaussians.png" alt="All data model gaussians">
            <img src="all_llava_gaussians.png" alt="All data llava gaussians">
            <img src="all_cogvlm_gaussians.png" alt="All data cogvlm gaussians">
            <img src="all_deepseek_gaussians.png" alt="All data deepseek gaussians">
        </div>
    </div>
    <div class="sub-plot-container">
        <img src="all_composition_gaussians.png" alt="All data composition gaussians">
        <img src="all_balance_elements_gaussians.png" alt="All data balance elements gaussians">
        <img src="all_movement_gaussians.png" alt="All data movement gaussians">
        <img src="all_focus_point_gaussians.png" alt="All data focus point gaussians">
        <img src="all_contrast_elements_gaussians.png" alt="All data contrast elements gaussians">
        <img src="all_proportion_gaussians.png" alt="All data proportion gaussians">
        <img src="all_foreground_background_4_gaussians.png" alt="All data foreground background gaussians">
        <img src="all_symmetry_asymmetry_1_gaussians.png" alt="All data symmetry asymmetry gaussians">
        <img src="all_eye_movement_2_gaussians.png" alt="All data eye movement gaussians">
    </div>
    <div class="highlight-percentage-data-container">
        {html_pinterest}
        <div class="main-plot-container">
            <img src="pinterest_model_gaussians.png" alt="Pinterest data model gaussians">
            <img src="pinterest_llava_gaussians.png" alt="Pinterest data llava gaussians">
            <img src="pinterest_cogvlm_gaussians.png" alt="Pinterest data cogvlm gaussians">
            <img src="pinterest_deepseek_gaussians.png" alt="Pinterest data deepseek gaussians">
        </div>
    </div>
    <div class="sub-plot-container">
        <img src="pinterest_composition_gaussians.png" alt="Pinterest data composition gaussians">
        <img src="pinterest_balance_elements_gaussians.png" alt="Pinterest data balance elements gaussians">
        <img src="pinterest_movement_gaussians.png" alt="Pinterest data movement gaussians">
        <img src="pinterest_focus_point_gaussians.png" alt="Pinterest data focus point gaussians">
        <img src="pinterest_contrast_elements_gaussians.png" alt="Pinterest data contrast elements gaussians">
        <img src="pinterest_proportion_gaussians.png" alt="Pinterest data proportion gaussians">
        <img src="pinterest_foreground_background_4_gaussians.png" alt="Pinterest data foreground background gaussians">
        <img src="pinterest_symmetry_asymmetry_1_gaussians.png" alt="Pinterest data symmetry asymmetry gaussians">
        <img src="pinterest_eye_movement_2_gaussians.png" alt="Pinterest data eye movement gaussians">
    </div>
    <div class="highlight-percentage-data-container">
        {html_renaissance}
        <div class="main-plot-container">
            <img src="renaissance_model_gaussians.png" alt="Renaissance data model gaussians">
            <img src="renaissance_llava_gaussians.png" alt="Renaissance data llava gaussians">
            <img src="renaissance_cogvlm_gaussians.png" alt="Renaissance data cogvlm gaussians">
            <img src="renaissance_deepseek_gaussians.png" alt="Renaissance data deepseek gaussians">
        </div>
    </div>
    <div class="sub-plot-container">
        <img src="renaissance_composition_gaussians.png" alt="Renaissance data composition gaussians">
        <img src="renaissance_balance_elements_gaussians.png" alt="Renaissance data balance elements gaussians">
        <img src="renaissance_movement_gaussians.png" alt="Renaissance data movement gaussians">
        <img src="renaissance_focus_point_gaussians.png" alt="Renaissance data focus point gaussians">
        <img src="renaissance_contrast_elements_gaussians.png" alt="Renaissance data contrast elements gaussians">
        <img src="renaissance_proportion_gaussians.png" alt="Renaissance data proportion gaussians">
        <img src="renaissance_foreground_background_4_gaussians.png" alt="Renaissance data foreground background gaussians">
        <img src="renaissance_symmetry_asymmetry_1_gaussians.png" alt="Renaissance data symmetry asymmetry gaussians">
        <img src="renaissance_eye_movement_2_gaussians.png" alt="Renaissance data eye movement gaussians">
    </div>
"""

with open('survey_highlight_html_table_full_v4.txt', 'w') as file:
    file.write(html_full)
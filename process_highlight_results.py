import re
import read_write_json
import plot_gaussians

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

def create_html(data):
    models = ["llava", "cogvlm", "deepseek"]
    tasks = ["composition", "balance_elements", "movement", "focus_point", "contrast_elements", "proportion", "foreground_background_4", "symmetry_asymmetry_1", "eye_movement_2"]

    html = f"""
        <table>
            <thead>
                <tr>
                    <th>Task</th>
                    <th>Llava</th>
                    <th>Cogvlm</th>
                    <th>Deepseek</th>
                </tr>
            </thead>"""
    
    html += f"""
        <tr>
            <td>All</td>"""
    for model in models:
        result = analyze_model_data(data, model)
        html += f"""
                <td>{result['percentage']}%</td>
                """
    html += f"""
        </tr>"""

    for task in tasks:
        task_text = task.split('_')[0]
        html += f"""
                <tr>
                    <td>{task_text}</td>"""
        for model in models:
            result = analyze_data(data, model, task)
            html += f"""
                    <td>{result['percentage']}%</td>"""
        html += f"""
                </tr>"""

    html += f"""
            </tbody>
        </table>"""

    return html

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
            
    plot_gaussians.plot_gaussians(data_dict, f"Models", "Percentage", "Density", f"plots\\{dataset_name.lower().replace(' ', '_')}_model_gaussians")

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

        plot_gaussians.plot_gaussians(data_dict, f"{model.capitalize()}", "Percentage", "Density", f"plots\\{dataset_name.lower().replace(' ', '_')}_{model}_gaussians")

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
        plot_gaussians.plot_gaussians(data_dict, f"{task_label}", "Percentage", "Density", f"plots\\{dataset_name.lower().replace(' ', '_')}_{task}_gaussians")

def create_combined_sets_plots(pinterest_data, renaissance_data):
    models = ["llava", "cogvlm", "deepseek"]
    tasks = ["composition", "balance_elements", "movement", "focus_point", "contrast_elements", "proportion", "foreground_background_4", "symmetry_asymmetry_1", "eye_movement_2"]
    
    for model in models:
        for task in tasks:
            data_dict = {
                'renaissance': [],
                'pinterest': [],
            }
            result_pinterest = analyze_data_items(pinterest_data, model, task)
            for item in result_pinterest:
                data_dict['pinterest'].append(item['percentage'])

            result_renaissance = analyze_data_items(renaissance_data, model, task)
            for item in result_renaissance:
                data_dict['renaissance'].append(item['percentage'])

            task_label = task.split('_')[0].capitalize()
            plot_gaussians.plot_gaussians(data_dict, f"{model.capitalize()} {task_label}", "Percentage", "Density", f"plots\\combined_sets_{model}_{task}_gaussians")

def create_plots_and_html(pinterest_data, renaissance_data, all_data):
    # Plots
    create_plots(pinterest_data, "Pinterest")
    create_plots(renaissance_data, "Renaissance")
    create_plots(all_data, "All")
    create_combined_sets_plots(pinterest_data, renaissance_data)
    
    # HTML
    html_pinterest = create_html(pinterest_data)
    html_renaissance = create_html(renaissance_data)
    html_all = create_html(all_data)

    html_full = f"""
        <div class="sub-tabs">
            <button class="sub-tab-button active" onclick="openSubTab('sub-tab5')">All</button>
            <button class="sub-tab-button" onclick="openSubTab('sub-tab6')">Pinterest</button>
            <button class="sub-tab-button" onclick="openSubTab('sub-tab7')">Renaissance</button>
            <button class="sub-tab-button" onclick="openSubTab('sub-tab8')">Sets</button>
        </div>

        <div id="sub-tab5" class="sub-tab-content" style="display: block;">
            <div class="highlight-percentage-data-container">
                {html_all}
                <div class="main-plot-container">
                    <img src="plots/all_model_gaussians.png" alt="All data model gaussians">
                    <img src="plots/all_llava_gaussians.png" alt="All data llava gaussians">
                    <img src="plots/all_cogvlm_gaussians.png" alt="All data cogvlm gaussians">
                    <img src="plots/all_deepseek_gaussians.png" alt="All data deepseek gaussians">
                </div>
            </div>
            <div class="sub-plot-container">
                <img src="plots/all_composition_gaussians.png" alt="All data composition gaussians">
                <img src="plots/all_balance_elements_gaussians.png" alt="All data balance elements gaussians">
                <img src="plots/all_movement_gaussians.png" alt="All data movement gaussians">
                <img src="plots/all_focus_point_gaussians.png" alt="All data focus point gaussians">
                <img src="plots/all_contrast_elements_gaussians.png" alt="All data contrast elements gaussians">
                <img src="plots/all_proportion_gaussians.png" alt="All data proportion gaussians">
                <img src="plots/all_foreground_background_4_gaussians.png" alt="All data foreground background gaussians">
                <img src="plots/all_symmetry_asymmetry_1_gaussians.png" alt="All data symmetry asymmetry gaussians">
                <img src="plots/all_eye_movement_2_gaussians.png" alt="All data eye movement gaussians">
            </div>
        </div>
        <div id="sub-tab6" class="sub-tab-content">
            <div class="highlight-percentage-data-container">
                {html_pinterest}
                <div class="main-plot-container">
                    <img src="plots/pinterest_model_gaussians.png" alt="Pinterest data model gaussians">
                    <img src="plots/pinterest_llava_gaussians.png" alt="Pinterest data llava gaussians">
                    <img src="plots/pinterest_cogvlm_gaussians.png" alt="Pinterest data cogvlm gaussians">
                    <img src="plots/pinterest_deepseek_gaussians.png" alt="Pinterest data deepseek gaussians">
                </div>
            </div>
            <div class="sub-plot-container">
                <img src="plots/pinterest_composition_gaussians.png" alt="Pinterest data composition gaussians">
                <img src="plots/pinterest_balance_elements_gaussians.png" alt="Pinterest data balance elements gaussians">
                <img src="plots/pinterest_movement_gaussians.png" alt="Pinterest data movement gaussians">
                <img src="plots/pinterest_focus_point_gaussians.png" alt="Pinterest data focus point gaussians">
                <img src="plots/pinterest_contrast_elements_gaussians.png" alt="Pinterest data contrast elements gaussians">
                <img src="plots/pinterest_proportion_gaussians.png" alt="Pinterest data proportion gaussians">
                <img src="plots/pinterest_foreground_background_4_gaussians.png" alt="Pinterest data foreground background gaussians">
                <img src="plots/pinterest_symmetry_asymmetry_1_gaussians.png" alt="Pinterest data symmetry asymmetry gaussians">
                <img src="plots/pinterest_eye_movement_2_gaussians.png" alt="Pinterest data eye movement gaussians">
            </div>
        </div>
        <div id="sub-tab7" class="sub-tab-content">
            <div class="highlight-percentage-data-container">
                {html_renaissance}
                <div class="main-plot-container">
                    <img src="plots/renaissance_model_gaussians.png" alt="Renaissance data model gaussians">
                    <img src="plots/renaissance_llava_gaussians.png" alt="Renaissance data llava gaussians">
                    <img src="plots/renaissance_cogvlm_gaussians.png" alt="Renaissance data cogvlm gaussians">
                    <img src="plots/renaissance_deepseek_gaussians.png" alt="Renaissance data deepseek gaussians">
                </div>
            </div>
            <div class="sub-plot-container">
                <img src="plots/renaissance_composition_gaussians.png" alt="Renaissance data composition gaussians">
                <img src="plots/renaissance_balance_elements_gaussians.png" alt="Renaissance data balance elements gaussians">
                <img src="plots/renaissance_movement_gaussians.png" alt="Renaissance data movement gaussians">
                <img src="plots/renaissance_focus_point_gaussians.png" alt="Renaissance data focus point gaussians">
                <img src="plots/renaissance_contrast_elements_gaussians.png" alt="Renaissance data contrast elements gaussians">
                <img src="plots/renaissance_proportion_gaussians.png" alt="Renaissance data proportion gaussians">
                <img src="plots/renaissance_foreground_background_4_gaussians.png" alt="Renaissance data foreground background gaussians">
                <img src="plots/renaissance_symmetry_asymmetry_1_gaussians.png" alt="Renaissance data symmetry asymmetry gaussians">
                <img src="plots/renaissance_eye_movement_2_gaussians.png" alt="Renaissance data eye movement gaussians">
            </div>
        </div>
        <div id="sub-tab8" class="sub-tab-content">
            <div class="sub-plot-container">
                    <img src="plots/combined_sets_llava_composition_gaussians.png" alt="Combined sets llava composition gaussians">
                    <img src="plots/combined_sets_cogvlm_composition_gaussians.png" alt="Combined sets cogvlm composition gaussians">
                    <img src="plots/combined_sets_deepseek_composition_gaussians.png" alt="Combined sets deepseek composition gaussians">
                    <img src="plots/combined_sets_llava_balance_elements_gaussians.png" alt="Combined sets llava balance elements gaussians">
                    <img src="plots/combined_sets_cogvlm_balance_elements_gaussians.png" alt="Combined sets cogvlm balance elements gaussians">
                    <img src="plots/combined_sets_deepseek_balance_elements_gaussians.png" alt="Combined sets deepseek balance elements gaussians">
                    <img src="plots/combined_sets_llava_movement_gaussians.png" alt="Combined sets llava movement gaussians">
                    <img src="plots/combined_sets_cogvlm_movement_gaussians.png" alt="Combined sets cogvlm movement gaussians">
                    <img src="plots/combined_sets_deepseek_movement_gaussians.png" alt="Combined sets deepseek movement gaussians">
                    <img src="plots/combined_sets_llava_focus_point_gaussians.png" alt="Combined sets llava focus point gaussians">
                    <img src="plots/combined_sets_cogvlm_focus_point_gaussians.png" alt="Combined sets cogvlm focus point gaussians">
                    <img src="plots/combined_sets_deepseek_focus_point_gaussians.png" alt="Combined sets deepseek focus point gaussians">
                    <img src="plots/combined_sets_llava_contrast_elements_gaussians.png" alt="Combined sets llava contrast elements gaussians">
                    <img src="plots/combined_sets_cogvlm_contrast_elements_gaussians.png" alt="Combined sets cogvlm contrast elements gaussians">
                    <img src="plots/combined_sets_deepseek_contrast_elements_gaussians.png" alt="Combined sets deepseek contrast elements gaussians">
                    <img src="plots/combined_sets_llava_proportion_gaussians.png" alt="Combined sets llava proportion gaussians">
                    <img src="plots/combined_sets_cogvlm_proportion_gaussians.png" alt="Combined sets cogvlm proportion gaussians">
                    <img src="plots/combined_sets_deepseek_proportion_gaussians.png" alt="Combined sets deepseek proportion gaussians">
                    <img src="plots/combined_sets_llava_foreground_background_4_gaussians.png" alt="Combined sets llava foreground background gaussians">
                    <img src="plots/combined_sets_cogvlm_foreground_background_4_gaussians.png" alt="Combined sets cogvlm foreground background gaussians">
                    <img src="plots/combined_sets_deepseek_foreground_background_4_gaussians.png" alt="Combined sets deepseek foreground background gaussians">
                    <img src="plots/combined_sets_llava_symmetry_asymmetry_1_gaussians.png" alt="Combined sets llava symmetry asymmetry gaussians">
                    <img src="plots/combined_sets_cogvlm_symmetry_asymmetry_1_gaussians.png" alt="Combined sets cogvlm symmetry asymmetry gaussians">
                    <img src="plots/combined_sets_deepseek_symmetry_asymmetry_1_gaussians.png" alt="Combined sets deepseek symmetry asymmetry gaussians">
                    <img src="plots/combined_sets_llava_eye_movement_2_gaussians.png" alt="Combined sets llava eye movement gaussians">
                    <img src="plots/combined_sets_cogvlm_eye_movement_2_gaussians.png" alt="Combined sets cogvlm eye movement gaussians">
                    <img src="plots/combined_sets_deepseek_eye_movement_2_gaussians.png" alt="Combined sets deepseek eye movement gaussians">
            </div>
        </div>
    """

    with open('highlight_html.txt', 'w') as file:
        file.write(html_full)

    return html_full
import read_highlight_results
import process_highlight_results 
import read_comparison_results

pinterest_highlight_json, renaissance_highlight_json, all_highlight_json = read_highlight_results.get_highlight_data()
highlight_html = process_highlight_results.create_plots_and_html(pinterest_highlight_json, renaissance_highlight_json, all_highlight_json)

comparison_data = read_comparison_results.create_comparison_data()
comparison_html = read_comparison_results.create_plots_and_html(comparison_data)
read_comparison_results.create_js_variable(comparison_data)

# Replace {highight_html} in the template with the highlight_html
with open('template.html', 'r') as file:
    template = file.read()
    template = template.replace('{highlight_html}', highlight_html)
    template = template.replace('{comparison_html}', comparison_html)

    # Write the template to a new file
    with open('index.html', 'w') as file:
        file.write(template)
# Process survey results

All the data is end to end processed, made into a html interface, plus intermediate data is saved in json format.

Data comes from formcarry export.json file. This file contains a list of participants, for which each comes with a list of submitted fields. There are side-by-side comparison fields and highlight fields. 

For the comparison fields is analysed which VLM won against what component. A trueskill rating is computed. An HTML table is created from these values and plots are made. 

The proportion highlighted text is computed in the highlight fields. The values are put into an HTML table. Plots are made from the distributions along several categories.

All the HTML is inserted into a template file.

Run:
```
python main.py
```

Interface link:
https://photosynthesismembrane.github.io/survey_results/
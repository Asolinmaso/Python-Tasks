import json
from collections import Counter
from bokeh.plotting import figure, show, output_file
from bokeh.io import output_notebook

def load_birthdays(filename):
    with open(filename, "r") as file:
        return json.load(file)

def count_birthdays_by_month(birthdays):
    month_counts = Counter()
    for name, birthday in birthdays.items():
        month = birthday.split('/')[0] 
        month_counts[month] += 1
    return month_counts

filename = 'birthdays.json'
birthdays = load_birthdays(filename)
month_counts = count_birthdays_by_month(birthdays)

# Prepare data for Bokeh
months = list(month_counts.keys())
counts = list(month_counts.values())

# Create a Bokeh plot
output_file("birthdays_histogram.html")  # Output to a file

p = figure(x_range=months, title="Birthday Counts by Month", height=350, toolbar_location=None, tools="")
p.vbar(x=months, top=counts, width=0.5)
p.xgrid.grid_line_color = None
p.y_range.start = 0

# Show the plot
show(p)

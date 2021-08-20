""" 9-3 -- Write To CSV.

Take the items in this list of lists: [["Top Gun", "Risky Business", "Minority 
Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on 
Fire", "Flight"]] and write them to a CSV file. The data from each list should 
be a row in the file, with each item in the list separated by a comma. 
"""


import os, sys, csv

path = os.path.join(sys.path[0], "movies.csv")
movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]]

with open(path, "w", newline='') as f:
    w = csv.writer(f, delimiter=",")

    for i in movies:
        w.writerow(i)

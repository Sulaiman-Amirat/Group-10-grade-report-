 import csv

def load_file():
    with open("Amirat.csv", "r") as f:
        return list(csv.reader(f))
  

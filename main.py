import csv
def animal_finder():
    with open('/Users/lamberto/codeExercises/Day6/csv-reader/data/cats.csv', encoding="utf-8") as f: 
        reader = csv.DictReader(f)
        cats = []
        for row in reader:
            cats.append(row)
        print(cats)
    
        # for row in reader:
            # print(f"{row['name']} is a  year old .")
        # read_data = list(f)
        # print(read_data[0].split(','))

animal_finder()


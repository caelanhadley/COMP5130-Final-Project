import csv, time, os
from apriori_python import apriori

'''
CSV Loader
    Gets contents of a CSV file.
    @filename The name of a dataset file in /datasets/
    @return A list of the CSV's contents
'''
def load_csv(filename):
    with open(os.path.join("datasets", filename), 'r') as file:
        reader = csv.reader(file)
        return list(reader)

'''
Main Loop
'''
def main(filename):
    itemsets, rules = apriori(load_csv(filename), minSup=0.5, minConf=0.5) # Do timer on apriori functions within func call
    print(rules)


if __name__ == "__main__":
    file = "Market_Basket_Optimisation.csv"
    main(file)

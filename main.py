import csv

'''
CSV Loader
    Loads a CSV file from /datasets as a string
'''
def load_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return list(reader)


'''
Dataset Parser
'''
def parse_data(data):
    item_list = ItemList()

    for recipt in data:
        for item in recipt:
            if item_list.exists(item) == False:
                item_list.add(Item(item))
            

'''
Main Loop
'''
def main(filename):
    parse_data(load_csv(filename))


class Item():
    name = ""
    count = 1

    def __init__(self, name_in):
        self.name = name_in

class ItemList():
    items = []

    def __init__(self):
        pass

    def add(self, item_in):
        self.items.append(item_in)

    def exists(self, item_in):
        if len(self.items) == 0:
            return False

        for item in self.items:
            if item.name == item_in:
                item.count += 1
                return True
        return False


if __name__ == "__main__":
    file = "Market_Basket_Optimisation.csv"
    main(file)

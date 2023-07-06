# Dream Team: Azel Lalli & Keilani Li
'''The following coding program reads a csv file and creates a dictionary where the key is the burger number and the
key is a list of quantities. Another dictionary is made where the key is the burger number and the key is a total
of burger quantities. This dictionary will be outputted when the program finishes running.'''

import csv

def read_order(fileName):
    order_dict = {}
    total_order_dict = {}

    with open(fileName, 'r') as burgerOrders:
        reader = csv.reader(burgerOrders)
        for row in reader:
            burger_number = row[0]
            quantities = list(map(int, row[1:]))

            order_dict[burger_number] = quantities
            total_order_dict[burger_number] = sum(quantities)

    return total_order_dict

def test_sum(total_order_dict):
    expected_result_total_order_dict = {'1': 91, '2': 100, '3': 32, '4': 62, '5': 64}

    for key in expected_result_total_order_dict:
        assert total_order_dict[key] == expected_result_total_order_dict[key], f'The actual result is not the same as the expected result for the order number {key}!'

def write_order_csv(total_order_dict, output_file):
    with open(output_file, 'w') as outfile:
        writer = csv.writer(outfile)

        for key, value in total_order_dict.items():
            writer.writerow([key, value])

if __name__ == "__main__":
    actual_result_total_order_dict = read_order("order.csv")
    test_sum(actual_result_total_order_dict)
    print('Everything passed!')
    write_order_csv(actual_result_total_order_dict, "outputfile.csv")

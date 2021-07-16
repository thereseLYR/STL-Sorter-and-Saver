
import os
import csv

TO_SAVE_DIR = 'SAVE_THESE.csv'
TO_DELETE_DIR = 'DELETE_THESE.CSV'
# deletion_count = 0
# to remove: giveaway_,millable, 20151002, parametric, customblock, lego_brick


def main():
    DELETION_COUNT = 0
    filename_list = convert_DELETE_THIS_CSV_to_list()
    print('Filename List:', filename_list)
    flattened_list = flatten(filename_list)
    print('Flattened list:', flattened_list)
    for file in flattened_list:
        delete(file)
        DELETION_COUNT += 1
    print('Finished running. Files Deleted:', DELETION_COUNT)


def convert_DELETE_THIS_CSV_to_list():
    with open('DELETE_THESE.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def flatten(list):
    flat_list = []
    for sublist in list:
        for item in sublist:
            flat_list.append(item)
    return flat_list


def delete(filename):
    # delete only if file exists
    if os.path.exists(filename):
        os.remove(filename)
        print('Successfully removed', filename)
        # deletion_count += 1
    else:
        print("Sorry, I can not remove %s file." % filename)


if __name__ == '__main__':
    main()

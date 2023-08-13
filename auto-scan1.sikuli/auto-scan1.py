import time
import os
import csv
import datetime

def extract():
    return extract_olivia_laptop_scale_100()

def extract_olivia_laptop_scale_100():
    item = {}
    item["title"] = Region(422,204,729,29).text()
    item["sead-result"] = Region(1496,461,395,47).text()
    item["sender"]=Region(482,252,605,20).text()
    item["veritas-tag"]=Region(447,301,97,15).text()
    item["sead-details"]=Region(1559,693,272,439).text().encode("unicode_escape")
    return item

def extract_olivia_laptop_scale_150():
    item = {}
    item["result"] = Region(939,449,310,76).text()
    item["title"] = Region(413,200,494,28).text()
    return item

def scan():
    wait_time = 10
    repeated = 200;

    result = {}

    # click on the first email
    Screen(0).click(Region(128,237,250,59)) 
    result = []

    time.sleep(wait_time)
    result.append(extract())

    # scan the following emails
    for index in range(repeated):
        type(Key.DOWN)
        time.sleep(wait_time)
        result.append(extract())
        
    return result

def save_list_of_dicts_as_csv(data_list):
    # Get the Documents folder path
    documents_folder = os.path.expanduser('~\\Documents')

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = 'scan_'+timestamp+'.csv'

    # Create an empty file in the Documents folder
    file_path = os.path.join(documents_folder, file_name)

    # Get the keys from the first dictionary to use as header
    if data_list:
        fieldnames = data_list[0].keys()
    else:
        fieldnames = []

    # Write the list of dictionaries to the CSV file
    with open(file_path, 'wb') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)

save_list_of_dicts_as_csv(scan())
#print(scan())
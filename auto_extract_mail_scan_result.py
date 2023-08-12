import time
import os
import csv
import datetime

def extract():
    return extract_olivia_laptop_scale_100()

def extract_olivia_laptop_scale_100():
    item = {}
    item["result"] = Region(1562,466,346,34).text()
    item["title"] = Region(425,201,752,32).text()
    item["sender"]=Region(493,255,633,16).text()
    item["details"]=Region(1629,699,229,341).text()
    return item

def extract_olivia_laptop_scale_150():
    item = {}
    item["result"] = Region(939,449,310,76).text()
    item["title"] = Region(413,200,494,28).text()
    return item

def scan():
    wait_time = 10
    repeated = 2;

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
    with open(file_path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)

save_list_of_dicts_as_csv(scan())
# print(scan())
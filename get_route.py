import argparse
import urllib.request
import re
import json
import csv

def extract_route(url):
    print("URL:", url)
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    html = mybytes.decode("utf8")
    fp.close()

    payload = json.loads(re.findall("payload\s=\s(\{[^;]+);", html)[0])

    #print(json.loads(payload["travels"][0]["infoJson"]))

    travels = sort_travels(payload["travels"])

    return {
        "name": payload["name"],
        "travels": travels,
        "simplified": simplify_route(travels)
    }

def simplify_route(travels):
    return {}

def sort_travels(travels):
    travels.sort(key=lambda x : x["date"])
    return travels

def save_route(data):

    # json
    json_obj = json.dumps(data["travels"], indent=4)
    with open(f'{data["name"]}.json', 'w') as file:
        file.write(json_obj)

    # csv
    csv_file = open(f'{data["name"]}.csv', 'w')
 
    csv_writer = csv.writer(csv_file)
    count = 0
 
    for travel in data["simplified"]:
        if count == 0:
 
            # Writing headers of CSV file
            header = travel.keys()
            csv_writer.writerow(header)
            count += 1
 
        # Writing data of CSV file
        csv_writer.writerow(travel.values())
 
    csv_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")

    parser.add_argument("--url", required=True)
    #parser.add_argument("--")

    args = parser.parse_args()

    data = extract_route(args.url)

    save_route(data)
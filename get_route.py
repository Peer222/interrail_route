import argparse
import urllib.request
import re
import json

def extract_route(url):
    print("URL:", url)
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    html = mybytes.decode("utf8")
    fp.close()

    payload = json.loads(re.findall("payload\s=\s(\{[^;]+);", html)[0])
    print(payload["travels"][0])

def build_csv():
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")

    parser.add_argument("--url", required=True)

    args = parser.parse_args()

    extract_route(args.url)




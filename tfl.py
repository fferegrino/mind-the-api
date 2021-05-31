import requests
import os
import sys

BASE_URL = "https://api.tfl.gov.uk"
APP_KEY = os.environ["TFL_APP_KEY"]

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("No option selected")
        exit(1)

    if sys.argv[1] == "lines":
        if len(sys.argv) != 3:
            print("No action selected")
            exit(1)
        action = sys.argv[2]
        if action == "status":
            response = requests.get(BASE_URL + "/Line/Mode/tube/Status")
            if response.status_code == 200:
                data = response.json()
                for line in data:
                    print(line["name"])
                    for status in line["lineStatuses"]:
                        print("\t", status["statusSeverityDescription"])

        else:
            print("The action you selected is not an action under lines")
            exit(1)

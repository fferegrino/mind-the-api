from typing import Optional

import requests
import typer
import os

BASE_URL = "https://api.tfl.gov.uk"
APP_KEY = os.environ["TFL_APP_KEY"]

main_app = typer.Typer()

lines_app = typer.Typer()


@lines_app.command()
def status(line_id: Optional[str] = typer.Argument(None)):
    if line_id is None:
        response = requests.get(BASE_URL + "/Line/Mode/tube/Status")
    else:
        response = requests.get(BASE_URL + f"/Line/{line_id}/Status")

    if response.status_code == 200:
        data = response.json()
        for line in data:
            print(line["name"])
            for status in line["lineStatuses"]:
                print("\t", status["statusSeverityDescription"])


main_app.add_typer(lines_app, name="lines")

if __name__ == "__main__":
    main_app()

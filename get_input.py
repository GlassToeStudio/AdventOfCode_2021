import os
import sys

import requests
from dotenv import load_dotenv


def import_data(day):
    ID = os.getenv("SESSION_ID")
    url = f"https://adventofcode.com/2020/day/{day}/input"

    cookies = {
        'session': os.getenv('SESSION_ID'),
    }

    res = requests.get(url, cookies=cookies)
    data = res.content.decode('UTF-8')
    return data


if __name__ == "__main__":
    day = sys.argv[1]
    filename = sys.argv[2]

    load_dotenv()
    data = import_data(day)

    if len(day) == 1:
        day = f"0{day}"

    try:
        os.mkdir(f"Day_{day}")
    except OSError as error:
        pass

    fi = open(f"Day_{day}/{filename}.txt", 'w')
    print(data, file=fi)
    py = open(f"Day_{day}/day_{sys.argv[1]}_problems.py", 'w')
    s = '"""'
    upper = "def format_data(data):\n    return [x.strip() for x in data.readlines()]"
    lower = f"if __name__ == \"__main__\":\n    with open(\"Day_{day}/input.txt\", \"r\") as in_file:\n        data = format_data(in_file)\n        print(data)"
    print(f"{s}\n{s}\n\n\n{upper}\n\n\n{lower}", file=py)

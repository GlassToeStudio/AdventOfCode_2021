import argparse
import os

import requests
from dotenv import load_dotenv

from colors import END, RED


def import_data(day):
    load_dotenv()
    ID = os.getenv("SESSION_ID")
    url = f"https://adventofcode.com/2021/day/{day}/input"

    cookies = {'session': ID, }

    res = requests.get(url, cookies=cookies)
    data = res.content.decode('UTF-8')
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", help="Enter the day for which you want the input file.", required=True)  # noqa: E501
    parser.add_argument("-f", "--file", help="Enter the name to save the input file.", default='input')  # noqa: E501
    args = parser.parse_args()

    data = import_data(args.day)

    try:
        os.mkdir(f"Day_{args.day}")
    except OSError as error:
        print(f"{RED}{error}{END}")
        pass

    with open(f"Day_{args.day}/{args.file}.txt", 'w') as input_file:
        print(data, file=input_file)

    with open(f"Day_{args.day}/day_{args.day}_problems.py", 'w') as python_file:  # noqa: E501
        s = '"""'
        output = (f"\"\"\"\n\"\"\"\n\n\n"
                  f"def format_data(data):\n"
                  f"    return [x.strip() for x in data.readlines()]\n\n\n"
                  f"if __name__ == \"__main__\":\n"
                  f"    with open(\"Day_{args.day}/{args.file}.txt\", \"r\") as in_file:\n"  # noqa: E501
                  f"        data = format_data(in_file)\n"
                  f"        print(data)")
        print(output, file=python_file)

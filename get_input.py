import argparse
import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from colors import END, RED


def import_input_data(url: str, ID: str) -> list[str]:
    """Grab the input data for the given url (day of advent of code)"""

    cookies = {'session': ID, }

    res = requests.get(f"{url}/input", cookies=cookies)
    data = res.content.decode('UTF-8')

    return data


def format_instruction_text(url: str, ID: str) -> str:
    """Grab the instruction text from the given url (day of advent of code)
        and return a pep8 complient copy.
    """

    # Get the instructions from the website.
    cookies = {'session': ID, }
    res = requests.get(f"{url}", cookies=cookies).text
    soup = BeautifulSoup(res, 'html.parser')

    # Save the text and format it.
    with open('temp', 'a+') as f:
        MAX_LINE_LENGTH = 79
        new_lines = []

        f.write(soup.get_text())
        f.seek(0)  # back to the beginning.
        lines = f.readlines()[18:-11]  # Cut out the junk.

        # All this just to get the title in the right spot
        t = lines.pop(0).split('---')
        t[1] = f'--- {t[1]} ---\n'
        lines.insert(0, t[1])
        lines.insert(1, t[2])

        # Break the lines up such that they are never longer
        # than MAX_LINE_LENGTH, for pep8
        for line in lines:
            start = 0
            end = MAX_LINE_LENGTH
            if end > len(line):
                new_lines.append(line)
                continue
            while end < len(line):
                while line[end] != ' ':
                    end -= 1
                new_lines.append(line[start:end] + '\n')
                start = end + 1
                end += MAX_LINE_LENGTH
                if(end > len(line)):
                    new_lines.append(line[start:]+'\n')

    os.remove('temp')

    return "".join(new_lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", help="Enter the day for which you want the input file.", required=True)  # noqa: E501
    parser.add_argument("-f", "--file", help="Enter the name to save the input file.", default='input')  # noqa: E501
    args = parser.parse_args()

    url = f"https://adventofcode.com/2020/day/{args.day}"

    load_dotenv()
    ID = os.getenv("SESSION_ID")

    data = import_input_data(url, ID)
    instructions = format_instruction_text(url, ID)

    try:
        os.mkdir(f"Day_{args.day}")
    except OSError as error:
        print(f"{RED}{error}{END}")
        pass

    with open(f"Day_{args.day}/{args.file}.txt", 'w') as input_file:
        print(data, file=input_file)

    with open(f"Day_{args.day}/day_{args.day}_problems.py", 'w') as python_file:  # noqa: E501
        s = '"""'
        output = (f"\"\"\"\n{instructions}\"\"\"\n\n\n"
                  f"def format_data(data):\n"
                  f"    return [x.strip() for x in data.readlines()]\n\n\n"
                  f"if __name__ == \"__main__\":\n"
                  f"    with open(\"Day_{args.day}/{args.file}.txt\", \"r\") as in_file:\n"  # noqa: E501
                  f"        data = format_data(in_file)\n"
                  f"        print(data)")
        print(output, file=python_file)

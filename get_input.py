import argparse
import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from colors import END, RED


def get_args() -> argparse.Namespace:
    """Setup arg parser and return optional and required args."""

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", help="Enter the day for which you want the input file.", required=True)  # noqa: E501
    parser.add_argument("-f", "--file", help="Enter the name to save the input file.", default='input')  # noqa: E501
    return parser.parse_args()


def get_session_id() -> str:
    """Get the session ID from the .env file."""

    load_dotenv()
    return os.getenv("SESSION_ID")


def get_input_data(url: str, ID: str) -> list[str]:
    """Get the input data for the given url (day of advent of code)"""

    cookies = {'session': ID, }
    res = requests.get(f"{url}/input", cookies=cookies)
    data = res.content.decode('UTF-8')

    return data


def get_instruction_data(url: str, ID: str) -> str:
    """Get the instruction text from the given url (day of advent of code)"""

    cookies = {'session': ID, }
    res = requests.get(f"{url}", cookies=cookies).text
    return BeautifulSoup(res, 'html.parser').get_text()


def format_instruction_text(html_text: str) -> str:
    """Get a pep8 formatted version of the given html_text."""

    # Save the text and format it.
    # Not sure why it differs so much after saving and reading
    # back from a file versus just doing html_text.split('\n')[18:-11]
    with open('temp', 'a+') as f:
        MAX_LINE_LENGTH = 79
        instructions = []

        f.write(html_text)
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
                instructions.append(line)
                continue
            while end < len(line):
                while line[end] != ' ':
                    end -= 1
                instructions.append(line[start:end] + '\n')
                start = end + 1
                end += MAX_LINE_LENGTH
                if(end > len(line)):
                    instructions.append(line[start:]+'\n')

    os.remove('temp')
    return "".join(instructions)


def try_make_dir(day) -> None:
    """Try to make a new directory for the given day.
        Throws an error if the directory exists.
    """

    day = fix_day(day)
    try:
        os.mkdir(f"Day_{day}")
    except OSError as error:
        print(f"{RED}{error}{END}")


def fix_day(day: str) -> str:
    """Append a 0 in front of day if day is one digit."""

    return f"0{day}" if len(day) == 1 else day


def make_input_file(day: str, file: str, data: list[str]) -> None:
    """Save the input data to a file for the given day in its
        correespsonding directory.
    """

    day = fix_day(day)
    with open(f"Day_{day}/{file}.txt", 'w') as input_file:
        input_file.write(data)


def make_python_file(day: str, file: str, instructions: str) -> None:
    """Save the instruction string to a python file for the given 
        day in its correespsonding directory.
    """

    day = fix_day(day)
    with open(f"Day_{day}/day_{day}_problems.py", 'w') as python_file:  # noqa: E501
        output = (f"\"\"\"\n{instructions}\"\"\"\n\n\n"
                  f"def format_data(data):\n"
                  f"    return [x.strip() for x in data.readlines()]\n\n\n"
                  f"if __name__ == \"__main__\":\n"
                  f"    with open(\"Day_{day}/{file}.txt\", \"r\") as in_file:\n"  # noqa: E501
                  f"        data = format_data(in_file)\n"
                  f"        print(data)\n")
        python_file.write(output)


if __name__ == "__main__":
    args = get_args()
    url = f"https://adventofcode.com/2020/day/{args.day}"
    ID = get_session_id()

    data = get_input_data(url, ID)
    instruction_data = get_instruction_data(url, ID)
    instructions = format_instruction_text(instruction_data)

    try_make_dir(args.day)
    make_input_file(args.day, args.file, data)
    make_python_file(args.day, args.file, instructions)

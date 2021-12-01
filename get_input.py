import argparse
import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from colors import END, RED


def get_args() -> argparse.Namespace:
    """Setup arg parser and return optional and required args.

    Returns:
        argparse.Namespace: args
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", help="Enter the day for which you want the input file.", required=True)  # noqa: E501
    parser.add_argument("-f", "--file", help="Enter the name to save the input file.", default='input')  # noqa: E501
    return parser.parse_args()


def get_session_id() -> str:
    """Get the session ID from the .env file.

    Returns:
        str: session id for loggged in user
    """

    load_dotenv()
    return os.getenv("SESSION_ID")


def get_input_data(url: str, ID: str) -> list[str]:
    """Get the input data for the given url (day of advent of code)

    Args:
        url (str): url of the advent of code problem for a specific day
        ID (str): session id for logged in user

    Returns:
        list[str]: the input for a given advent of code problem
    """

    cookies = {'session': ID, }
    res = requests.get(f"{url}/input", cookies=cookies)
    data = res.content.decode('UTF-8')

    return data


def get_instruction_data(url: str, ID: str) -> str:
    """Get the instruction text from the given url (day of advent of code)

    Args:
        url (str): url of the advent of code problem for a specific day
        ID (str): session id for logged in user

    Returns:
        str: html text from the given url
    """

    cookies = {'session': ID, }
    res = requests.get(f"{url}", cookies=cookies).text
    return BeautifulSoup(res, 'html.parser').get_text()


def format_instruction_text(html_text: str) -> str:
    """Get a pep8 formatted version of the given html_text.

    Args:
        html_text (str): all text from html object

    Returns:
        str: pep8 formatted set of instruction text
    """

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


def fix_day(day: str) -> str:
    """Append a zero [0] in front of day if day is one digit.

    Args:
        day (str): 1, 21, etc.

    Returns:
        str: 01, 21, etc.
    """

    return f"0{day}" if len(day) == 1 else day


def try_make_dir(day: str) -> None:
    """Try to make a new directory for the given day.\n
    ./Day_01,\n
    ./Day_21,\n
    etc.\n
    If it exists, just print to console.

    Args:
        day (str): 01, 21, etc.

    """

    if os.path.isdir(f"Day_{day}"):
        print(f"{RED}Directory exists.{END}")
    else:
        os.mkdir(f"Day_{day}")


def make_input_file(day: str, file: str, data: list[str]) -> None:
    """Save the input data to a file for the given day in its
    correspsonding directory.

    Args:
        day (str): 01, 21, etc.
        file (str): file name to save as
        data (list[str]): the data to save to file
    """
    if os.path.exists(f"Day_{day}/day_{day}_problems.py"):
        print(f"{RED}input file exists.{END}")
        return

    with open(f"Day_{day}/{file}.txt", 'w') as input_file:
        input_file.write(data)


def make_python_file(day: str, file: str, instructions: str) -> None:
    """Save the instruction string to a python file for the given
    day in its correespsonding directory. If the file exists, just
    overwrite the previous instructions with new instructions that
    include part 2.

    Args:
        day (str): 01, 21, etc.
        file (str): file name to pass into generated python code
        instructions (str): instructions to be added adt the top of python file
    """

    # If we already made the file, just overwrite the instructions,
    # keep the code we already wrote.
    if os.path.exists(f"Day_{day}/day_{day}_problems.py"):
        with open(f"Day_{day}/day_{day}_problems.py", 'r+') as python_file:
            data = python_file.read()
            s = data.split('\"\"\"', 2)
            output = (f"\"\"\"\n{instructions}\"\"\"{''.join(s[2:])}")
            python_file.seek(0)
            python_file.truncate(0)
            python_file.write(output)
    else:
        with open(f"Day_{day}/day_{day}_problems.py", 'w') as python_file:
            output = (f"\"\"\"\n{instructions}\"\"\"\n\n"
                      f"def format_data(data):\n"
                      f"    return [x.strip() for x in data.readlines()]\n\n\n"
                      f"if __name__ == \"__main__\":\n"
                      f"    with open(\"Day_{day}/{file}.txt\", \"r\") as in_file:\n"  # noqa: E501
                      f"        data = format_data(in_file)\n"
                      f"        print(data)\n")
            python_file.write(output)


if __name__ == "__main__":
    args = get_args()
    url = f"https://adventofcode.com/2021/day/{args.day}"
    id = get_session_id()
    data = get_input_data(url, id)
    instruction_data = get_instruction_data(url, id)
    instructions = format_instruction_text(instruction_data)
    day = fix_day(args.day)
    try_make_dir(day)
    make_input_file(day, args.file, data)
    make_python_file(day, args.file, instructions)

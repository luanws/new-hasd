import os
import re
import unicodedata
from typing import List

number_of_hymns = 600
path = os.path.join(os.getcwd(), 'HASD')


def get_filenames_from_path(path: str) -> List[str]:
    filenames = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            filenames.append(str_to_utf8(filename))
    return filenames


def str_to_utf8(string: str) -> str:
    return unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8')


def check_missing(values: List[int], complete_values: List[int]) -> List[int]:
    missing = list(set(complete_values) - set(values))
    missing.sort()
    return missing


filenames = get_filenames_from_path(path)
hymn_numbers_str = [(re.findall(r'^\d+', filename) + [0])[0] for filename in filenames]
hymn_numbers = [int(n) for n in hymn_numbers_str]
hymn_numbers = list(filter(lambda n: n != 0, hymn_numbers))
hymn_numbers.sort()

complete_hymn_numbers = list(range(1, number_of_hymns + 1))
missing_hymn_numbers = check_missing(hymn_numbers, complete_hymn_numbers)
if len(missing_hymn_numbers) > 0:
    print('Missing hymn numbers:')
    print('\n'.join(map(str, missing_hymn_numbers)))
else:
    print('All hymn numbers are present')

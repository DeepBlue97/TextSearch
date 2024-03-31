from pathlib import Path
from typing import List

def read_pdf():
    pass


def locate_keywords_plain(file_path: Path, keywords: List[str]):
    location = {}

    with open(file_path, 'r') as file:
        for row_num, line in enumerate(file, start=1):
            for kw in keywords:
                col_num = line.find(kw)
                if col_num != -1:
                    if location.get(kw, None) == None:
                        location[kw] = []
                    location[kw].append({'row_num': row_num, 'col_num': col_num + 1})

    return location

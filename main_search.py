from pathlib import Path
from typing import Union, List

from read import locate_keywords_plain
from print_color import print_color_text


def search_file(path: str, suffix: List[str], ignore: List[str]) -> List[Path]:
    path = Path(path)
    files = []
    if path.exists():
        if not path.is_dir():
            return files
        else:
            for _suffix in suffix:
                files += sorted(path.glob('**/*'+_suffix))
                for _ignore in ignore:
                    files = [i for i in files if _ignore not in str(i)]
            return files
    else:
        return files


if __name__ == '__main__':
    
    from config import config

    files = []

    for sp in config['search_item']:
        files += search_file(path=sp, suffix=config['suffix'], ignore=config['ignore_item'])

    for file in files:
        location = locate_keywords_plain(file_path=file, keywords=['ignore'])
        if location:
            print_color_text(str(file) + ' ', "cyan", end='')
            print(location)

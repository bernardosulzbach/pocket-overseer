import argparse
from bs4 import BeautifulSoup

FILE_PATH_ARGUMENT = 'file-path'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(FILE_PATH_ARGUMENT)
    arguments = vars(parser.parse_args())
    with open(arguments[FILE_PATH_ARGUMENT]) as file_handle:
        page = file_handle.read()
        soup = BeautifulSoup(page, 'html.parser')
        element = soup.contents[0]
        header_text = None
        set_size = 0

        def flush_set():
            nonlocal header_text, set_size
            if header_text is not None:
                print('{} ({})'.format(header_text, set_size))
                header_text = None
                set_size = 0

        while element is not None:
            if element.name == 'h1':
                flush_set()
                header_text = element.string
            if element.name == 'li':
                set_size += 1
            element = element.next_element

        flush_set()


if __name__ == '__main__':
    main()

import json
import argparse


def load_data(path):
    with open(path, 'r', encoding='utf-8') as data_file:
        try:
            data = json.load(data_file)
            return data
        except json.JSONDecodeError:
            return None


def pretty_print_json(data):
    pretty_json_string = json.dumps(data, ensure_ascii=False, indent=4)
    print(pretty_json_string)


def get_console_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file_path',
        help='путь к файлу с данными в формате JSON'
    )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    console_arguments = get_console_arguments()
    file_path = console_arguments.file_path
    try:
        json_data = load_data(file_path)
    except FileNotFoundError:
        exit('Не удалось найти файл с данными о барах.')
    if not json_data:
        exit('В указанном файле нет данных в формате JSON')
    pretty_print_json(json_data)

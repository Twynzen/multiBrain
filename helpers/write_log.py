import os
import logging


def validate_directory(directory_with_file_included: str) -> bool:
    if os.path.isdir(os.path.dirname(directory_with_file_included)) and os.access(os.path.dirname(directory_with_file_included), os.W_OK):
        return True
    return False


def write_info_in_a_log(mensaje: str, file_log: str) -> None:
    file_log = f'{os.getcwd()}/logs/{file_log}'
    if (not validate_directory(file_log)):
        print(
            f"Error: The directory {os.path.dirname(file_log)} doesn't exist")
        return None
    # print(f'Writing in the log {file_log}.log')
    format_log = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename=f'{file_log}.log',
                        level=logging.INFO, format=format_log)
    logging.info(mensaje)

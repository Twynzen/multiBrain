import os
import logging


class Logs:
    format_log = '%(asctime)s - %(levelname)s - %(message)s'

    def __init__(self):
        pass

    def validate_directory(self, directory_with_file_included: str) -> bool:
        if os.path.isdir(os.path.dirname(directory_with_file_included)) and os.access(os.path.dirname(directory_with_file_included), os.W_OK):
            return True
        return False
    
    def write_info_in_a_log(self, mensaje: str, file_log: str) -> None:
        file_log = f'{os.getcwd()}/logs/{file_log}'
        if (not self.validate_directory(file_log)):
            print(
                f"Error: The directory {os.path.dirname(file_log)} doesn't exist")
            return None
        # print(f'Writing in the log {file_log}.log')
        logging.basicConfig(filename=f'{file_log}.log',
                            level=logging.INFO, format=self.format_log)
        logging.info(mensaje)

    def write_error_in_a_log(self, mensaje: str, file_log: str) -> None:
        file_log = f'{os.getcwd()}/logs/{file_log}'
        if (not self.validate_directory(file_log)):
            print(
                f"Error: The directory {os.path.dirname(file_log)} doesn't exist")
            return None
        # print(f'Writing in the log {file_log}.log')

        logging.basicConfig(filename=f'{file_log}.log',
                            level=logging.ERROR, format=self.format_log)
        logging.info(mensaje)

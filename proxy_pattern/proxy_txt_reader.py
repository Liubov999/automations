from proxy_pattern.abstract_reader import Reader
from proxy_pattern.abstract_writer import Writer
from proxy_pattern.main import txt_writer
from proxy_pattern.txt_reader import TxtReader
from proxy_pattern.txt_writer import TxtWriter


class TxtProxyReaderWriter(Reader, Writer):
    def __init__(self, txt_reader: TxtReader):
        self.__result = ''
        self.__is_actual = False
        self.__reader = txt_reader
        self.__writer = txt_writer

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read_file()
            self.__is_actual = True
            return self.__result

    def update_actual_status(self, status):
        self.__is_actual = status

    @property
    def write_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__writer.write_file(new_data='New Data')
            self.__is_actual = True
            return self.__result
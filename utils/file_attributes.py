from os.path import splitext
from constants.constants import EXTENSION_DICT


class FileAttributes:
    def __init__(self, file):
        self.file = file
        self.file_name = self._get_file_name()
        self.file_extension = self._get_file_extension()
        self.file_type = self._get_file_type()

    def _split_file_name_ext(self):
        _split_file_name_tuple = splitext(self.file)
        return _split_file_name_tuple

    def _get_file_name(self):
        _file_extracted_name = self._split_file_name_ext()[0]
        return _file_extracted_name

    def _get_file_extension(self):
        _file_ext = self._split_file_name_ext()[1]
        return _file_ext

    def _get_file_type(self):
        for _file_type, _file_ext in EXTENSION_DICT.items():
            if self.file_extension == _file_ext:
                return _file_type

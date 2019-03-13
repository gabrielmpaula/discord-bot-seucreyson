from os import pardir
from os.path import abspath, dirname, join


CURRENT_PATH = abspath(dirname(__file__))
ROOT_DIR = abspath(join(CURRENT_PATH, pardir))
DATA_DIR_NAME = 'data'
PLAYER_DATA_DIR_NAME = 'player_data'
PLAYER_DATA_DIR = join(ROOT_DIR,DATA_DIR_NAME,PLAYER_DATA_DIR_NAME)

EXTENSION_DICT = dict()
EXTENSION_DICT['gzip'] = '.gz'
EXTENSION_DICT['zip'] = '.zip'
EXTENSION_DICT['json'] = '.json'

OPENDOTA_API = 'https://api.opendota.com/api/'


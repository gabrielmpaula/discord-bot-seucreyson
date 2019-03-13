from utils.files_management import FilesManagement
from utils.time import Time
from config.constants import PLAYER_DATA_DIR
from json import dump, load
from os.path import join
from os import chdir


class Player:
    def __init__(self, discord_name):
        self.discord_name = discord_name
        self.player = dict()
        self.player['discord_name'] = self.discord_name
        self.player['steam_id'] = None
        self.player['created_at'] = None
        self.player['opendota'] = dict()

    def link_steam_id(self, steam_id):
        self.player['steam_id'] = steam_id

    def write_data(self):
        chdir(PLAYER_DATA_DIR)
        with open('{}.json'.format(self.discord_name), 'w') as outfile:
            dump(self.player, outfile)

    def read_data(self):
        if self._mount_player_data_file_path():
            with open('{}.json'.format(self.discord_name)) as f:
                self.player = load(f)
        return self.player

    def _search_player_data(self):
        print(FilesManagement.get_sorted_files_list(PLAYER_DATA_DIR))
        if self.discord_name in FilesManagement.get_sorted_files_list(PLAYER_DATA_DIR)[1]:
            print('arquivo encontrado')
            return True
        else:
            self.player['created_at'] = Time.generate_created_at()
            print('arquivo n encontrado')
            return False

    def _mount_player_data_file_path(self):
        _player_data_file_path = join(PLAYER_DATA_DIR, self.discord_name)
        return _player_data_file_path

    def get_steam_id(self):
        self.read_data()
        return self.player['steam_id']

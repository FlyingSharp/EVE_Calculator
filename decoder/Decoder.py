import os
import glob
import re
import threading


class Decoder:
    _instance_lock = threading.Lock()

    def __init__(self):
        self._decoder_list = {}
        self._read_config()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Decoder, "_instance"):
            with Decoder._instance_lock:
                if not hasattr(Decoder, "_instance"):
                    Decoder._instance = object.__new__(cls)
        return Decoder._instance

    def __str__(self):
        return str(self._decoder_list)

    def _read_config(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        config_files = glob.glob(os.path.join(current_path, '*.config'))
        for path in config_files:
            with open(path, 'r', encoding='UTF-8') as f:
                decoder_name = None
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    match = re.match(r'(.*):(-?\d+(\.\d+)?)', line)
                    if match:  # 匹配成功，说明解码器的属性描述
                        key = match.group(1)
                        value = float(match.group(2))
                        self._decoder_list[decoder_name][key] = value
                    else:  # 匹配失败，说明是解码器的名称
                        decoder_name = line
                        self._decoder_list[decoder_name] = {}

    def get_decoder_affection(self, decoder_name):
        decoder_type = decoder_name[:2]
        if decoder_type == "生产":
            return self._decoder_list[decoder_name]['时间消耗'], self._decoder_list[decoder_name]['材料效率']
        elif decoder_type == "逆向":
            return  self._decoder_list[decoder_name]['时间消耗'], self._decoder_list[decoder_name]['逆向成功率']

    def get_decoder_success_affection(self, decoder_name):
        decoder_type = decoder_name[:2]
        if decoder_type == "逆向":
            return self._decoder_list[decoder_name]['逆向成功率']
        else:
            return 0

    def get_decoder_mat_affection(self, decoder_name):
        decoder_type = decoder_name[:2]
        if decoder_type == "生产":
            return self._decoder_list[decoder_name]['材料效率']
        else:
            return 0

if __name__ == "__main__":
    print(Decoder())

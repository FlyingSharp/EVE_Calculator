import os
import glob
import re


class Decoder:
    def __init__(self):
        self._decoder_list = {}
        self._read_config()

    def __str__(self):
        return str(self._decoder_list)

    def _read_config(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        config_files = glob.glob(os.path.join(current_path, '*.config'))
        pattern = r'(.*):(-?\d+(\.\d+)?)'
        for path in config_files:
            with open(path, 'r', encoding='UTF-8') as f:
                decoder_name = None
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    match = re.match(pattern, line)
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


if __name__ == "__main__":
    print(Decoder())

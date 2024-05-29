import os
import glob
import re
import threading

from extra_buffer.BufferData import BufferData
from decoder.Decoder import Decoder


# 统计材料
# 根据材料计算价格
# 要求可迭代计算
class Blueprint:
    _instance_lock = threading.Lock()

    def __init__(self):
        self._material_config = {}
        self._material_desc = {}
        self._max_base_prop = {}
        self._decoder_count = {}
        self._max_skill_influence = 2
        self._blueprint_price = {}

        self._read_config()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Blueprint, "_instance"):
            with Blueprint._instance_lock:
                if not hasattr(Blueprint, "_instance"):
                    Blueprint._instance = object.__new__(cls)
        return Blueprint._instance

    def __str__(self):
        return str(self._material_config) + '\n' + str(self._max_base_prop) + '\n' + str(self._decoder_count) + '\n' + str(self._material_desc)

    def _read_config(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        config_path = os.path.join(current_path, 'material.config')
        with open(config_path, 'r', encoding='UTF-8') as f:
            blueprint_name = None
            for line in f:
                line = line.strip()
                if not line:
                    continue
                match = re.match(r'(.*):(-?\d+(\.\d+)?)', line)
                if match:  # 匹配成功
                    key = match.group(1)
                    value = float(match.group(2))
                    if '最大基础成功率' in key:
                        self._max_base_prop[blueprint_name] = value
                        continue
                    elif '解码器数量' in key:
                        self._decoder_count[blueprint_name] = int(value)
                        continue
                    elif '主材料' in key:
                        match = re.match(r'(\w+):(.*)', key)
                        if match:
                            key = match[2]
                            self._material_desc[blueprint_name] = {}
                            self._material_desc[blueprint_name]['main_max_count'] = int(value)
                            self._material_desc[blueprint_name]['main_material_name'] = key
                    self._material_config[blueprint_name][key] = int(value)
                else:
                    blueprint_name = line
                    self._material_config[blueprint_name] = {}

    def _get_reverse_success_prop(self, blueprint_name, main_own_count, decoder_names):
        coef = main_own_count / self.get_main_material_max_count(blueprint_name)
        base_prop = self._max_base_prop[blueprint_name] * self._max_skill_influence
        decoder_prop = self._max_base_prop[blueprint_name] * coef * Decoder().get_decoder_success_affection(
            decoder_names)
        building_pro = BufferData.reverse_engine_prop * coef
        return base_prop + decoder_prop + building_pro

    def get_material_list(self, blueprint_name):
        return self._material_config[blueprint_name]

    def get_main_material_name(self, blueprint_name):
        return self._material_desc[blueprint_name]['main_material_name']

    def get_main_material_max_count(self, blueprint_name):
        return self._material_desc[blueprint_name]['main_max_count']

    def can_blueprint_reverse(self, blueprint_name):
        return blueprint_name in self._material_config

    # 获得最小满足100%成功率的主材料数量,如果
    def _get_mini_main_count(self, blueprint_name):
        max_main_count = self.get_main_material_max_count(blueprint_name)
        pre_main_count = max_main_count
        for own_count in range(max_main_count, 1, -1):
            success_prop = self._get_reverse_success_prop(blueprint_name, own_count, '逆向精算解码器')
            if success_prop < 1:
                break
            else:
                pre_main_count = own_count
        return pre_main_count

    # def _get_min_total_mat_list(self, blueprint_name, mat_list):
    #
    #     main_material_name = self.get_main_material_name(blueprint_name)
    #     if self.can_blueprint_reverse(main_material_name):

    def _get_double_blueprint_prop(self, blueprint_name):
        max_main_count = self.get_main_material_max_count(blueprint_name)
        return self._get_reverse_success_prop(blueprint_name, max_main_count, '逆向增量解码器')


if __name__ == "__main__":
    print(Blueprint())
    print(Blueprint()._get_mini_main_count(("万古级蓝图")))

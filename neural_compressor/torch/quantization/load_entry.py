# Copyright (c) 2024 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import os

from neural_compressor.common.utils import FP8_QUANT  # unified namespace
from neural_compressor.common.utils import load_config_mapping  # unified namespace
from neural_compressor.torch.quantization.config import FP8Config

config_name_mapping = {
    FP8_QUANT: FP8Config,
}


def load(model, output_dir="./saved_results"):
    from neural_compressor.common.base_config import ConfigRegistry

    qconfig_file_path = os.path.join(os.path.abspath(os.path.expanduser(output_dir)), "qconfig.json")
    config_mapping = load_config_mapping(qconfig_file_path, ConfigRegistry.get_all_configs()["torch"])
    model.qconfig = config_mapping
    # select load function
    config_object = config_mapping[next(iter(config_mapping))]
    if isinstance(config_object, FP8Config):
        from neural_compressor.torch.algorithms.habana_fp8 import load

        return load(model, output_dir)
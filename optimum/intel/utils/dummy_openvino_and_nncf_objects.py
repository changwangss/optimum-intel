# Copyright 2023 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .import_utils import DummyObject, requires_backends


class OVQuantizer(metaclass=DummyObject):
    _backends = ["openvino", "nncf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["openvino", "nncf"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["openvino", "nncf"])


class OVCalibrationDataset(metaclass=DummyObject):
    _backends = ["openvino", "nncf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["openvino", "nncf"])


class OVWeightQuantizationConfig(metaclass=DummyObject):
    _backends = ["openvino", "nncf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["openvino", "nncf"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["openvino", "nncf"])


class OVQuantizationConfig(metaclass=DummyObject):
    _backends = ["openvino", "nncf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["openvino", "nncf"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["openvino", "nncf"])


class OVMixedQuantizationConfig(metaclass=DummyObject):
    _backends = ["openvino", "nncf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["openvino", "nncf"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["openvino", "nncf"])

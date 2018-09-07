# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#     http://www.apache.org/licenses/LICENSE-2.0
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

# pylint: disable=redefined-builtin
# pylint: disable=missing-docstring
import json
from enum import Enum


class RuntimeType(Enum):

    PYTHON2_7 = "python2.7"
    PYTHON3_6 = "python3.6"

    # TODO : Add more runtimes here when we support more runtimes such as Java/Go/Scala etc..


class Manifest(object):
    """
    The main manifest object which gets written into the model archive as MANIFEST.json
    """

    def __init__(self, runtime, engine, model, specification_version=None, implementation_version=None,
                 description=None, publisher=None, model_server_version=None, license=None, user_data=None):

        self.runtime = RuntimeType(runtime)
        self.engine = engine
        self.model = model
        self.publisher = publisher
        self.specification_version = specification_version
        self.implementation_version = implementation_version
        self.model_server_version = model_server_version
        self.license = license
        self.description = description
        self.user_data = user_data
        self.manifest_dict = self.__to_dict__()

    def __to_dict__(self):
        manifest_dict = dict()

        manifest_dict['runtime'] = self.runtime.value

        manifest_dict['engine'] = str(self.engine)

        manifest_dict['model'] = str(self.model)

        if self.license is not None:
            manifest_dict['license'] = self.license

        if self.model_server_version is not None:
            manifest_dict['modelServerVersion'] = self.model_server_version

        if self.description is not None:
            manifest_dict['description'] = self.description

        if self.implementation_version is not None:
            manifest_dict['implementationVersion'] = self.implementation_version

        if self.specification_version is not None:
            manifest_dict['specificationVersion'] = self.specification_version

        if self.user_data is not None:
            manifest_dict['userData'] = self.user_data

        if self.publisher is not None:
            manifest_dict['publisher'] = str(self.publisher)

        return manifest_dict

    def __str__(self):
        return json.dumps(self.manifest_dict)

    def __repr__(self):
        return json.dumps(self.manifest_dict)
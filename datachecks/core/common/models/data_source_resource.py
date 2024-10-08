#  Copyright 2022-present, the Waterdip Labs Pvt. Ltd.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Dataset:
    """
    Dataset resource
    """

    name: str
    data_source: str
    description: Optional[str] = None


@dataclass
class Table:
    """
    Database Table resource
    """

    data_source: str
    name: str


@dataclass
class Index:
    """
    Search Index resource
    """

    data_source: str
    name: str


@dataclass
class Field:
    """
    Search Field resource
    """

    belongs_to: Union[Table, Index]
    name: str

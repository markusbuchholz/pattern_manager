#!/usr/bin/env python

# Copyright 2019 Danish Technological Institute (DTI)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Author: Mads Vainoe Baatrup

import pluginlib


@pluginlib.Parent('pattern', group='patterns')
class Pattern(object):
    """
    This class is the plugin parent object for pattern plugins

    :param parent: An XForm parent object under which to create the XForm pattern
    :type parent: XForm
    """

    def __init__(self, parent):
        self.parent = parent

    @pluginlib.abstractmethod
    def generate(self):
        """
        This abstract method is implemented in each plugin and is responsible for generating the
        specific pattern of XForm objects
        """

        pass
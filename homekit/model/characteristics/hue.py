#
# Copyright 2018 Joachim Lusiardi
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
#

from homekit.model.characteristics.characteristic_types import CharacteristicsTypes
from homekit.model.characteristics.characteristic_formats import CharacteristicFormats
from homekit.model.characteristics.characteristic_permissions import CharacteristicPermissions
from homekit.model.characteristics.characteristic_units import CharacteristicUnits
from homekit.model.characteristics.abstract_characteristic import AbstractCharacteristic


class HueCharacteristic(AbstractCharacteristic):
    """
    Defined on page 151
    """

    def __init__(self, iid):
        AbstractCharacteristic.__init__(self, iid, CharacteristicsTypes.HUE, CharacteristicFormats.float)
        self.perms = [CharacteristicPermissions.paired_read, CharacteristicPermissions.paired_write,
                      CharacteristicPermissions.events]
        self.minValue = 0
        self.maxValue = 360
        self.step = 1
        self.value = 0
        self.unit = CharacteristicUnits.arcdegrees

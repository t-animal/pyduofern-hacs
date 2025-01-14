from typing import TypedDict, cast

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity
from pyduofern.duofern_stick import DuofernStickThreaded

from custom_components.duofern.const import DOMAIN

class DuofernDomainData(TypedDict):
    stick: DuofernStickThreaded
    devices: dict[str, Entity]
    deviceByHassId: dict[str, Entity]


def getDuofernStick(hass: HomeAssistant) -> DuofernStickThreaded:
    return _getData(hass)['stick']

def isDeviceSetUp(hass: HomeAssistant, duofernId: str, subIdWithinHassDevice: str = "") -> bool:
    return (duofernId + subIdWithinHassDevice) in _getData(hass)['devices']

def saveDeviceAsSetUp(hass: HomeAssistant, device: Entity, duofernId: str, subIdWithinHassDevice: str = "") -> None:
    _getData(hass)['devices'][duofernId + subIdWithinHassDevice] = device
    _getData(hass)['deviceByHassId'][device.unique_id] = device

def setupDomainData(hass: HomeAssistant, stick: DuofernStickThreaded) -> None:
    hass.data[DOMAIN] = DuofernDomainData({
        'stick': stick,
        'devices': {},
        'deviceByHassId': {}
    })

def _getData(hass: HomeAssistant) -> DuofernDomainData:
    return cast(DuofernDomainData, hass.data[DOMAIN])

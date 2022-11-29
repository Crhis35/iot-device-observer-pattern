

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict
from iot_device_observer_pattern.abstracts.observer import Observer

from iot_device_observer_pattern.abstracts.subject import Subject, SubjectInput


class DeviceStatus(Enum):
    ON = "ON"
    OFF = "OFF"
    REBOOT = "REBOOT"
    MOUNTED = "MOUNTED"
    UNMOUNTED = "UNMOUNTED"
    MAINTENANCE = "MAINTENANCE"


@dataclass
class Device(Subject):
    _state: DeviceStatus = DeviceStatus.ON
    _observers: Dict[str, Observer] = field(default_factory=dict)

    @property
    def state(self) -> DeviceStatus:
        return self._state

    @property
    def observers(self) -> Dict[str, Observer]:
        return self._observers

    def attach(self, input: SubjectInput) -> str:
        self.observers[input.id] = input.observer
        return input.id

    def detach(self, input: str) -> None:
        del self.observers[input]

    def notify(self) -> None:
        for item in self.observers.values():
            item.update(self)

    def get_state(self) -> Dict:
        return {'data': self.state}

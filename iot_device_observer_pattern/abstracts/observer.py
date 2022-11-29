

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from iot_device_observer_pattern.abstracts.subject import Subject


@dataclass
class Observer(ABC):

    @abstractmethod
    def update(self, subject: 'Subject') -> None:
        raise NotImplementedError("Update is not implemented on Observer")

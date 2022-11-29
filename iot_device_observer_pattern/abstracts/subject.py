

from abc import ABC, abstractmethod
from ast import Dict
from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

from nanoid import generate

if TYPE_CHECKING:
    from iot_device_observer_pattern.abstracts.observer import Observer


@dataclass
class SubjectInput:
    observer: 'Observer'
    id: Optional[str] = generate()


@dataclass
class Subject(ABC):

    @abstractmethod
    def attach(self, input: SubjectInput) -> str:
        raise NotImplementedError("Attach is not implemented on Subject")

    @abstractmethod
    def detach(self, input: str) -> None:
        raise NotImplementedError("Detach is not implemented on Subject")

    @abstractmethod
    def notify(self,) -> None:
        raise NotImplementedError("Notify is not implemented on Subject")

    @abstractmethod
    def get_state(self,) -> Dict:
        raise NotImplementedError("Get_state is not implemented on Subject")

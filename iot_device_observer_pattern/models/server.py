

from dataclasses import dataclass
from iot_device_observer_pattern.abstracts.observer import Observer
from iot_device_observer_pattern.abstracts.subject import Subject


@dataclass
class Server(Observer):
    url: str

    def update(self, subject: 'Subject') -> None:
        print('Sending subject data {} to endpoint {}'.format(subject.get_state(), self.url))

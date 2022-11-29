

from dataclasses import dataclass
from iot_device_observer_pattern.abstracts.observer import Observer
from iot_device_observer_pattern.abstracts.subject import Subject


@dataclass
class Dashboard(Observer):

    def update(self, subject: 'Subject') -> None:
        print('Display subject data {}'.format(subject.get_state()))

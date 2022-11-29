from iot_device_observer_pattern.abstracts.subject import SubjectInput
from iot_device_observer_pattern.models.dashboard import Dashboard


def fake_data():
    return SubjectInput(Dashboard())

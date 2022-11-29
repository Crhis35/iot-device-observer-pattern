

from iot_device_observer_pattern.models.device import Device, DeviceStatus
from tests.mocks import fake_data


def test_device_instance():
    device = Device()

    assert device.state == DeviceStatus.ON
    assert device.get_state()['data'] == DeviceStatus.ON
    assert len(device.observers) == 0


def test_add_observers():
    device = Device()

    device.attach(fake_data())
    assert len(device.observers) == 1
    assert isinstance(device.attach(fake_data()), str)


def test_remove_observers():
    device = Device()

    observer_id = device.attach(fake_data())
    assert len(device.observers) == 1
    assert isinstance(observer_id, str)

    device.notify()

    device.detach(observer_id)
    assert len(device.observers) == 0

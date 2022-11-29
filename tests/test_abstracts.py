import pytest

from tests.mocks import fake_data
from iot_device_observer_pattern.abstracts.observer import Observer
from iot_device_observer_pattern.abstracts.subject import Subject

Subject.__abstractmethods__ = frozenset()
Observer.__abstractmethods__ = frozenset()


def test_observer_update():
    observer = Observer()

    with pytest.raises(NotImplementedError, match='Update is not implemented on Observer'):
        observer.update(Subject())


def test_subject_attach():
    subject = Subject()

    with pytest.raises(NotImplementedError, match='Attach is not implemented on Subject'):
        subject.attach(fake_data())


def test_subject_detach():

    subject = Subject()

    with pytest.raises(NotImplementedError, match='Detach is not implemented on Subject'):
        subject.detach('123')


def test_subject_notify():

    subject = Subject()

    with pytest.raises(NotImplementedError, match='Notify is not implemented on Subject'):
        subject.notify()


def test_subject_get_state():

    subject = Subject()

    with pytest.raises(NotImplementedError, match='Get_state is not implemented on Subject'):
        subject.get_state()

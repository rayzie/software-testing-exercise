import pytest
import random
from car import Car


@pytest.fixture
def car():
    return Car()


def test_initial_speed(car):
    assert car.speed == 0


def test_initial_odometer(car):
    assert car.odometer == 0


def test_initial_time(car):
    assert car.time == 0


# Tests for changing speed
def test_change_speed(car):
    car.change_speed(7)
    assert car.speed == 7


def test_multiple_speed_change(car):
    total_change = 0
    random.seed(42)
    for _ in range(3):
        change = random.randint(0, 10)
        total_change += change
        car.change_speed(change)
    assert car.speed == total_change


# Tests for getting current speed
def test_get_current_speed_from_start(car):
    assert car.get_current_speed() == 0


def test_get_current_speed_after_change(car):
    car.change_speed(27)
    assert car.get_current_speed() == 27

def test_average_speed_normal(car):
    car.change_speed(10)
    car.init_time()
    car.change_speed(0)  # step()을 호출하기 위한 트리거
    car.step()
    car.change_speed(-1)
    car.change_speed(-20)
    assert car.average_speed() == car.odometer / car.time

def test_average_speed_raises_on_zero_time(car):
    # 시간 증가 없이 바로 호출 → self.time == 0 상태 보장
    with pytest.raises(Exception, match="Divide by 0!"):
        car.average_speed()
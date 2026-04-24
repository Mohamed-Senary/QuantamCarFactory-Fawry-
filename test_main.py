'''
IMPORTANT: this test file is AI GENERATED but the core implementation (QuantamCarFactory) is mine:
AI was used to generate the test cases required to test all aspects and that is just to speed testing process up.
The Main.py file pretty much does the same thing using manual debugging.
'''

import pytest
from QuantamCarFactory import CarFactory, EngineType

@pytest.fixture
def factory():
    return CarFactory()

@pytest.fixture
def gas_car(factory):
    return factory.create_car(EngineType.GAS)

@pytest.fixture
def electric_car(factory):
    return factory.create_car(EngineType.ELECTRIC)

@pytest.fixture
def hybrid_car(factory):
    return factory.create_car(EngineType.HYBRID)

# --- Start/Stop ---
def test_car_starts(gas_car):
    gas_car.start()
    assert gas_car.started == True

def test_car_stops(gas_car):
    gas_car.start()
    gas_car.stop()
    assert gas_car.started == False

def test_car_cannot_stop_while_moving(gas_car):
    gas_car.start()
    gas_car.accelerate()
    gas_car.stop()
    assert gas_car.started == True

def test_car_cannot_accelerate_before_starting(gas_car):
    gas_car.accelerate()
    assert gas_car.speed == 0

# --- Accelerate/Brake ---
def test_accelerate(gas_car):
    gas_car.start()
    gas_car.accelerate()
    assert gas_car.speed == 20

def test_brake(gas_car):
    gas_car.start()
    gas_car.accelerate()
    gas_car.brake()
    assert gas_car.speed == 0

def test_speed_cap(gas_car):
    gas_car.start()
    for _ in range(15):
        gas_car.accelerate()
    assert gas_car.speed == 200

def test_speed_floor(gas_car):
    gas_car.start()
    gas_car.brake()
    assert gas_car.speed == 0

# --- Hybrid engine switching ---
def test_hybrid_uses_electric_below_50(hybrid_car):
    hybrid_car.start()
    hybrid_car.accelerate()  # 20
    assert hybrid_car.engine.ee.internal_speed == 20
    assert hybrid_car.engine.ge.internal_speed == 0

def test_hybrid_uses_gas_above_50(hybrid_car):
    hybrid_car.start()
    for _ in range(3):
        hybrid_car.accelerate()  # 60
    assert hybrid_car.engine.ge.internal_speed == 60
    assert hybrid_car.engine.ee.internal_speed == 0

def test_hybrid_switches_back_to_electric(hybrid_car):
    hybrid_car.start()
    for _ in range(3):
        hybrid_car.accelerate()  # 60
    hybrid_car.brake()  # 40
    assert hybrid_car.engine.ee.internal_speed == 40
    assert hybrid_car.engine.ge.internal_speed == 0

# --- Engine replacement ---
def test_engine_replacement(factory, gas_car):
    gas_car.start()
    gas_car.stop()
    factory.replace_engine(gas_car, EngineType.HYBRID)
    assert isinstance(gas_car.engine, factory.create_car(EngineType.HYBRID).engine.__class__)

def test_same_engine_replacement(factory, gas_car):
    factory.replace_engine(gas_car, EngineType.GAS)
    assert isinstance(gas_car.engine, type(factory.create_car(EngineType.GAS).engine))
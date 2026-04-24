from abc import ABC, abstractmethod
from enum import Enum

class Engine(ABC):

    def __init__(self):
        super().__init__()
        self.internal_speed = 0

    def _increase(self):
        self.internal_speed +=1
    
    def _decrease(self):
        self.internal_speed -=1

    def __str__(self):
        return f"Engine:\nInternal Speed:{self.internal_speed}\nActive:{self.internal_speed>0}"

    @abstractmethod
    def notify(self, target):
        pass

class GasolineEngine (Engine):

    def notify(self, target):
        while self.internal_speed < target:
            self._increase()
        while self.internal_speed > target:
            self._decrease()

    def __str__(self):
        return super().__str__()+"\nType: Gas Engine"

class ElectricEngine (Engine):

    def notify(self, target):
        while self.internal_speed < target:
            self._increase()
        while self.internal_speed > target:
            self._decrease()

    def __str__(self):
        return super().__str__()+"\nType: Electric Engine"
    
class HybridEngine (Engine):
    def __init__(self):
        super().__init__()
        self.ee = ElectricEngine()
        self.ge = GasolineEngine()

    def _increase(self):
        pass
    def _decrease(self):
        pass

    def notify(self, target):
        if target < 50:
            if self.ge.internal_speed:
                self.ge.notify(0)
            self.ee.notify(target)
            self.internal_speed = self.ee.internal_speed
            return
    
        if self.ee.internal_speed:
            self.ee.notify(0)
        self.ge.notify(target)
        self.internal_speed = self.ge.internal_speed

        def __str__(self):
            return (super().__str__() + 
                    f"\nType: Mixed Hybrid Engine\n-- Gas Engine --\n{self.ge}\n-- Electric Engine --\n{self.ee}")

class Car:
    def __init__(self, engine:Engine):
        self.speed = 0
        self.engine = engine
        self.started = False

    def start(self):
        self.started = True

    def stop(self):
        if not self.started:
            return
        if self.speed != 0:
            return
        self.started = False
            
    def accelerate(self):
        if self.started and self.speed < 200:
            self.speed += 20
            self.engine.notify(self.speed)

    def brake(self):
        if self.started and self.speed > 0:
            self.speed -= 20
            self.engine.notify(self.speed)

class EngineType(Enum):
    GAS = "GasolineEngine"
    ELECTRIC = "ElectricEngine"
    HYBRID = "HybridEngine"

class CarFactory:
    @staticmethod
    def create_car (e_type:EngineType):
        if e_type == EngineType.GAS:
            engine = GasolineEngine()
        elif e_type == EngineType.ELECTRIC:
            engine = ElectricEngine()
        elif e_type == EngineType.HYBRID:
            engine = HybridEngine()
        return Car(engine)
    
    @staticmethod
    def replace_engine (c:Car, e_type:EngineType):
        if c.engine.__class__.__name__ == e_type.value:
            print ("Invalid replacing Engine with same kind")
            return

        if e_type == EngineType.GAS:
            c.engine = GasolineEngine()
        elif e_type == EngineType.ELECTRIC:
            c.engine = ElectricEngine()
        elif e_type == EngineType.HYBRID:
            c.engine = HybridEngine()

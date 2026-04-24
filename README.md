# QuantamCarFactory-Fawry-

A Python implementation of a car factory system built as part of a Fawry screening challenge.

## 📋 Overview

A simple car factory that creates and manages cars with swappable engines. Supports three engine types with proper speed management and hybrid engine optimization.

## 🔧 Engine Types

- **GasolineEngine** — traditional gas powered engine
- **ElectricEngine** — electric powered engine
- **MixedHybridEngine** — smart hybrid that uses electric below 50 km/h and switches to gas at 50 km/h and above, never running both simultaneously

## 🚙 Car Operations

| Operation | Behavior |
|---|---|
| `start()` | Starts the car at 0 speed |
| `stop()` | Stops the car, only if speed is 0 |
| `accelerate()` | Increases speed by 20 km/h (max 200) |
| `brake()` | Decreases speed by 20 km/h (min 0) |

## 🏭 Factory

The `CarFactory` class handles:
- Creating a new car with a specified engine type
- Replacing the engine of an existing car

```python
factory = CarFactory()
car = factory.create_car(EngineType.GAS)
factory.replace_engine(car, EngineType.HYBRID)
```

## 🧪 Running Tests

```bash
pip install pytest
pytest test_main.py -v
```

## ▶️ Running the Demo

```bash
python main.py
```

## 📁 Project Structure
```
├── QuantamCarFactory.py  # All core classes (Engine, Car, CarFactory, EngineType)
├── Main.py               # Demo script
└── test_main.py          # Pytest test suite
```
------------
> 🤖 This README and the test file were AI generated. The core implementation is original work.

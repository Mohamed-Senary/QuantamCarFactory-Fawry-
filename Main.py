from QuantamCarFactory import CarFactory, EngineType

def main():
    factory = CarFactory()

    # Create cars with each engine type
    gas_car = factory.create_car(EngineType.GAS)
    electric_car = factory.create_car(EngineType.ELECTRIC)
    hybrid_car = factory.create_car(EngineType.HYBRID)

    # Test gas car
    print("=== Gas Car ===")
    gas_car.start()
    print(f"Started | Speed: {gas_car.speed} | {gas_car.engine}")
    gas_car.accelerate()
    print(f"Accelerated | Speed: {gas_car.speed} | {gas_car.engine}")
    gas_car.accelerate()
    print(f"Accelerated | Speed: {gas_car.speed} | {gas_car.engine}")
    gas_car.brake()
    print(f"Braked | Speed: {gas_car.speed} | {gas_car.engine}")
    gas_car.brake()
    print(f"Braked | Speed: {gas_car.speed} | {gas_car.engine}")
    gas_car.stop()
    print(f"Stopped | Started: {gas_car.started}")

    # Test electric car
    print("\n=== Electric Car ===")
    electric_car.start()
    print(f"Started | Speed: {electric_car.speed} | {electric_car.engine}")
    electric_car.accelerate()
    print(f"Accelerated | Speed: {electric_car.speed} | {electric_car.engine}")
    electric_car.stop()
    print(f"Stop while moving (should not stop the engine as speed !=0) | Started: {electric_car.started}")
    electric_car.brake()
    print(f"Braked | Speed: {electric_car.speed} | {electric_car.engine}")
    electric_car.stop()
    print(f"Stopped | Started: {electric_car.started}")

    # Test hybrid car
    print("\n=== Hybrid Car ===")
    hybrid_car.start()
    print(f"Started | Speed: {hybrid_car.speed} | {hybrid_car.engine}")
    hybrid_car.accelerate()
    print(f"Accelerated | Speed: {hybrid_car.speed} | {hybrid_car.engine}")
    hybrid_car.accelerate()
    print(f"Accelerated | Speed: {hybrid_car.speed} | {hybrid_car.engine}")
    hybrid_car.accelerate()
    print(f"Accelerated | Speed: {hybrid_car.speed} | {hybrid_car.engine}")
    hybrid_car.brake()
    print(f"Braked | Speed: {hybrid_car.speed} | {hybrid_car.engine}")
    hybrid_car.brake()
    print(f"Braked | Speed: {hybrid_car.speed} | {hybrid_car.engine}")
    hybrid_car.brake()
    print(f"Braked | Speed: {hybrid_car.speed} | {hybrid_car.engine}")
    hybrid_car.stop()
    print(f"Stopped | Started: {hybrid_car.started}")

    # Test engine replacement
    print("\n=== Engine Replacement ===")
    factory.replace_engine(gas_car, EngineType.HYBRID)
    print(f"Replaced gas with hybrid | {gas_car.engine}")
    factory.replace_engine(gas_car, EngineType.HYBRID)
    print(f"Same engine replacement attempt | {gas_car.engine}")

if __name__ == "__main__":
    main()
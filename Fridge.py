from abc import ABC, abstractmethod
from typing import List, Optional

class IDoor(ABC):
    @abstractmethod
    def open(self) -> None:
        pass
    
    @abstractmethod
    def close(self) -> None:
        pass
    
    @abstractmethod
    def get_status(self) -> str:
        pass

class IStorage(ABC):
    @abstractmethod
    def put_product(self, product: str) -> None:
        pass
    
    @abstractmethod
    def get_products(self) -> List[str]:
        pass

class ITemperatureController(ABC):
    @abstractmethod
    def set_temperature(self, temp: int) -> None:
        pass
    
    @abstractmethod
    def get_temperature(self) -> str:
        pass

class Door(IDoor):
    def __init__(self, status: int = 0):
        self._status = status
    
    def open(self) -> None:
        if self._status == 1:
            print("Дверь холодильника уже открыта")
        else:
            print("Дверь холодильника была открыта успешно")
            self._status = 1
    
    def close(self) -> None:
        if self._status == 0:
            print("Дверь холодильника уже закрыта")
        else:
            print("Дверь холодильника была закрыта успешно")
            self._status = 0
    
    def get_status(self) -> str:
        return "Дверь холодильника открыта" if self._status == 1 else "Дверь холодильника закрыта"

class ProductStorage(IStorage):
    def __init__(self):
        self._products: List[str] = []
    
    def put_product(self, product: str) -> None:
        try:
            if not isinstance(product, str):
                raise TypeError(f"Ожидается строка, получен {type(product).__name__}")
            
            if not product.strip():
                raise ValueError("Продукт не может быть пустой строкой")
            
            self._products.append(product)
            print(f"Продукт '{product}' был успешно помещен в холодильник")
            
        except TypeError as e:
            print(f"Ошибка типа: {e}")
            raise
        except ValueError as e:
            print(f"Ошибка значения: {e}")
            raise
    
    def get_products(self) -> List[str]:
        return self._products.copy()


class TemperatureController(ITemperatureController):
    MIN_TEMP = 0
    MAX_TEMP = 12
    
    def __init__(self, initial_temp: int = 4):
        self._temperature = initial_temp
    
    def set_temperature(self, temp: int) -> None:
        if self.MIN_TEMP <= temp <= self.MAX_TEMP:
            self._temperature = temp
            print(f"В холодильнике установлена новая температура: {temp}°C")
        else:
            print(f"Неверная температура. Допустимый диапазон: {self.MIN_TEMP}-{self.MAX_TEMP}°C")
    
    def get_temperature(self) -> str:
        return f"{self._temperature}°C"

class SmartDoor(Door):
    def open(self) -> None:
        super().open()
        if self._status == 1:
            print("Включена подсветка холодильника")
    
    def close(self) -> None:
        super().close()
        if self._status == 0:
            print("Подсветка выключена")


class Refrigerator:
    def __init__(self, 
                 door: Optional[IDoor] = None,
                 storage: Optional[IStorage] = None,
                 temp_controller: Optional[ITemperatureController] = None):
        self._door = door or Door()
        self._storage = storage or ProductStorage()
        self._temp_controller = temp_controller or TemperatureController()
    
    def show_info(self) -> None:
        print("\n" + "="*40)
        print("ИНФОРМАЦИЯ О ХОЛОДИЛЬНИКЕ")
        print("="*40)
        print(f"Состояние: {self._door.get_status()}")
        print(f"Температура: {self._temp_controller.get_temperature()}")
        products = self._storage.get_products()
        print(f"Продукты ({len(products)}): {', '.join(products) if products else 'холодильник пуст'}")
        print("="*40)

    @property
    def door(self) -> IDoor:
        return self._door
    
    @property
    def storage(self) -> IStorage:
        return self._storage
    
    @property
    def temperature_controller(self) -> ITemperatureController:
        return self._temp_controller

class RefrigeratorFactory:
    @staticmethod
    def create_standard() -> Refrigerator:
        return Refrigerator()
    
    @staticmethod
    def create_smart() -> Refrigerator:
        return Refrigerator(door=SmartDoor())


def demonstrate_refrigerators():
    print("=== СТАНДАРТНЫЙ ХОЛОДИЛЬНИК ===")
    fridge1 = RefrigeratorFactory.create_standard()

    fridge1.show_info()
    fridge1.door.open()
    
    fridge1.storage.put_product("Молоко")
    fridge1.storage.put_product("Яйца")
    fridge1.storage.put_product("Сыр")
    try:
        # попытка добавить несуществующий продукт(неккоректное значение)
        fridge1.storage.put_product("")  
    except ValueError:
        pass
    
    try:
        # попытка добавить некорректный продукт(число)
        fridge1.storage.put_product(123) 
    except TypeError:
        pass
    
    try:
        fridge1.storage.put_product(None)  
    except TypeError:
        pass
    
    fridge1.door.close()
    fridge1.temperature_controller.set_temperature(5)
    fridge1.show_info()
    
    print("\n=== УМНЫЙ ХОЛОДИЛЬНИК ===")
    fridge2 = RefrigeratorFactory.create_smart()
    fridge2.door.open()
    fridge2.storage.put_product("Овощи")
    fridge2.storage.put_product("Фрукты")
    fridge2.door.close()
    fridge2.show_info()


if __name__ == "__main__":
    demonstrate_refrigerators()

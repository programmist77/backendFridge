class door_status():
    def __init__(self, status):
        self.status = status
        
    def open_door(self):
        if self.status == 1:
            print("Дверь холодильника уже открыта")
        elif self.status == 0:
            print("Дверь холодильника была открыта успешно ")
            self.status = 1

    def close_door(self):
        if self.status == 1:
            print("Дверь холодильника была закрыта успешно")
            self.status = 0
        elif self.status == 0:
            print("Дверь холодильника уже закрыта")
    
    def door_status(self):
        if self.status == 1:
            return "Дверь холодильника открыта";
        elif self.status == 0:
            return "Дверь холодильника закрыта";

class put_products():
    def __init__(self):
        self.products = []

    def put_product(self, product):
        self.products.append(product)
        print(f"Продукт {product} был успешно помещен в холодильник")

    def get_products(self):
        return self.products

class cold_temp():
    def __init__(self, new_temp):
        self.temperature = new_temp

    def InstallTemp(self, temp):
        if 0 <= temp <= 12:
            self.temperature = temp
            print(f"В холодильнике установлена новая температура {temp}")
        else: 
            print("В холодильник не может быть установлена данная температура. Пожалуйста, укажите в диапозоне от 0 до 12")

    def get_temperature(self):
        return f"{self.temperature}℃"

class cold_info():
    def __init__(self):
        self.door = door_status(status=0)
        self.temperature = cold_temp(new_temp=4)
        self.products = put_products()

    def show_info(self):
        print("\nИНФОРМАЦИЯ О ХОЛОДИЛЬНИКЕ")
        print(f"{self.door.door_status()}")
        print(f"Температура: {self.temperature.get_temperature()}")
        print(f"Продукты внутри: {self.products.get_products()}")

def UseCold():
    my_fridge = cold_info()
    my_fridge.show_info()

    my_fridge.door.open_door()
    my_fridge.products.put_product("Яблоко")
    my_fridge.door.close_door()
    my_fridge.temperature.InstallTemp(8)

    my_fridge.show_info()

if __name__ == "__main__":
    UseCold()


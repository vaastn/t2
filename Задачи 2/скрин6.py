class Aircraft:
    def __init__(self, model):
        self.model = model

class Route:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

class Airline:
    def __init__(self):
        self.aircrafts = []
        self.routes = []

    def add_aircraft(self, model):
        self.aircrafts.append(Aircraft(model))
        print(f"Самолет {model} добавлен")

    def remove_aircraft(self, model):
        for aircraft in self.aircrafts:
            if aircraft.model == model:
                self.aircrafts.remove(aircraft)
                print(f"Самолет {model} удален")
                return
        print(f"Самолет {model} не найден")

    def add_route(self, origin, destination):
        self.routes.append(Route(origin, destination))
        print(f"Маршрут из {origin} в {destination} добавлен")

    def remove_route(self, origin, destination):
        for route in self.routes:
            if route.origin == origin and route.destination == destination:
                self.routes.remove(route)
                print(f"Маршрут из {origin} в {destination} удален")
                return
        print(f"Маршрут из {origin} в {destination} не найден")

    def find_aircraft_by_model(self, model):
        for aircraft in self.aircrafts:
            if aircraft.model == model:
                print(f"Самолет {model} найден")
                return
        print(f"Самолет {model} не найден")

    def find_routes_by_city(self, city):
        available_routes = []
        for route in self.routes:
            if route.origin == city:
                available_routes.append(route.destination)
        if available_routes:
            print(f"Доступные маршруты из {city}: {', '.join(available_routes)}")
        else:
            print(f"Нет доступных маршрутов {city}")

# пример использования класса
if __name__ == "__main__":
    airline = Airline()

    # добавление самолетов
    airline.add_aircraft("Boeing 747")
    airline.add_aircraft("Airbus A320")

    # добавление маршрутов
    airline.add_route("Нью-йорк", "Лондон")
    airline.add_route("Лондон", "Париж")
    airline.add_route("Париж", "Токио")

    # поиск самолета по модели
    airline.find_aircraft_by_model("Boeing 747")
    airline.find_aircraft_by_model("Airbus A380")

    # поиск доступных маршрутов для заданного города
    airline.find_routes_by_city("Лондон")
    airline.find_routes_by_city("Токио")

    # Удаление самолета и маршрута
    airline.remove_aircraft("Boeing 747")
    airline.remove_route("Лондон", "Париж")

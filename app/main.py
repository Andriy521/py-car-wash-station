class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Car) -> float:
        wash_cost = car.comfort_class * \
            (self.clean_power - car.clean_mark) * \
            self.average_rating / self.distance_from_city_center
        return round(wash_cost, 1)

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.wash_single_car(car)
        return income

    def rate_service(self, num: float) -> None:
        sum_of_rates = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        new_sum = sum_of_rates + num
        final_result = new_sum / self.count_of_ratings
        self.average_rating = round(final_result, 1)

    def wash_single_car(self, car: Car) -> float:
        income = self.calculate_washing_price(car)
        car.clean_mark = self.clean_power
        return income

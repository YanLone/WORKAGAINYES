from typing import Dict, Type


class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self, training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return(f'Тип тренировки {self.training_type}; ',
               f'Длительность: {self.duration} ч.; ',
               f'Дистанция: {self.distance} км; ',
               f'Ср. скорость: {self.speed} км/ч; ',
               f'Потрачено ккал: {self.calories}; ')


class Training:
    """Базовый класс тренировки."""
    
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    MINUTES_TO_HOURS: float = 60
    MULTIPLY_TWO: int = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.MINUTES_TO_HOURS

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        InfoMessage(self.__class__.__name__,
                    self.duration,
                    self.get_distance(),
                    self.get_mean_speed(),
                    self.get_spent_calories())
        return InfoMessage


class Running(Training):
    """Тренировка: бег."""

    coeff_calorie_1 = 18
    coeff_calorie_2 = 20

    def get_spent_calories(self):
        return ((self.coeff_calorie_1 * self.get_mean_speed()
                - self.coeff_calorie_2) * self.M_IN_KM
                * self.MINUTES_TO_HOURS)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    
    coeff_calorie_1 = 0.035
    coeff_calorie_2 = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action,
                         duration,
                         weight)
        self.height = height


def get_spent_calories(self) -> float:
    return ((self.coeff_calorie_1 * self.weight
            + (self.get_mean_speed() ** self.MULTIPLY_TWO)
            * self.coeff_calorie_2 * self.height)
            * self.MINUTES_TO_HOURS)


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP: float = 1.38
    coeff_calorie_1 = 1.1

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.MINUTES_TO_HOURS)

    def get_spent_calories(self):
        return (self.get_mean_speed() + self.coeff_calorie_1
                * self.MULTIPLY_TWO * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    database: Dict[str, Type[Training]] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking}
    return database[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    
    print(training.show_training_info().get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
                ]
for workout_type, data in packages:
    training = read_package(workout_type, data)
    main(training)

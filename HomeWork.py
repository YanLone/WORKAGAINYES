from typing import Dict, Type

class InfoMessage:
    def __init__(self,  
                 training_type,
                 duration,
                 distance, 
                 speed, 
                 calories) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
    
    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; ' 
                f'Длительность: {self.duration} ч.; ' 
                f'Дистанция: {self.distance} км; ' 
                f'Ср. скорость: {self.speed} км/ч; ' 
                f'Потрачено ккал: {self.calories} ')
    

        """Информационное сообщение о тренировке."""
    


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM: float = 1000   
    MINUTES_TO_HOURS: float = 60
    

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight         
        
    
    
    def get_distance(self) -> float:
        return self.action * self.LEN_STEP / self.M_IN_KM
        """Получить дистанцию в км."""
       

    def get_mean_speed(self) -> float:
        return self.get_distance() / self.duration

        """Получить среднюю скорость движения."""
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass
        

    def show_training_info(self) -> InfoMessage:
        return InfoMessage(self.__class__.__name__,
                          self.duration,
                          self.get_distance(), 
                          self.get_mean_speed(), 
                          self.get_spent_calories())
        
        """Вернуть информационное сообщение о выполненной тренировке."""
        
class Running(Training):
    coeff_calorie_1 = 18
    coeff_calorie_2 = 20
    



    def get_spent_calories(self) -> float:
        return ((self.coeff_calorie_1 * self.get_mean_speed()
                 - self.coeff_calorie_2)
                * self.weight / self.M_IN_KM
                * self.MINUTES_TO_HOURS)        
    """Тренировка: бег."""
    


class SportsWalking(Training):
    coeff_calorie_1 = 0.035
    coeff_calorie_2 = 0.029
   

    def __init__(self,
                action: int,
                duration: float, 
                weight: float,
                height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height


    def get_spent_calories(self):
        return ((self.coeff_calorie_1 * self.weight 
                + (self.get_mean_speed()**2 // self.height) 
                * self.coeff_calorie_2 * self.weight) 
                * self.MINUTES_TO_HOURS)    

    """Тренировка: спортивная ходьба."""
class Swimming(Training):
    coeff_calorie_1 = 1.1
    LEN_STEP = 1.38
    

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        


    def get_mean_speed(self): 
        return (self.length_pool * self.count_pool 
               / self.M_IN_KM / self.MINUTES_TO_HOURS)


    def get_spent_calories(self):
        return ((self.get_mean_speed() + self.coeff_calorie_1)
               * 2 * self.weight)
    
        """Тренировка: плавание."""
    


def read_package(workout_type: str, data: list) -> Training:    
    database: Dict[str, Type[Training]] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
}
    return database[workout_type](*data)
    
    """Прочитать данные полученные от датчиков."""
    


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info().get_message()
    print(info)
    


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]     
for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
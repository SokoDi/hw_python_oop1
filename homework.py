class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 traning_type: str,
                 duration: float,
                 distens: float,
                 speed: float,
                 calories: float,
                 ) -> None:

        self.traning_type = traning_type
        self.duration = duration
        self.distanse = distens
        self.speed = speed
        self.calories = calories

    def __str__(self) -> str:
        return (f'Тип тренеровки: {self.traning_type};'
                f'Длительность: {self.duration} ч.;'
                f'Дистанция: {round(self.duration, 3)} км;'
                f'Ср. скорость: {round(self.speed, 3)} км/ч;'
                f'Потрачено ккал {round(self.calories, 3)}.')


M_IN_KM = 1000


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:

        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        return self.action * self.LEN_STEP / M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage


class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def get_spent_calories(self) -> float:
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER
                + self.get_mean_speed()
                + self.CALORIES_MEAN_SPEED_SHIFT)
                * self.weight / M_IN_KM * (self.duration * 60))


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CALORIES_MEAN_SPEED_MULTIPLIER = 0.035
    CALORIES_MEAN_SPEED_SHIFT = 0.029

    def __init__(self, height: int) -> None:
        self.height = height

    def get_mean_speed(self) -> float:
        return self.get_distance() * M_IN_KM / self.duration * 60

    def get_spent_calories(self) -> float:
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.weight
                + ((self.get_mean_speed * 60) ** 2
                 / self.height * 100) * self.CALORIES_MEAN_SPEED_SHIFT
                * self.weight) * self.speed * 60)


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

import numpy as np

# Пример данных времени ответа в миллисекундах
response_times = np.array([180, 200, 205, 210, 190, 195, 205, 220, 230, 300,406,120])

# Среднее значение и стандартное отклонение
mean = np.mean(response_times)
std_dev = np.std(response_times)

# Функция для вычисления Z-оценки
def calculate_z_score(value):
    return (value - mean) / std_dev

# Проверяем каждое значение на аномалию
for time in response_times:
    z_score = calculate_z_score(time)
    if abs(z_score) > 2:  # Порог Z-оценки
        print(f"Аномалия обнаружена: {time} мс, Z-оценка: {z_score:.2f}")

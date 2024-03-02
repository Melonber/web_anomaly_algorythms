import numpy as np

# Генерируем искусственные данные о времени загрузки веб-страницы (в секундах)
np.random.seed(42)
load_times = np.random.normal(3, 0.5, 100)  # Среднее время загрузки 3 секунды, стандартное отклонение 0.5
print(load_times)
# Определение квантилей
lower_quantile = np.quantile(load_times, 0.05)
upper_quantile = np.quantile(load_times, 0.95)

# Поиск аномалий
anomalies = []
for time in load_times:
    if time < lower_quantile or time > upper_quantile:
        anomalies.append(time)

# Вывод результатов
print(f"Нижний квантиль (5%): {lower_quantile:.2f} сек")
print(f"Верхний квантиль (95%): {upper_quantile:.2f} сек")
print("Обнаруженные аномалии во времени загрузки:", anomalies)

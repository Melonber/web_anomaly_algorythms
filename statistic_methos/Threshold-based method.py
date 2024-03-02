# Пример данных загрузки CPU в процентах
cpu_loads = [55, 60, 58, 65, 70, 80, 85, 90, 95, 75, 80, 88, 92]

# Установка порогового значения
threshold = 85

# Функция для проверки каждого значения загрузки CPU
def check_cpu_load(data, threshold):
    anomalies = []
    for index, load in enumerate(data):
        if load > threshold:
            anomalies.append((index, load))
    return anomalies

# Поиск аномалий
anomalies = check_cpu_load(cpu_loads, threshold)

# Вывод результатов
if anomalies:
    print("Обнаружены аномалии в загрузке CPU:")
    for anomaly in anomalies:
        print(f"Индекс: {anomaly[0]}, Загрузка: {anomaly[1]}%")
else:
    print("Аномалии не обнаружены.")

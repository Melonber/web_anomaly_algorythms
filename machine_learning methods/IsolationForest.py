from sklearn.ensemble import IsolationForest
import numpy as np

# Предположим, что у нас есть сгенерированные данные о трафике (количество запросов в минуту)
np.random.seed(42)
normal_traffic = np.random.normal(loc=100, scale=10, size=1000)  # Нормальный трафик
spike_traffic = np.random.normal(loc=500, scale=10, size=50)  # Пики трафика
traffic_data = np.concatenate((normal_traffic, spike_traffic))

# Переформатируем данные для обучения модели
traffic_data = traffic_data.reshape(-1, 1)

# Обучение модели изолирующего леса
clf = IsolationForest(contamination=0.05)  # предполагаемая доля аномалий в данных
clf.fit(traffic_data)

# Предсказание
predictions = clf.predict(traffic_data)

# Идентификация аномального трафика
anomalies = traffic_data[predictions == -1]

print(f"Обнаружено {len(anomalies)} потенциальных аномалий.")

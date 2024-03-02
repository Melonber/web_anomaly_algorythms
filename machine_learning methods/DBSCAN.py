from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np

# Предположим, у нас есть предобработанные данные о трафике веб-сайта
X = np.random.rand(100, 2)  # Искусственные данные для примера

# Нормализация данных
X_scaled = StandardScaler().fit_transform(X)

# Применение DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
clusters = dbscan.fit_predict(X_scaled)

# Определение шума как аномалий
anomalies = X[clusters == -1]
print(f"Обнаружено {len(anomalies)} аномалий.")

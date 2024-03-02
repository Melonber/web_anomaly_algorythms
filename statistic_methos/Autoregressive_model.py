import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg

# Генерация искусственного временного ряда, где значения могут увеличиваться и уменьшаться
np.random.seed(42)
data = np.random.normal(0, 0.5, 100).cumsum() + 50  # Измененные параметры для более реалистичного ряда

# Создание временного ряда
ts = pd.Series(data)

# Определение и обучение авторегрессионной модели
model = AutoReg(ts, lags=1)
model_fitted = model.fit()

# Прогнозирование
predictions = model_fitted.predict(start=len(ts), end=len(ts) + 10, dynamic=True)

# Визуализация с прогнозом
plt.figure(figsize=(10, 6))
plt.plot(ts, label='Исходные данные')
plt.plot(np.arange(len(ts), len(ts) + 11), predictions, label='Прогноз', linestyle='--')
plt.legend()
plt.title("Авторегрессионная модель с прогнозированием загрузки CPU")
plt.show()

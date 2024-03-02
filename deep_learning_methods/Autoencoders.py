from keras.layers import Input, Dense
from keras.models import Model
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Предположим, data - это предобработанные данные логов
data = np.random.rand(1000, 20)  # Искусственные данные для примера
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

# Разделение на обучающую и тестовую выборки
X_train = data_scaled[:800]
X_test = data_scaled[800:]

# Архитектура автоэнкодера
input_layer = Input(shape=(X_train.shape[1],))
encoded = Dense(10, activation='relu')(input_layer)
decoded = Dense(X_train.shape[1], activation='sigmoid')(encoded)
autoencoder = Model(input_layer, decoded)

autoencoder.compile(optimizer='adam', loss='mean_squared_error')

# Обучение
autoencoder.fit(X_train, X_train, epochs=50, batch_size=256, shuffle=True, validation_split=0.2)

# Оценка ошибки реконструкции
reconstructed = autoencoder.predict(X_test)
mse = np.mean(np.power(X_test - reconstructed, 2), axis=1)

# Определение порога для ошибки реконструкции и выявление аномалий
threshold = np.quantile(mse, 0.95)
anomalies = mse > threshold
print(f"Обнаружено {np.sum(anomalies)} аномалий из {len(X_test)} записей.")

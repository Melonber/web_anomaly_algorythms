<h1>Статистические методы:</h1>
<h2>Z-оценка(z-score)</h2> это статистический инструмент, который измеряет количество стандартных отклонений, на которое значение отклоняется от среднего значения выборки. Формула Z-оценки:<br />
<img width="119" alt="image" src="https://github.com/Melonber/web_anomaly_algorythms/assets/68331365/c5f4888a-3e16-4b7e-ad36-a4246c0e7cf6"><br />
где:<br />
<img width="328" alt="image" src="https://github.com/Melonber/web_anomaly_algorythms/assets/68331365/399a4713-1c3e-491a-bc27-6f544537c4e4"><br />
Предположим, у нас есть веб-сервис, и мы хотим обнаружить аномалии во времени его ответа. Допустим, среднее время ответа (μ) составляет 200 мс, а стандартное отклонение (σ) — 50 мс. Если время ответа на определенный запрос составляет 300 мс, мы можем вычислить Z-оценку для этого запроса:<br />
<img width="206" alt="image" src="https://github.com/Melonber/web_anomaly_algorythms/assets/68331365/2e66d607-8171-454f-9156-803f9525cd11"><br />
Это означает, что время ответа на запрос находится на 2 стандартных отклонения выше среднего, что может быть признаком аномалии.

Концепция системы обнаружения аномалий
Для создания простой системы обнаружения аномалий на основе Z-оценки для веб-сервиса, нам потребуются следующие компоненты:

Сбор данных: Непрерывный мониторинг времени ответа веб-сервиса для каждого запроса.<br />
Анализ данных: Регулярный расчет среднего времени ответа и стандартного отклонения на основе собранных данных.<br />
Определение порога Z-оценки: Установление порога Z-оценки, выше которого значения будут считаться аномальными. Например, 
∣Z∣>2 (более двух стандартных отклонений от среднего).<br />
Оповещение: Система должна уведомлять операторов или автоматически принимать меры при обнаружении аномалии.<br/>

<h2>Метод на основе пороговых значений(Threshold-based method)</h2>
один из самых простых и часто используемых методов для обнаружения аномалий. Этот метод заключается в установлении фиксированных порогов, которые определяют границы "нормального" поведения. Значения, выходящие за эти границы, считаются аномальными.<br/>
<h3>Пример метода:</h3>
Допустим, у нас есть веб-сервис, и мы хотим мониторить загрузку процессора (CPU) на сервере. Нормальная работа сервера предполагает, что загрузка CPU не должна превышать 85% в течение длительного времени. Соответственно, мы можем установить пороговое значение на уровне 85%. Все, что выше этого значения, будет считаться аномалией, указывающей на потенциальные проблемы с производительностью или стабильностью системы.
<h3>Реализация:</h3>
Код анализирует данные о загрузке CPU и выявляет случаи, когда загрузка превышает установленный порог в 85%. Каждый такой случай рассматривается как потенциальная аномалия, требующая дальнейшего рассмотрения или вмешательства.
Методы на основе пороговых значений просты в реализации и понимании, но они требуют тщательного выбора пороговых значений и могут не учитывать сложности данных или изменения в поведении системы со временем. Поэтому важно регулярно пересматривать и корректировать пороговые значения, особенно в динамично изменяющихся условиях.

<h2>Метод на основе квантилей (Quantile-based method)</h2>
В статистике квантили являются точками или значениями, которые разделяют ранжированный набор данных на равные части. В контексте обнаружения аномалий и анализа данных, квантили помогают определить границы "нормального" поведения данных, выход за которые может указывать на аномалии или необычные наблюдения. Метод на основе квантилей для обнаружения аномалий в данных работает путем определения значений, которые находятся за пределами заданных квантильных интервалов. Этот метод особенно полезен для идентификации экстремальных значений в данных, которые могут указывать на аномалии.
<h3>Пример</h3>
Представим, что у нас есть данные о времени загрузки веб-страницы. Мы хотим обнаружить случаи, когда время загрузки аномально высоко или низко. Используя метод на основе квантилей, мы можем определить аномалии, установив квантили, например, 5% и 95%. Значения времени загрузки, которые находятся за пределами этих квантилей, будут считаться аномальными.
В этом примере мы сначала генерируем искусственные данные, имитирующие время загрузки веб-страницы. Затем мы используем функцию np.quantile для определения нижнего (5%) и верхнего (95%) квантилей этих данных. Любые значения за пределами этих квантилей считаются аномальными. Этот метод позволяет нам идентифицировать как необычно низкие, так и необычно высокие времена загрузки, которые могут указывать на проблемы с производительностью сайта или его доступностью.
<h3>Шаги:</h3>
Расчет квантилей для набора данных, например, 5-го и 95-го перцентилей времени загрузки веб-страниц.<br/>
Определение значений, которые выходят за пределы этих квантилей, как аномальных.<br/>
Анализ аномальных значений для выявления потенциальных проблем с производительностью сайта или его инфраструктурой.

<h2>Авторегрессионная модель(AR)</h2>
Авторегрессионная модель (AR) является одним из классических подходов к анализу временных рядов. Она предсказывает будущие значения на основе предыдущих наблюдений самого ряда. Модель AR(p) определяется как линейная комбинация p предыдущих значений временного ряда.

Пример использования авторегрессионной модели (AR) Допустим, мы хотим анализировать и предсказывать загрузку CPU на сервере, используя авторегрессионную модель. На основе исторических данных о загрузке CPU мы можем построить модель AR, которая поможет нам предсказать будущую загрузку.
Для этого мы можем использовать библиотеку statsmodels в Python, которая предоставляет широкие возможности для моделирования временных рядов.
<h3>Шаги:</h3>
Сбор и подготовка данных: Предположим, у нас есть временной ряд загрузки CPU за последние n минут.<br/>
Определение порядка модели (p): Используем методы, такие как критерий Акаике (AIC), для определения оптимального значения p.<br/>
Построение и обучение модели AR: Используем исторические данные для обучения модели.<br/>
Прогнозирование: Используем модель для прогнозирования будущей загрузки CPU.<br/>

<h1>Машинное обучение</h1>
<h2>Изолирующий лес (Isolation Forest)</h2>
Изолирующий лес (Isolation Forest) — это алгоритм обучения без учителя, используемый для обнаружения аномалий. Он основан на принципе изоляции аномалий путем случайного выбора признака и случайного разделения значения признака до тех пор, пока не будут изолированы отдельные точки данных. Аномалии обычно легче изолировать, чем нормальные точки данных, что делает этот метод эффективным для выявления аномальных наблюдений.
<h3>Пример применения:</h3> Обнаружение резких пиков трафика на веб-сервере, которые могут указывать на DDoS-атаки или другие аномальные ситуации.
<h3>Шаги:</h3>
Сбор данных о трафике веб-сервера.<br/>
Обучение модели изолирующего леса на данных трафика, указав ожидаемую пропорцию аномалий через параметр contamination.<br/>
Применение обученной модели к новым данным для идентификации потенциальных аномалий.<br/>
Анализ выявленных аномалий для определения их причин и возможного воздействия на систему.<br/>

<h2>Кластеризация (K-средних, DBSCAN)</h2>
Кластеризация — это метод машинного обучения без учителя, который используется для группировки объектов на основе их сходства. Два популярных алгоритма кластеризации — K-средних (K-means) и DBSCAN (Density-Based Spatial Clustering of Applications with Noise) — имеют различные подходы к определению кластеров.
DBSCAN отлично подходит для идентификации аномалий в данных благодаря своей способности находить кластеры произвольной формы и выделять выбросы как шум.
<h3>Пример применения:</h3>
Идентифицикация аномальных паттернов трафика, такие как необычно высокое или низкое количество посещений, которые могут указывать на технические проблемы или атаки на веб-сайт.
<h3>Шаги:</h3>
Сбор и предобработка данных: Аналогично подготовить данные о трафике веб-сайта.<br/>
Применение DBSCAN:<br/>
Выбрать параметры eps (максимальное расстояние между двумя точками для считывания их соседями) и min_samples (минимальное количество точек в окрестности точки для считывания её центральной точкой кластера) <br/>
Применение DBSCAN для кластеризации данных. Точки, не принадлежащие ни к одному кластеру, будут классифицированы как шум и могут рассматриваться как аномалии.

<h1>Глубокое обучение</h1>
<h2>Автоэнкодеры</h2>
это тип нейронных сетей, используемых для обучения эффективному представлению данных (кодированию), обычно с целью уменьшения размерности или для обнаружения аномалий. Автоэнкодеры состоят из двух частей: кодировщика, который сжимает входные данные в более маленькое представление, и декодера, который пытается восстановить исходные данные из этого сжатого представления. При обнаружении аномалий автоэнкодеры обучаются на "нормальных" данных, и ожидается, что они будут плохо восстанавливать аномальные данные, что позволяет их выявить.
<h3>Пример:</h3>
Обнаружения аномалий в данных логов операций веб-сервиса. Аномалии в логах могут указывать на необычные или подозрительные действия, такие как ошибки в работе сервиса, неавторизованный доступ или внутренние сбои системы.<br/>
Предположим, у нас есть набор данных логов, который включает различные метрики, такие как время ответа сервера, коды состояния HTTP, объем переданных данных, IP-адреса пользователей и типы запросов.
<h3>Шаги реализации</h3>
Предобработка данных
Преобразование категориальных переменных (например, кодов состояния HTTP и типов запросов) в числовые с помощью one-hot encoding.
Нормализация числовых переменных (например, времени ответа сервера и объема переданных данных).
<br/>
Разработка автоэнкодера:
Кодировщик: Сжатие данных логов в более маленькое представление.
Декодер: Попытка восстановить исходные данные из сжатого представления.
Архитектура автоэнкодера должна быть адаптирована к специфике данных.
<br/>
Обучение автоэнкодера:
Использование нормальных данных логов (без аномалий) для обучения автоэнкодера.
Минимизация ошибки реконструкции.
<br/>
Обнаружение аномалий:
Применение обученного автоэнкодера к новым данным логов.
Использование ошибки реконструкции для идентификации записей, которые сильно отличаются от "нормальных" и могут считаться аномальными.



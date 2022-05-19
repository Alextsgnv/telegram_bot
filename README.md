<h3>Телеграм бот прогнозирования тематики новостей</h3>
<hr>
<br>
<h4>Задачи по реализации проекта</h4>
<p>1. Найти корпус данных для обучения</p>
<p>2. Обработать полученные данные</p>
<p>3. Определится с моделью обучения</p>
<p>4. Оценить точность модели</p>
<p>5. Реализловать телеграм бота, реализующего прогноз тематики с использованием модели</p>
<br>
<h4>Корпус данных</h4>
<br>
<p>В качестве данных был взят корпус новостей информационного портала <a href = 'https://www.kaggle.com/datasets/yutkin/corpus-of-russian-news-articles-from-lenta'>Lenta.ru</a>. Этот датасет содержит более 800 тысяч новостей с 1999 по 2019 годы</p>
Для предсказания используется модель логистической регресси, предварительно обученая на корпусе новостей и информационного портала Lenta.ru? собранный в период с 1999 по 2019 годы.Класс тем модели: Россия, Мир, Экономика, Спорт, Культура, Наука и техника, Интернет и СМИ, Бывший СССР, Из жизни, Дом, Силовые структуры, Украина, Ценности, Бизнес, Путешествия.

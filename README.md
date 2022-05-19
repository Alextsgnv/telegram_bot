<h3>Телеграм бот прогнозирования тематики новостей</h3>
<hr>

<h4>Задачи по реализации проекта</h4>
<p>1. Найти корпус данных для обучения</p>
<p>2. Обработать полученные данные</p>
<p>3. Определится с моделью обучения</p>
<p>4. Оценить точность модели</p>
<p>5. Реализловать телеграм бота, реализующего прогноз тематики с использованием модели</p>
<h4>Корпус данных</h4>
<p>В качестве данных был взят корпус новостей информационного портала <a href = 'https://www.kaggle.com/datasets/yutkin/corpus-of-russian-news-articles-from-lenta'>Lenta.ru</a>. Этот датасет содержит более 800 тысяч новостей с 1999 по 2019 годы. Возможные тематики: Россия, Мир, Экономика, Спорт, Культура, Наука и техника, Интернет и СМИ, Бывший СССР, Из жизни, Дом, Силовые структуры, Украина, Ценности, Бизнес, Путешествия.</p>
<h4>Обработка данных</h4>
<p>Так как цель состояла именно в решении задачи как задичи классификации текста, в качестве основных признаков были выбраны "Заголовок статьи" и "Текст статьи".
Данные признаки объединялис в один общий признак, после чего с ними производились следующие манипуляции:</p>
<p>1. Приведение признака в нижний регистр.</p>
<p>2. Удаление символов пунктуации.</p>
<p>3. Удаление цифр.</p>
<p>4. Удаление url адресов.</p>
<p>5. Удаление множественных пробелов.</p>
<p>6. Удаление стоп-слов.</p>
<p>7. Стемминг.</p>
<p>8. Удаление одиночных символов.</p>
<p>После даннных операций к тексту применялся алгоритм TfIdf, определяющий частотную зависимость слова в сэмпле и во всем корпусе. На полученном признаковом пространстве была обучена логистическая регрессия с l1 регулязаторм, выступившая функцией понижения размерности. После чего были отобраны конечные признаки для будущего обучения моделей.</p>
<h4>Модель обучения</h4>
<p>В качестве основной модели была выбрана логистическая регрессия с l2 регулязатором на признаках полученных при обучении логистической регрессии с l1 регуляризатором. Модель была выбрана за счет своей быстрой сходимости и достаточно высокой точности.</p>
<h4>Оценка модели</h4>
<p>Для оценки модели былт выбраны метрики precision и recal. В среднем precision и recal для всех классов не опускаютс ниже 0.68.</p>
<h4>Реализация телеграм бота</h4>
<p>Телеграм бот реализован с использованием библиотеки aiogram.</p>
<p>Ссылка на бота <a href ='t.me/news_alex_bot'>Бот.</p>

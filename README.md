# О проекте

Проект написан в рамках обучения, на площадке [dvmn.org](https://dvmn.org/), модуля [django orm](https://dvmn.org/modules/django-orm/lesson/correcting-grades/#1)

По условиям задания некий Ваня попросил написать для него скрипт, который будет исправлять плохие оценки и подчищать плохие отзывы от учителей.

Проект django, а именно электронный дневник лежит [тут](https://github.com/devmanorg/e-diary/tree/master)

В скрипте лежат четыре функции
1. `catch_exception(function_name, *args)` - отлавливает ошибки при запросе к базе. Ожидает в качестве аргумента, одну из функций ниже, и позиционные аргументы.
2. `fix_marks("Имя Фамилия учащегося")` - позволяет заменить все плохие оценки на пятерки. В качестве аргумента ожидает имя ученика.
3. `create_commendation("Имя Фамилия учащегося", "Название предмета")` - функция, добавляет хорошие отзывы. В качестве аргумента ожидает имя ученика и название предмета.
4. `delete_chastisement("Имя Фамилия учащегося")` - функция удаляет все плохие отзывы, оставленные учителями. В качестве аргумента ожидает имя ученика.

### Пример запуска:

```python
catch_exception(fix_marks, "Имя фамилия") 
```

Пример выполнения скрипта:
[![imageup.ru](https://imageup.ru/img7/4179995/example.gif)](https://imageup.ru/img7/4179995/example.gif.html)


### Как подготовить проект

- Скачать основной проект электронного дневника, лежит [тут](https://github.com/devmanorg/e-diary/tree/master);
- Добавить в проект базу данных дневника, можно скачать [тут](https://dvmn.org/filer/canonical/1562234129/166/) или подключить свою базу;
- Добавить скрипт из этого репозитория в папку с проектом рядом с `manage.py`.

## Требования к окружению

Python3 должен быть уже установлен.
Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```python
pip install -r requirements.txt
```
***

# hacks_tools

## Описание для Вани

[![imageup.ru](https://imageup.ru/img223/4178540/red-matrix-5031496_1920-1078x516.jpg)](https://imageup.ru/img223/4178540/red-matrix-5031496_1920-1078x516.jpg.html)

***

## Как подключить скрипт

### 1. Положить скрипт в папку с проектом `e-diary`

[![imageup.ru](https://imageup.ru/img28/4180042/explorer_1jmboowrvs.png)](https://imageup.ru/img28/4180042/explorer_1jmboowrvs.png.html)

### 2. Запустим терминал и пропишем следующую команду:


- _Команда `python manage.py shell`_ включит программу, которая позволит подключиться к базе данных и использовать инструменты из нашего скрипта 😈

```python
python manage.py shell
```
[![imageup.ru](https://imageup.ru/img77/4179807/shell.gif)](https://imageup.ru/img77/4179807/shell.gif.html)

### 3. Подключимся к нашей базе данных.
Для этого в терминале пропишем:
```python
from datacenter.models import * 
```
[![imageup.ru](https://imageup.ru/img108/4179831/db.gif)](https://imageup.ru/img108/4179831/db.gif.html)


### 4. Подключаем инструменты скрипта🍄🍄🍄.
```python
from scripts import *   
```
[![imageup.ru](https://imageup.ru/img288/4179940/tools.gif)](https://imageup.ru/img288/4179940/tools.gif.html)


Что бы проверить что всё получилось, набери в терминале
```python
fix_marks 
```
В ответ получим ответ как на картинке. Значит скрипт подключен и можно приступать.
[![imageup.ru](https://imageup.ru/img22/4180055/pycharm64_sdbxsgvg9x.png)](https://imageup.ru/img22/4180055/pycharm64_sdbxsgvg9x.png.html)
 
***

## Инструменты скрипта:

1. `catch_exception` - основной инструмент нашего скрипта, через него запускаются все остальные инструменты.
2. `fix_marks("Имя Фамилия учащегося")` - позволяет заменить все плохие оценки на пятерки. В скобках необходимо указать имя ученика. Обрати внимание, что имя должно быть в кавычках.
3. `create_commendation("Имя Фамилия учащегося", "Название предмета")` - инструмент добавляет хорошие отзывы. В скобках, через запятую, необходимо указать имя ученика и название предмета. Обрати внимание, что имя и название предмета должно быть в кавычках.
4. `delete_chastisement("Имя Фамилия учащегося")` - этот инструмент удаляет все плохие отзывы, оставленные учителями. 

Пример использования:

`Наш основной инструмент(название инструмента, "Имя ученика", "Название предмета")` - название предмета добавляется только для - `create_commendation` 

Чтобы исправить плохие оценки, использую следующую команду:
```python
catch_exception(fix_marks, "Имя фамилия") 
```

Чтобы удалить плохие отзывы, использую команду:

```python
catch_exception(delete_chastisement, "Имя фамилия") 
```

Чтобы добавить хорошие отзывы, использую команду:

```python
catch_exception(create_commendation, "Имя фамилия", "Название предмета") 
```

Доказательство работы
[![imageup.ru](https://imageup.ru/img7/4179995/example.gif)](https://imageup.ru/img7/4179995/example.gif.html)

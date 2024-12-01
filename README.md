# МТС Hack & Change
## Трек Web/DA: Сервис визуализации организационной структуры от МТС

Нами было разработано MVP веб-приложения для визуализации организационной структуры компании, которое поможет пользователям легко ориентироваться и находить сотрудников по косвенным признакам, не зная их точного имени или места в иерархии.<br></br>
Поиск сотрудников можно осуществлять с помощью:
 - Фильтров, расположенных в левой части экрана;
 - Поисковой строки в центре экрана, запрос из которой будет направляться в обученную модель.

В корне проекта расположены четыре ключевые директории. Первые три, backend-for-frontend, employees и ml-searcher хранят в себе код трех сервисов, последняя - client содержится клиентская составляющая продукта.
Файл docker-compose.yml необходим для сборки и запуска всей системы.

## Как это запустить?
Для начала необходимо создать файлы с переменными окружения. Файлы для тестового запуска можно скачать по ссылке https://drive.google.com/drive/folders/1Tg-bfYzENQhIUFTE8DLxHmLVLtgfkkaY?usp=sharing.
.env необходимо положить в папку client, а все остальные в environment в корне проекта. <br></br>

Для запуска приложения должен быть заранее установлен docker. Команда для запуска: 
```
docker-compose up --build
```
Так как предполагается, что приложение будет тестироваться на локальном устройстве, то попасть на страницу веб-приложения можно по адресу http://localhost


Загруженная на сервер версия приложения хранится по адресу: http://188.120.225.145/
Ссылка на видео-демонстрацию функционала веб-приложения: https://drive.google.com/file/d/13goLDWiGzCMYFcPCm8S86MIj1t8lCq4f/view?usp=drive_link


### Created by ChillGuys
Подлипалин Виктор (tg @flainberg) - UI/UX Дизайнер <br>
Морев Алексей (tg @Balex777) - Frontend разработчик <br>
Шкитырь Константин (tg @freddiy_jey) - Backend разработчик/DevOps <br>
Мацегора Дмитрий (tg @qiisqwww) - Backend разработчик/капитан команды <br>
Ерофеев Олег (tg @OlegErofeev1) - ML разработчик <br>

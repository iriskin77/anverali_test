

## Описание

#### Необходимо написать программу, которая будет: 

+ [x] получать данные контакта (ID, Имя) из Битрикс24 по Webhook; 
+ [x] проверять имя контакта на наличие его в БД (PostgreSQL);
+ [x] для женских имен таблица names_woman, для мужских имен таблица names_man;
+ [x] далее, если нашел имя в БД мужчин ставить пол "Мужчина", если нашел имя в БД женщин ставить "Женщина";
+ [x] далее передавать данные по гендеру обратно в контакт по ID;

#### Список использованных технологий

+ FastApi
+ Uvicorn
+ Django, Django-ORM
+ PostgreSQL
+ Docker, docker-compose

## Как запустить

+ Клонировать репозиторий: git clone https://github.com/iriskin77/anverali_test/
+ Запустить из Docker: 
  + docker-compose build
  + docker-compose up
+ После этого приложение будет доступно на порту: http://localhost:8000/
+ Воспользоваться django-admin можно по адресу: http://localhost:8000/django/admin
+ Перед тем, как воспользоваться django-admin, следует создать superuser
  + Войти в docker контейнер: docker exec -it <container_id> bash
  + Создать superuser: python3 manage.py createsuperuser

Palta weather
-

**Backend**: Реализовать микро-сервис, который на вход получает в качестве параметра
название города.

- Требование по HighLoad: микро-сервис должен легко масштабироваться (Docker).
- Использовать API Yandex Погода с определенной периодичностью, получать данные от
  Yandex.
- Требование к частоте обновления данных: раз 5/10/более минут (в качестве параметров
  микро-сервиса можно выставить в бэкенде).
- Результаты периодического опроса источника данных микро-сервисом необходимо сохранить
  в любую OLTP базу данных и в дальнейшем использовать для фронтенда.

**Frontend**: Реализовать простой интерфейс в виде графика погоды по выбранному городу.


Requirements
-
`Docker`

Usage
-

**Example:** Run app with default settings (Moscow):
```shell
docker-compose build
docker-compose up
```

Open http://0.0.0.0:5000/

**... or specify host env values:**

- **PORT:** To run app at.
- **APP_NAME:** `App name` to display in app.
- **COORD:** `City coords` to send to Yandex API.
- **SCHEDULE:** `Weather update interval`, in seconds.

**Example:** Run app with Tomsk city settings:
```shell
docker-compose build
PORT=5001 APP_NAME="tomsk" COORD="56.484645,84.947649" SCHEDULE=10 docker-compose up
```

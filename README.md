# Разворачиваем (kafka + spark + jupyter) в докер-контейнере

## О проекте
Целью проекта является развернуть локальную среду для работы со стриминговыми данным(проводится эмуляция стриминга):
 - **Kafka** - брокер сообщений
 - **Spark** (1 мастер + 2 воркера) - распределенные вычисления
 - **Jupyter Notebook** - удобная среда для написания и запуска PySpark кода

Все сервисы запускаются с помощью 'docker-compose'.

---

## Стек технологий
 - Docker & Docker-compose
 - Apache Kafka 3.6.1
 - Apache Zookeeper 3.9.2
 - Apache Spark 3.5.0 (Bitnami image)
 - Jupyter Notebook (pyspark-notebook)

## Структура проекта
```bash
.
├── docker-compose.yml       # Конфигурация сервисов
├── app/                     # Spark-приложения
│   └── example.py
├── notebooks/               # Jupyter ноутбуки
│   └── example.ipynb
└── README.md                # Этот файл :)



Преждем всего нужно создать топик куда кафка будет отправлять данные 
$ docker exec -it kafka kafka-topics.sh --bootstrap-server localhost:9092 --create --topic csv-data

1. Проверьте детали каждого топика
bash# Информация о топике kafka
docker exec -it kafka kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic kafka

# Информация о топике csv-data
docker exec -it kafka kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic csv-data

# __consumer_offsets - системный топик, можно пропустить
2. Проверьте количество сообщений в топиках
bash# Проверьте offset для kafka топика
docker exec -it kafka kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic kafka

# Проверьте offset для csv-data топика
docker exec -it kafka kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic csv-data

3. Попробуйте прочитать топик csv-data
bash# Скорее всего в csv-data есть данные
docker exec -it kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic csv-data --from-beginning --max-messages 10

4. Или прочитайте топик kafka
bash# Проверьте топик kafka
docker exec -it kafka kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic kafka --from-beginning --max-messages 5
5. Если топики пустые, отправьте тестовое сообщение

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
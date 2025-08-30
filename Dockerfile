FROM jupyter/pyspark-notebook:latest

# Устанавливаем дополнительные библиотеки
RUN pip install --no-cache-dir kafka-python pandas

COPY ./notebooks /home/jovyan/work

# Указываем рабочую директорию
WORKDIR /home/jovyan/work

# Запуск Jupyter
CMD ["start-notebook.sh", "--NotebookApp.token=''"]

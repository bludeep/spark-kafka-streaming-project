FROM jupyter/pyspark-notebook:latest

# Устанавливаем дополнительные библиотеки
RUN pip install --no-cache-dir kafka-python pandas streamlit plotly psycopg2-binary sqlalchemy

# Указываем рабочую директорию
WORKDIR /home/jovyan/work

# Запуск Jupyter
CMD ["start-notebook.sh", "--NotebookApp.token=''"]

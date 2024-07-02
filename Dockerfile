# Используем официальный образ Python в качестве базового
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы requirements.txt в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . /app/

# Открываем порт 8000 для доступа к Django серверу
EXPOSE 8000

# Выполняем команду для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

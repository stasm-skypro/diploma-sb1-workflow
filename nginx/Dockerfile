FROM nginx:latest

# Установим netcat
RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

# Копируем конфигурацию и скрипты
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/wait-for.sh /wait-for.sh
RUN chmod +x /wait-for.sh

COPY html/ /usr/share/nginx/html/

EXPOSE 80

# Ждём web, затем запускаем nginx
CMD ["/wait-for.sh", "web", "8000", "nginx", "-g", "daemon off;"]

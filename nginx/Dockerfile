FROM nginx:latest

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/wait-for.sh /wait-for.sh
RUN chmod +x /wait-for.sh

COPY html/ /usr/share/nginx/html/

EXPOSE 80

CMD ["/wait-for.sh", "web", "8000", "nginx", "-g", "daemon off;"]

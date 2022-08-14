FROM ubuntu:latest

LABEL maintainer="Ruslan Potekhin <potekhin.ruslan@gmail.com>"

COPY --chmod=777 start.sh /

RUN apt-get update && apt install -y httrack nginx

COPY default /etc/nginx/sites-available/default

# Expose the port for access
EXPOSE 80/tcp

# Run the Nginx server
CMD ["bash", "/start.sh"]
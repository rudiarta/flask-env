FROM nginx:1.17.3-alpine

RUN apk update && \
    apk add nmap
ADD nginx.conf /etc/nginx/
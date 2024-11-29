FROM nginx:1.27.2-alpine-slim

RUN apk add --no-cache curl

RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/
COPY certificate.crt /etc/nginx
COPY private.key /etc/nginx

CMD ["nginx", "-g", "daemon off;"]
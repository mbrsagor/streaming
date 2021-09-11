#base image
FROM nginx:latest
#remove nginx default
RUN rm /etc/nginx/conf.d/default.conf
#added new new default conf
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
# COPY certs /etc/nginx/certs/

CMD ["nginx", "-g", "daemon off;"]
FROM nginx:1.14
# 设置时区
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY conf/nginx.conf /etc/nginx/nginx.conf
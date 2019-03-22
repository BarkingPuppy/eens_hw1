FROM nginx:1.14
# 设置时区
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# 复制配置
COPY conf/nginx.conf /etc/nginx/nginx.conf
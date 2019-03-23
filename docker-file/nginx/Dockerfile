FROM nginx:1.14

# 設定伺服器的時區
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 將nginx的設定檔複製到container中
COPY conf/nginx.conf /etc/nginx/nginx.conf
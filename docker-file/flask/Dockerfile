FROM python:3-slim

# 設定網站的時區
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 設定程式的工作路徑
RUN mkdir -p /home/web
WORKDIR /home/web

# 安裝程式需要的套件，列在requirements.txt中
ADD requirements.txt  /home/web/requirements.txt
RUN pip3 install -r requirements.txt

# 使用gunicorn啟動app，並發布在port 5000上
CMD gunicorn -w 4 -b 0.0.0.0:5000 run:app
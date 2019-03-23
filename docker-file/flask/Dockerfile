FROM python:3-slim
# 设置时区
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 设置工作区
RUN mkdir -p /home/web
WORKDIR /home/web
# 添加依赖
ADD requirements.txt  /home/web/requirements.txt
RUN pip3 install -r requirements.txt

# 使用gunicorn启动应用
CMD gunicorn -w 4 -b 0.0.0.0:5000 run:app
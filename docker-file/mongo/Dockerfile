FROM mongo
ENV SETUP_DIR /docker-entrypoint-initdb.d
ENV WORKDIR /usr/local/work
RUN mkdir -p $WORKDIR
ADD ./setup.sh $SETUP_DIR/
EXPOSE 27017
RUN chmod 777 $SETUP_DIR/setup.sh
# RUN $SETUP_DIR/setup.sh

FROM httpd:alpine3.16
RUN apk add python3 py3-pip
COPY index.html /usr/local/apache2/htdocs/
COPY favicon.ico /usr/local/apache2/htdocs/
COPY sup /usr/local/apache2/htdocs/
COPY the_daily_christorian.* /usr/local/apache2/htdocs/
COPY reset.sh /usr/local/apache2/htdocs/
COPY templates/rss.xml /usr/local/apache2/htdocs/
RUN mkdir /usr/local/apache2/htdocs/templates
RUN mkdir /usr/local/apache2/htdocs/daily_chris_chan
ADD templates/ /usr/local/apache2/htdocs/templates
ADD requirements.txt /
ADD crontab /
RUN cat /crontab >> /etc/crontabs/root
RUN pip3 install -r /requirements.txt
EXPOSE 80

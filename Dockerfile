FROM xqdocker/ubuntu-nginx
MAINTAINER Nick Krichevsky<nick@ollien.com>

RUN add-apt-repository ppa:certbot/certbot
RUN apt-get update && apt-get install -y python-certbot-nginx supervisor cron
RUN echo "0 0 * * SUN root certbot renew" > /etc/cron.d/crontab
RUN rm /etc/nginx/conf.d/default.conf
COPY certbot.py /certbot.py
COPY nginx_listener.py /nginx_listener.py
COPY supervisord/* /etc/supervisor/conf.d/

CMD /usr/bin/supervisord

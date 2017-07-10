FROM xqdocker/ubuntu-nginx
MAINTAINER Nick Krichevsky<nick@ollien.com>

RUN add-apt-repository ppa:certbot/certbot
RUN apt-get update && apt-get install -y python-certbot-nginx supervisor
RUN rm /etc/nginx/conf.d/default.conf
COPY certbot-config.json /certbot-config.json
COPY certbot.py /certbot.py
COPY nginx_listener.py /nginx_listener.py
COPY supervisord/* /etc/supervisor/conf.d/

CMD /usr/bin/supervisord

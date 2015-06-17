FROM python:2.7.9

RUN apt-get -y update \
	&& apt-get -y install python-pip supervisor nginx \
	&& apt-get autoremove -y \
	&& apt-get clean \
	&& rm /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default /etc/nginx/nginx.conf

COPY . /hornet

WORKDIR /hornet

ADD dockerfiles/settings_local.py hornet/settings_local.py

RUN pip install -r requirements.pip \
	&& python manage.py migrate \
	&& python manage.py collectstatic --noinput

ADD dockerfiles/nginx.conf /etc/nginx/nginx.conf
ADD dockerfiles/supervisord.conf /etc/supervisord.conf
ADD dockerfiles/hornet.supervisor.conf /etc/supervisor/conf.d/hornet.conf
ADD dockerfiles/hornet.nginx.conf /etc/nginx/conf.d/hornet.conf
ADD dockerfiles/supervisor.upstart.conf /etc/init/supervisor.conf
ADD dockerfiles/init.sh /init.sh

EXPOSE 80 2000

CMD ["/bin/bash", "/init.sh"]
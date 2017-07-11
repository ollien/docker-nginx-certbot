# NGINX/Certbot Docker Image

A Docker container that runs certbot and nginx together in order to provide support for Let's Encrypt. Supports autorenewal.

## Installation
1. Pull the container from Docker Hub.

	`docker pull ollien:nginx-certbot`
2. Edit your `certbot-config.json` according to the configuration guidelines below.

3. Start the Docker container.

	````
		docker run \
		-v /path/to/nginx0config:/etc/nginx/conf.d/default.conf \
		-v /path/to/certbot-config.json:/certbot-config.json \
		-p 80:80 \
		-p 443:443 \
		ollien:nginx-certbot
	````


## Configuration
All containers require a `certbot-config.json`. This file must be in JSON format with the following format.

| Key        | Usage                                                                       |
|------------|-----------------------------------------------------------------------------|
| account_id | Your Let's Encrypt account id. Cannot be used in pair with `email`.         |
| email      | Your Let's Encrypt email address. Cannot be used in pair with `account_id`. |
| domains    | An array of the domains you wish to register with Let's Encrypt.            |

## License
MIT

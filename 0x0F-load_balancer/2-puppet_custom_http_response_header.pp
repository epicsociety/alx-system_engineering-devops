# add-header
file { 'Nginx server config file':
  ensure => file,
  path   => '/etc/nginx/sites-available/default',
  mode   => '0744',
  owner  => 'www-data',
  content =>
"server {
			listen 80 default_server;
			listen [::]:80 default_server;
			root /var/www/html;
			index index.html index.htm index.nginx-debian.html;
			server_name _;
			error_page 404 /custom_404.html;
			location /custom_404.html {
					root /var/www/error;
					internal;
					add_header X-Served-By \$hostname;
			}
			location / {
					try_files \$uri \$uri/ =404;
					add_header X-Served-By \$hostname;
			}
			location /redirect_me/ {
					rewrite ^(.*)$ http://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
					add_header X-Served-By \$hostname;
			}
}"
}

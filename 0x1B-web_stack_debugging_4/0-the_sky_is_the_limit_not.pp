# Contents of the Puppet manifest file used to fix the issue
# Example Puppet manifest file for fixing Nginx configuration

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => "
    user www-data;
    worker_processes auto;
    pid /run/nginx.pid;

    events {
      worker_connections 1000; # Adjusted to handle 1000
				#requests with 100 at a time
      # multi_accept on;
    }

    http {

      ##
      # Basic Settings
      ##

      sendfile on;
      tcp_nopush on;
      tcp_nodelay on;
      keepalive_timeout 65;
      types_hash_max_size 2048;

      server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
          try_files ${uri} ${uri}/ =404;
        }
      }
    }
  ",
}

# Reload Nginx to apply the changes
service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/nginx/nginx.conf'],
}

# 2-puppet_custom_http_response_header.pp

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Define a custom fact to retrieve the hostname
$hostname = $facts['hostname']

# Configure Nginx with custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name _;

        location /hbnb_static {
            alias /data/web_static/current/;
        }

        add_header X-Served-By $hostname;

        location / {
            proxy_pass http://localhost:5001;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
  ",
  notify  => Service['nginx'],
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Restart Nginx after configuration changes
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

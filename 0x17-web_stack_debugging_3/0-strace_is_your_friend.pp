# Ensure Apache package is installed
package { 'apache2':
  ensure => installed,
}

# Fix Apache configuration
file { '/etc/apache2/apache2.conf':
  ensure  => file,
  content => template('apache2/apache2.conf.erb'),
  notify  => Service['apache2'],
}

# Restart Apache service
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/apache2/apache2.conf'],
}

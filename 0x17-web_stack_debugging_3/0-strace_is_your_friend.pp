# Puppet manifest to fix Apache 500 error and ensure correct page is returned

# Ensure Apache package is installed
package { 'apache2':
  ensure => installed,
}

# Fix Apache configuration
file { '/etc/apache2/apache2.conf':
  ensure  => file,
  source  => 'puppet:///modules/apache2/apache2.conf.erb', # Correct the path to the template file
  notify  => Service['apache2'],
}

# Restart Apache service
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/apache2/apache2.conf'],
}

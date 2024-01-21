#!/usr/bin/env bash
# Automating my Tasks using Puppet

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "# SSH client configuration\n
    Host *\n
      IdentityFile ~/.ssh/school\n
      PasswordAuthentication no\n",
}

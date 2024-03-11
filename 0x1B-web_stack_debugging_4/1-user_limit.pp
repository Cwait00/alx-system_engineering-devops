# Contents of the Puppet manifest file used to adjust the open
file limit for the holberton user
# Example Puppet manifest file for adjusting open file limit for a user

exec { 'increase_open_file_limit_for_holberton':
  command => 'ulimit -n 4096',  # Adjust the open file limit as needed
  user    => 'holberton',
}

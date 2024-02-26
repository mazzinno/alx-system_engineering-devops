# using Puppet to make changes to our configuration file
file_line { 'Turn off passwd':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no', }
file_line { 'Declaring identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school', }

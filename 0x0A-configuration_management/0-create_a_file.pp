#this file is.
file { '/tmp/school':
  ensure  => present,
  content => "I love Puppet",
  mode    => '0744',        # Set file permissions
  owner   => 'www-data',        # Set file owner
  group   => 'www-data',        # Set file group
}

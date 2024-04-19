#Change ULIMIT value from 15 to 2000
exec {'/etc/default/nginx':
command  => 'sed -i "s/15/500/g" /etc/default/nginx; sudo service nginx restart',
provider => shell,
}

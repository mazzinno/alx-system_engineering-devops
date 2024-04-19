#Increases limit of open files
exec {'hard-limit':
    command  => 'sed -i "/holberton hard/s/5/10000" /etc/security/limits.conf',
    provider => shell,
}

exec {'soft-limit':
    command  => 'sed -i "/holberton hard/s/4/10000" /etc/security/limits.conf',
    provider => shell,
}

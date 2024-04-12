# incorrect file name
exec{ 'fix-wordpress':
    command => 'sed -i \'s/class-wp-locale.phpp/class-wp-locale.php/g\' /var/www/html/wp-settings.php',
    path    => '/usr/local/bin/:/bin/',
}

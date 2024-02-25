#kills a process called killmenow
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/bin/',
}

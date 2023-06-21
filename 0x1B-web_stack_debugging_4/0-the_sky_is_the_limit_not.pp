# fixing nginx
{ 'nginx-debug':
  command => 'bash',
  unless  => "grep -q '^ULIMIT=\"-n 8192\"' /etc/default/nginx",
  path    => '/usr/bin:/usr/sbin:/bin',
  refreshonly => true,
  subscribe => File['/etc/default/nginx'],
}

file { '/etc/default/nginx':
  ensure  => present,
  content => "ULIMIT=\"-n 8192\"\n",
  notify  => Exec['nginx-debug'],
}

service { 'nginx':
  ensure => running,
  subscribe => File['/etc/default/nginx'],
}

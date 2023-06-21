# possible to login with the holberton user 
exec { 'configuration-for-holberton-user':
  command     => 'sed',
  unless      => "grep -E '^holberton\\s+hard\\s+nofile\\s+88888$' /etc/security/limits.conf && grep -E '^holberton\\s+soft\\s+nofile\\s+88888$' /etc/security/limits.conf",
  path        => '/usr/bin:/usr/sbin:/bin',
  refreshonly => true,
}

file { '/etc/security/limits.conf':
  ensure  => present,
  mode    => '0644',
  content => "holberton hard nofile 88888\nholberton soft nofile 88888\n",
  notify  => Exec['configuration-for-holberton-user'],
}

# installs nginx and configures it
# using curl, nginx must return a page that contains the string "Hello World!"
# handles redirection also

package { 'nginx':
    ensure => installed,
}

file { 'index.html':
    ensure  => present,
    path    => 'var/www/html/index.html',
    content => 'Hello World!'
}

file_line { 'aaaaa':
    ensure => 'present',
    path   => 'etc/nginx/sites-available/default',
    after  => 'listen 80 default_server;',
    line   =>  "rewrite \"^/redirect_me\" \"https://www.youtube.com/watch?v=J---aiyznGQ\" permanent;",
}

service { 'nginx':
    ensure  => running,
    restart => true,
    require => Package['nginx'],
}

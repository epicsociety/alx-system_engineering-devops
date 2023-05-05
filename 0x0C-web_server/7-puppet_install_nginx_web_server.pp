# installs nginx and configures it
# using curl, nginx must return a page that contains the string "Hello World!"
# handles redirection also

package { 'nginx':
    ensure => installed,
}

file { 'index.html':
    ensure  => present,
    path    => 'var/www/html/index.html',
    content => 'Hello World!"
}

nginx::resource::server { 'epicsociety.tech':
    path   => '/etc/nginx/sites-available/default',
    listen_port => '85',
    server_name => 'epicsociety.tech',
    location => [
    {
        location => '/redirect_me',
        rewrite => [
            rewrite "^/redirect_me" "https://www.youtube.com/watch?v=J---aiyznGQ" permanent;',
        ],
    },
    ],
}

service { 'nginx':
    ensure  => running,
    restart => true,
    require => Package['nginx'],
}

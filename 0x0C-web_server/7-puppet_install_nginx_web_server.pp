#automating works using puppet

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
          ensure  => installed,
          require => Exec['update system']
}
exec { 'redirect_me':
       command => 'sed -i "241\ rewrite ^redirect_me https://www.github.com/KisingiMichael permanent;" /etc/nginx/sites-enabled/default',
       provider => 'shell'
}

file { '/var/www/html/index.html':
       content => 'Hello World!'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

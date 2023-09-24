#Client configuration file with Puppet

file {'/etc/ssh/ssh_config':
ensure => present
}

file_line {'Identify file':
ensure => present,
path => '/etc/ssh/ssh_config',
line => 'IdentifyFile ~/.ssh/school'
}

file_line {'password auth':
ensure => present,
path => '/etc/ssh/ssh_config'
line => 'PathwordAuthentication no'
}

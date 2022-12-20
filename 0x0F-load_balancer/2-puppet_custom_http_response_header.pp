# automate the task of creating a custom HTTP header response,
# installing nginx and configure the server with Puppet.

exec {'update':
  command  => 'sudo apt-get -y update',
  provider => shell,
  befor    => Exec['install Nginx'],
}

exec {'install Nginx':
  command  => 'sudo apt-get -y install nginx',
  provider => shell,
  before   => Exec['update header'],
}

exec {'update header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['restart Nginx'],
}

exec {'restart Nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}

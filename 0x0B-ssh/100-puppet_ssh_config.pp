# using Puppet to make changes to our configuration file
# Your SSH client configuration must be configured 
# - to use the private key ~/.ssh/school
# Your SSH client configuration must be configured 
# - to refuse to authenticate using a password

file_line { 'Turn off passwd auth':
  ensure             => 'present',
  path               => '/etc/ssh/ssh_config',
  line               => '    PasswordAuthentication no',
  match              => '^PasswordAuthentication',
  append_on_no_match => true,
}
file_line { 'Declare identity file':
  ensure             => 'present',
  path               => '/etc/ssh/ssh_config',
  line               => '    IdentityFile ~/.ssh/holberton',
  match              => '^IdentityFile',
  append_on_no_match => true,
}

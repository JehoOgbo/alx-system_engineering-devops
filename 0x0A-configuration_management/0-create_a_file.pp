# create a file in tmp directory
file { '/tmp/school':
	ensure => 'file',
	content => "I love Puppet"
	mode => '0744'
	group => 'www-data',
	owner => 'www-data'
}

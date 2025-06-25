file { '~/new.txt':
	ensure => '/tmp/school',
	content => "I love Puppet"
	mode => '0744'
	group => 'www-data',
	owner => 'www-data'
}

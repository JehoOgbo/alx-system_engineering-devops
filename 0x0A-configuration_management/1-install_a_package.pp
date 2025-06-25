# install flask using puppet
# version must be 2.1.0
package { 'Flask' :
  ensure   => '2.1.0',
  provider => 'pip3'
}

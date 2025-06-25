# create a manifest that kills a process named killmenow
# must use the exec puppet resource
# must use pkill
exec { 'killer':
  command  => 'pkill killmenow',
  provider => 'shell'
}

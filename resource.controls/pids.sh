#!/bin/bash

count=10

## test this before and after the steps below 
## sudo mkdir /sys/fs/cgroup/cgrp1
## echo 5 | sudo tee /sys/fs/cgroup/cgrp1/pids.max
## more /sys/fs/cgroup/cgrp1/pids.max
## echo $$ | sudo tee /sys/fs/cgroup/cgrp1/cgroup.procs 

for ((count=1; count<=10; count++)); do
    echo "Sleeping now on count $count"
		sleep 10 &
done

## sudo unshare --user --map-root-user --mount-proc --uts --pid --fork /bin/bash

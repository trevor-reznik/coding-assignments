# Project #1

*Christian P. Byrne*

## Exercise 1

. . . 


## Exercise 2 - ``ssh`, `scp`, and Shell Scripting



#### (a) 

From inside Lectura ssh session:

```
Test 1: I am not inside a Docker container.
Test 2: I am not inside a Docker container.
```

#### (b)

From inside ubuntu container:

```
Test 1: I am inside a Docker container.
Test 2: I am inside a Docker container.
```

#### (c)  

`scp` command used to copy file from Lectura to container:

```bash
# From container shell
scp cbyrne@lectura.cs.arizona.edu:./../russelll/cs346_exercises/proj* .
```


#### (d) 


The shebang line is `#! /bin/bash`, so Linux uses `bash` to execute the script.

#### (e)


##### First Test

- `cat /proc/1/cgroup` read config for control group 1 
- `2>&1` combines stdout and stderr to one stream
- `| grep docker` filters the stream for lines container "docker"
- `$()` interpolate the output into a new string
- if the string is not null, implying that there was an instance the word docker in control group 1's proc file, indicate that we are inside a container

To trick the first condition:
- create a symlink or an alias that would point the cat command to a dummy folder
- create a process named "docker": `bash -c "exec -a docker"`, get the PID of the process: `top | grep docker`, then write the PID to the corresponding `cgroup.procs` file such that the process will be a part of the cgroup as outlined in the man pages for the `cgroup` utility

##### Second Test


- the `-f` primary in the conditional before a path tests if a file exists
- if the the `.dockerenv` file exists in the root directory, then the script will print that you are inside a docker container

To trick the second condition:
- create a file called `.dockerenv` in the root dir: `touch /.dockerenv`

## Exercise 3

`proj01_cbyrne_config_ubuntu`

## Exercise 4


#### (a)

```bash
# In Alpine container, search bin for commands
ls /bin | grep -w 'cat\|curl\|grep\|less\|nano\|python3\|ssh\|telnet\|vi'
```

```
> cat
> grep
```

- `cat`, `grep` - Exists
- `curl`, `less`, `nano`, `python3`, `ssh`, `telnet`, `vi` - Does not exist in bin

#### (b)

It seems that the default shell on alphine is `ash`, and `bash` is not installed as an alternative shell like on macs. This can be confirmed by searching for `bash` in `/bin` and seeing that it is not there. 

The shebang line indicates to use bash as the interpreter, but bash is not installed.

#### (c)

`proj01_cbyrne_config_alpine`

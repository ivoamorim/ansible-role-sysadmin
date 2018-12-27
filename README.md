sysadmin
=========

Installs sysadmin utils packages.
Requirements
------------

None

Role Variables
--------------

**logrotate_scripts**: A list of logrotate scripts and the directives to use for the rotation.

# Install sysstat, dstat, lsof, wide range of top
resource_monitor_packages: boolean

# Install tcpdump, nmap, netcat
network_monitor_packages: boolean

# Install Bash, Zsh
shell_packages: boolean

# Install tmux
terminal_packages: boolean

# Install Emacs, Vim
editor_packages: boolean

Dependencies
------------

None

Example Playbook
----------------
```
- hosts: all
  vars:
    monitor_packages: true
    network_monitor_packages: true
    shell_packages: true
    terminal_packages: true
    editor_packages: true

  roles:
    - role: ivoamorim.logrotate
```

License
-------

BSD

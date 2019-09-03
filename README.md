# kmon Design
# 1. Description:
kmon is tool be used to monitor cpu, mem, network and disk etc. related real time dynamic data and to dump cpu, mem, network and disk etc static data for trouble shooting.

# 2. kmon source code structure
* src: source file used by main kmon 
* lib: module files used by main kmon
* module: plugin module used by main kmon
* conf: configureation file for module used by main kmon (format yaml)
* kmon.py: main function by kmon

# 3. kmon Usage
kmon [OPTION] OBJECT { COMMAND | help}
where OBJECT := { cpu | mem | net | disk }

* Supported COMMAND for each OBJECT:
* * show
* * monitor

Monitor COMMAND Manditory Option:

## 3.1. mon
counter+value

## 3.2. dump (static data dump) ( for example: sysctl -a )
3.2.1: --cpu: cpu related static data dump
3.2.2: --mem: mem related static data dump
3.2.3: --net: network related static data dump
3.2.4: --disk: disk related static data dump
3.2.5: --all: dump cpu, mem, net and disk related static data

# 4. kmon plugin support
Configuration Template

# 5. kmon Collection Data Type
5.1. Dynamic Data
Network:
5.1.1. ip link
5.1.2. netstat
5.1.3. ethtool
CPU:
MEM:
DISK:

5.2. Static Data
5.2.1. Tool
sysctl, /proc
Network:
CPU:
MEM:
DISK:
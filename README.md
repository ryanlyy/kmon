# kmon Design
# 1. Description:
kmon is tool be used to monitor cpu, mem, network and disk etc. related real time dynamic data and to dump cpu, mem, network and disk etc static data for troubleshooting.

# 2. kmon source code structure

# 3. kmon Usage
```
Usage: kmon [OPTION] OBJECT { COMMAND | help}
where OBJECT := { cpu | mem | net | disk }
      OPTION := { --version] }
```

Supported COMMAND for each OBJECT:
* dump
* monitor

Monitor COMMAND Manditory Option:
* --interval: dump data interval 

Monitor COMMAND Optional Option:
* --counter: Performance Data (data incremental in --interval), if no --counter, all counters shall be monitor on this OBJECT
* --duration: Data monitor timer duration 

Minitor COMAMND Other Options:
* OBJECT: cpu
* OBJECT: mem
* OBJECT: net
* OBJECT: disk


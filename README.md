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

## COMMAND
**Manditory COMMAND for each OBJECT:**
* dump
* monitor

**Specific COMMAND for each OBJECT:**
* OBJECT: cpu
* OBJECT: mem
* OBJECT: net
* OBJECT: disk

## Monitor COMMAND Option
**Manditory Option:**
* --interval: data monitor interval 

**Optional Option:**
* --counter: Performance Data (data incremental in --interval), if no --counter, all counters shall be monitor on this OBJECT; multiple --counter shall be supported
* --duration: Data monitor time duration, -f no --duration, monitor is forever
* --output: format supported: csv, if no --output, stdout is used with friendly format

**Specific Options:**
* OBJECT: cpu
* OBJECT: mem
* OBJECT: net
* OBJECT: disk


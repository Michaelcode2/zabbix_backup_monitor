#!/bin/bash

cat '/home/michael/PythonProjects/Zabbix files/BackupTime.txt' | grep "$1" | awk '{print $2}'
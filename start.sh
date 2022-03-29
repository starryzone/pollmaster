#!/bin/bash
ps -ef | grep "python launcher.py" | grep -v grep | awk '{print $2}' | xargs kill -9 
node index.js &
python ipc.py &
python launcher.py
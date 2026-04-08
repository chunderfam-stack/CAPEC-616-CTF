#!/bin/bash

service cron start
python -u /tmp/.update_service.py &
tail -f /dev/null

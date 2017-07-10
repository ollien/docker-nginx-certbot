#!/usr/bin/env python3
import certbot
import sys

while True:
    sys.stdout.write("READY\n")
    sys.stdout.flush()
    raw_header = sys.stdin.readline()
    header = dict([item.split(":") for item in raw_header.split()])
    raw_payload = sys.stdin.read(int(header["len"]))
    payload = dict([item.split(":") for item in raw_payload.split()])
    if payload["processname"] == "nginx":
        certbot.run()
        break
    sys.stdout.write("RESULT 2\n")
    sys.stdout.write("OK")
    sys.stdout.flush()

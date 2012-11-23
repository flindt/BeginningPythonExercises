#!/usr/bin/env python
import subprocess
"""
A ssh based command dispatch system
"""
machines = ["127.0.0.1"]

cmd = "uname"


for machine in machines:
    subprocess.call("ssh root@%s %s" % (machine, cmd), shell=True)

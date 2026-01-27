#!/usr/bin/python3
import os
secrets = os.environ["secrets"]

print("start")
if secrets:
    print("secret found")
else:
    print("no secret found")
print("end")


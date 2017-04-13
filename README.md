# SimpleTextCypher

Simple Plain Text Cypher written in python

When executed, the program creates a Encrypted txt file and a Decrypter python script for that file, each file created has your own decrypter which is generated in the cyphering process

for test:
```sh
$ python encrypter.py [file name] [output file name]
```

- default file name "raw_file.txt"
- default output file name "{current datetime}"

will be generated 2 files:
 - [output file name]
 - [output file name]_decrypter.py
 
The decrypter script shows the file decrypted on console, has only one optional paramether for save the decrypted file
```sh
$ python {output file name}_decrypter.py [--save]
```

<h1>0x04-utf8_validation</h1>
<h1>Resources</h1>
<li><a href="https://intranet.alxswe.com/rltoken/oqFi6P1hNvp9aSuNv---IQ">UTF-8</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/d--jVK8sBSlhkosu7pFzdw">Characters, Symbols, and the Unicode Miracle</a></li>

<h1>Tasks</h1>
<h2>0. UTF-8 Validation</h2>
<p>
Write a method that determines if a given data set represents a valid UTF-8 encoding.
</p>
<p>
Prototype: def validUTF8(data)
</p>
<p>
Return: True if data is a valid UTF-8 encoding, else return False
</p>
<p>
A character in UTF-8 can be 1 to 4 bytes long
</p>
<p>
The data set can contain multiple characters
</p>
<p>
The data will be represented by a list of integers
</p>
<p>
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
</p>
<pre>
carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

carrie@ubuntu:~/0x04-utf8_validation$
</pre>
<pre>
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
</pre>
<b>Repo:</b>

<li>GitHub repository: alx-interview</li>
<li>Directory: 0x04-utf8_validation</li>
<li>File: 0-validate_utf8.py</li>

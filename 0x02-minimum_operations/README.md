<h1>0x02-minimum_operations</h1>
<h2>Tasks</h2>
<h3>0. Minimum Operations</h3>
<p>
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
</p>
<li>Prototype: def minOperations(n)</li>
<li>Returns an integer</li>
<li>If n is impossible to achieve, return 0</li>

<b>Example:</b>
<p>
n = 9
</p>
<p>
H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
</p>
<p>
Number of operations: 6
</p>
<pre>
carrie@ubuntu:~/0x02-minoperations$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$
carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
carrie@ubuntu:~/0x02-minoperations$
</pre>
<b>Repo:</b>

<li>GitHub repository: alx-interview</li>
<li>Directory: 0x02-minimum_operations</li>
<li>File: 0-minoperations.py</li>

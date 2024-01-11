<h1>0x01. Lockboxes</h1>
<h1>Tasks</h1>
<h3>0. Lockboxes</h3>
<p>
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.</p>
<p>
Write a method that determines if all the boxes can be opened.</p>

<li>Prototype: def canUnlockAll(boxes)</li>
<li>boxes is a list of lists</li>
<li>A key with the same number as a box opens that box</li>
<li>You can assume all keys will be positive integers
    <li>There can be keys that do not have boxes</li>
</li>
<li>The first box boxes[0] is unlocked</li>
<li>Return True if all boxes can be opened, else return False</li>
<pre>
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$
</pre>
<pre>
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
</pre>
<b>Repo:</b>

<li>GitHub repository: alx-interview</li>
<li>Directory: 0x01-lockboxes</li>
<li>SFile: 0-lockboxes.py</li>
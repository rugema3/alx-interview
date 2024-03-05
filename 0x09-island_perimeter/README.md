<h1>0x09-island_perimeter</h1>
<p>For the “0. Island Perimeter” project, you will need to apply your knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to solve a geometric problem within a grid context. The goal is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers. Understanding how to navigate and analyze 2D arrays and apply logical operations to determine the conditions for perimeter calculation is crucial for this task.</p>

<h1>Concepts Needed:</h1>
<ol>
<li>2D Arrays (Matrices):
    <ul>
        <li>Accessing and iterating over elements in a 2D array.</li>
        <li>Understanding how to navigate through adjacent cells (horizontally and vertically).</li>
    </ul>
</li>

<li>Conditional Logic:
    <ul>
        <li>Applying conditions to determine whether a cell contributes to the perimeter of the island.</li>
    </ul>
</li>
<li>Counting Techniques:
<ul>
    <li>Developing a method to count the edges that contribute to the island’s perimeter.</li>
</ul>
</li>
<li>Problem-Solving Strategies:
<ul>
    <li>Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.</li>
<ul>
</li>
<li>Python Programming:
<ul>
    <li>Nested loops for iterating over grid cells.</li>
    <li>Conditional statements to check the status of adjacent cells.</li>
</ul>
</li>
<ol>
<h1>Resources:</h1>
<li>Python Official Documentation:
    <li><a href="https://intranet.alxswe.com/rltoken/8SPalOgoGDWQChVbct0p1g">Nested Lists:</a> Understanding how to work with lists within lists in Python.</li>
</li>
<li>GeeksforGeeks Articles:
    <li><a href="https://intranet.alxswe.com/rltoken/IYcYmeVlCfF-F7Szn1fzfQ">Python Multi-dimensional Arrays:</a>A guide to working with 2D arrays in Python effectively.</li>
</li>
<li>TutorialsPoint:
    <li><a href="https://intranet.alxswe.com/rltoken/TZ8UtQaRxN5cFf8c1TB-rw">Python Lists: </a>Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.</li>
</li>
<li>YouTube Tutorials:
    <li><a href="https://intranet.alxswe.com/rltoken/H7SwlI_XYDpwYonNYKXQfg">Python 2D arrays and lists</a></li>
</li>
<p>
By understanding these concepts and utilizing the provided resources, you will be equipped to approach the problem methodically. You’ll need to iterate over the grid, apply logical operations to identify the perimeter of the island, and account for the specific conditions described in the task. This project not only tests your algorithmic thinking but also reinforces your ability to manipulate data structures and apply logical reasoning to solve problems.
</p>


<h1>Tasks</h1>
<b>0. Island Perimeter</b>
<p>
Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:</p>
    <li>grid is a list of list of integers:
        <li>0 represents water</li>
        <li>1 represents land</li>
        <li>Each cell is square, with a side length of 1</li>
        <li>Cells are connected horizontally/vertically (not diagonally).</li>
        <li>grid is rectangular, with its width and height not exceeding 100</li>
    </li>
<li>The grid is completely surrounded by water</li>
<li>There is only one island (or nothing).</li>
<li>The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).</li>
<pre>
guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

guillaume@ubuntu:~/0x09$ 
guillaume@ubuntu:~/0x09$ ./0-main.py
12
guillaume@ubuntu:~/0x09$ 
</pre>
<br>
<b>Repo:</b>

<li>GitHub repository: alx-interview</li>
<li>Directory: 0x09-island_perimeter</li>
<li>SFile: 0-island_perimeter.py</li>

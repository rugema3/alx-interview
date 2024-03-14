<h1>0x0A-primegame</h1>
<p>
For this project, you will need to leverage your understanding of prime numbers, game theory, and algorithm optimization to solve a competitive game scenario. The challenge involves determining the winner of a game based on the strategic removal of prime numbers and their multiples from a set of consecutive integers.
</p>

<h1>Concepts Needed:</h1>
<li>Prime Numbers:
    <li>Understanding what prime numbers are.</li>
    <li>Efficient algorithms for identifying prime numbers within a range.</li>
</li>
<li>Sieve of Eratosthenes:
    <li>An efficient algorithm for finding all prime numbers up to any given limit, which can be particularly useful for this task.</li>
</li>
<li>Game Theory:
    <li>Basic principles of competitive games where players take turns and the concept of optimal play.</li>
    <li>Understanding win conditions and strategies that lead to a win or loss.</li>
</li>
<li>Dynamic Programming/Memoization:
    <li>Using previous results to make future calculations faster, potentially necessary for optimizing the solution for multiple rounds of the game.</li>
</li>
<li>Python Programming:
    <li>Loops and conditional statements for implementing game logic and algorithms.</li>
    <li>Arrays and lists for storing the integers and tracking removed numbers.</li>
</li>
<h1>Resources:</h1>
<li>Prime Numbers and Sieve of Eratosthenes:
    <li><a href="https://intranet.alxswe.com/rltoken/IUKEfGVroNza8u37x0lEzw">Khan Academy: </a>Prime Numbers: Introduction to prime numbers.</li>
    <li><a href="https://intranet.alxswe.com/rltoken/sVjdrNQEaErO_qRYsVMTEg">Sieve of Eratosthenes in Python: </a>A step-by-step guide to implementing the sieve algorithm in Python.</li>
</li>
<li>Game Theory Basics:
    <li><a href="https://intranet.alxswe.com/rltoken/lH4z--LnsuXYKh23Ji9Elw">Game Theory Introduction:</a> A simple explanation of game theory and strategic decision-making.</li>
</li>
<li>Dynamic Programming:
    <li><a href="https://intranet.alxswe.com/rltoken/W6T0RxWaFG3GisPxLLNYkQ">What Is Dynamic Programming With Python Examples: </a>An introduction to dynamic programming with Python examples.</li>
</li>
<li>Python Official Documentation:
    <li><a href="https://intranet.alxswe.com/rltoken/JTEGXnSDYDp8yblD9y86eg">Python Lists: </a>Managing lists in Python, useful for tracking the game state.</li>
</li>
<p>
By grasping these concepts and making use of the recommended resources, you will be well-equipped to approach the problem with a solid understanding of both the mathematical and programming challenges involved. The key to success in this project lies in applying efficient algorithms to manage the game’s state and making optimal decisions based on the game’s rules.
</p>
<h1>Tasks</h1>
<b>0. Prime Game</b>
<p>
Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.
</p>
<p>
They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.
</p>
<li>Prototype: def isWinner(x, nums)</li>
<li>where x is the number of rounds and nums is an array of n</li>
<li>Return: name of the player that won the most rounds</li>
<li>If the winner cannot be determined, return None</li>
<li>You can assume n and x will not be larger than 10000</li>
<li>You cannot import any packages in this task</li>
Example:

<li>x = 3, nums = [4, 5, 1]</li>

<b>First round: 4</b>

<li>Maria picks 2 and removes 2, 4, leaving 1, 3</li>
<li>Ben picks 3 and removes 3, leaving 1</li>
<li>Ben wins because there are no prime numbers left for Maria to choose</li>

<b>Second round: 5</b>

<li>Maria picks 2 and removes 2, 4, leaving 1, 3, 5</li>
<li>Ben picks 3 and removes 3, leaving 1, 5</li>
<li>Maria picks 5 and removes 5, leaving 1</li>
<li>Maria wins because there are no prime numbers left for Ben to choose</li>

<b>Third round: 1</b>
<li>Ben wins because there are no prime numbers for Maria to choose</li>
<b>Result: Ben has the most wins</b>
<pre>
carrie@ubuntu:~/0x0A-primegame$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
</pre>
<pre>
carrie@ubuntu:~/0x0A-primegame$
carrie@ubuntu:~/0x0A-primegame$ ./main_0.py
Winner: Ben
carrie@ubuntu:~/0x0A-primegame$
</pre>
<b>Repo:</b>

<li>GitHub repository: alx-interview</li>
<li>Directory: 0x0A-primegame</li>
<li>File: 0-prime_game.py</li>

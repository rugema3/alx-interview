<h1>0x06. Star Wars API</h1>
<p>
The “0. Star Wars Characters” project requires you to interact with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you need to be familiar with several key concepts related to web programming, API interaction, and asynchronous programming in JavaScript.
</p>
<h1>Concepts Needed:</h1>
<li>HTTP Requests in JavaScript:
    <li>Understanding how to make HTTP requests to external services using the request module or alternatives like fetch in Node.js.</li>
    <li><a href="https://intranet.alxswe.com/rltoken/MVi2QK7VEKbM1C1ewe1G8Q">Making HTTP Requests in Node.js</a></li>
</li>
<li>Working with APIs:
    <li>Understanding the basics of RESTful APIs and how to interact with them.</li>
    <li>Parsing JSON data returned by APIs.</li>
    <li><a href="https://intranet.alxswe.com/rltoken/KyGS_uB68mLaP5irrH8JVA">Working with APIs in JavaScript</a></li>
</li>
<li>Asynchronous Programming:
    <li>Managing asynchronous operations with callbacks, promises, and async/await syntax.</li>
    <li>Handling API response data asynchronously.</li>
    <li><a href="https://intranet.alxswe.com/rltoken/tdKMGJrRstCkXSReNfRFpQ">Asynchronous Programming in JavaScript</a></li>
</li>
<li>Command Line Arguments in Node.js:
    <li>Using the process.argv array to access command-line arguments passed to a Node.js script.</li>
    <li><a href="https://intranet.alxswe.com/rltoken/ExaDQWLNmpSD4MeavYMQQg">Node.js Process & Command Line Arguments</a></li>
</li>
<li>Array Manipulation and Iteration:
    <li>Iterating over arrays and manipulating data structures to format and display character names.</li>
    <li><a href="https://intranet.alxswe.com/rltoken/ExaDQWLNmpSD4MeavYMQQg">JavaScript Array Methods</a></li>
</li>
<p>
By familiarizing yourself with these concepts and resources, you will be able to efficiently retrieve, process, and display Star Wars characters from the specified movie using the Star Wars API, demonstrating your ability to work with external APIs and manage asynchronous code in JavaScript.
</p>
<h1>More Info</h1>
<h2>Install Node 10</h2>
<pre>
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</pre>
<h2>Install semi-standard</h2>
<h3>Documentation</h3>
<pre>
$ sudo npm install semistandard --global
</pre>
<br>
<h2>Install request module and use it</h2>

<h3>Documentation</h3>
<pre>
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
</pre>

<h1>Tasks</h1>
<b>0. Star Wars Characters</b>
<p>
Write a script that prints all characters of a Star Wars movie:
</p>
<li>The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”</li>
<li>Display one character name per line in the same order as the “characters” list in the /films/ endpoint</li>
<li>You must use the Star wars API</li>
<li>You must use the request module</li>
<br>
<pre>
alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$ 
</pre>
<br>
<b>Repo:</b>

<li>GitHub repository: alx-interview</li>
<li>Directory: 0x06-starwars_api</li>
<li>File: 0-starwars_characters.js</li>
title: Portfolio
banner: My Projects
%%%



## What You'll Find

- [**Bootstrapping**](#bootstrapping)
- [**Graphics**](#graphics)
	- [Ray Tracer in C](#ray-tracer)
	- [Audio Visualiser](#audio-visualiser)
	- [Graphics Playground](#graphics-playground)
- [**Games**](#games)
	- [Space Racer](#space-racer)
	- [Sunken](#sunken)
	- [Wasm-4 Console](#wasm4-console)
- [**Other**](#other)
	- [WinDayNight](#windaynight)
	- [Websites](#websites)
	- [OSS (Netpbm)](#oss-netpbm)
	- [Advent of Code](#advent-of-code)
	- [Duplicate File Finder](#duplicate-finder)



<br>
<div class="portfolio-header">
	<h3 class="portfolio-title" id="bootstrapping">Bootstrapping</h3>
</div>

My goal is to build up to a high-level development environment starting from a minimal environment.
Using a 495-byte handwritten executable that just parses octal to a buffer and has access only to an input stream,
so far I've managed to bootstrap into my own rudimentary assembly language, and from there into a basic FORTH environment.

Further plans are to try implementing other programming paradigms seen in languages like LISP, APL, and C.

These code snippets are runnable code in each stage (octal, assembly, forth) that will call sys_exit with the status code 42:

```
110 307 300 347 000 000 000 # mov rax, 347q ; sys_exit_group
110 307 307 052 000 000 000 # mov rdi, 42   ; status code
017 005                     # syscall
^                           # execute the buffer code
```

```
:mover7 52 0 0 0 # status code 42 (oct 52)
<sysexit         # the sys_exit call
^                # execute the buffer code
```

```
: exit42   42 sys_exit ; # make word to push 42 and call exit
exit42                   # execute word
```



<br>

## Graphics

---



<br>
<div class="portfolio-header">
	<h3 class="portfolio-title" id="ray-tracer">Ray Tracer</h3>
	<div class="portfolio-links">
		<a class="button portfolio-button" href="https://github.com/WalterPlinge/rtic">GitHub</a>
	</div>
</div>

RTIC is one of my many ray tracers; this one targeting pure C (currently C17) with minimal dependencies, only using 2 libraries: <a href="https://github.com/nothings/stb/blob/master/stb_ds.h">Dynamic Storage</a> for arrays, and <a href="https://github.com/nothings/stb/blob/master/stb_image_write.h">Image Write</a> for PNG output.

It features a simple command-line interface, and a custom, human-editable file format for storing scene data. It builds with a custom script, also written in C, and supports several compilers. I also wanted to experiment with code style, from common type renaming to unconventional extra whitespace and alignment.

This image was rendered using the example world file provided, at 32 samples per pixel.

<figure class="portfolio-figure">
	<img src="/img/rtic_w1024_h512_s32_d32_109s-small.webp" alt="A scene showcasing some primitive shapes and materials" width="1024" height="512"/>
	<figcaption>A scene showcasing some primitive shapes and materials</figcaption>
</figure>



<br>
<div class="portfolio-header">
	<h3 class="portfolio-title" id="audio-visualiser">Audio Visualiser</h3>
</div>

This was a cool project looking at different ways of visualising audio. Working under my course leader at university, I was the sole developer, from a blank window to adding shader support and handling audio input (and output).

I modeled it after <a href="https://www.shadertoy.com/">ShaderToy</a>, making use of modern C++, and only minimal libraries:
<ul>
	<li><a href="https://www.opengl.org/sdk/libs/GLEW/">glew</a> + <a href="https://www.glfw.org/">glfw</a> for windowing, input and rendering</li>
	<li><a href="https://github.com/thestk/rtaudio">rtaudio</a> for audio input and output</li>
	<li><a href="https://github.com/adamstark/Gist">gist</a> for audio analysis</li>
</ul>

The image is of a prototype shader I wrote, using an FFT algorithm to show frequency information. I visualised it as a spiral, lining up the octaves which suits music visualisation very well. You can see the spiral highlighting 3 major areas around the middle bands at roughly 1, 4, 10 o'clock. These indicate a triad chord, and you can also see the notes resonating through the upper octaves, where the spikes are pointing outward.

<figure class="portfolio-figure">
	<img src="/img/audio_visualiser-small.webp" alt="A spiral visualisation of the audio" width="540" height="540"/>
	<figcaption>A spiral visualisation of the audio</figcaption>
</figure>



<br>
<div class="portfolio-header">
	<h3 class="portfolio-title" id="graphics-playground">Graphics Playground</h3>
	<div class="portfolio-links">
		<a class="button portfolio-button" href="https://github.com/WalterPlinge/odin-graphics-playground">GitHub</a>
	</div>
</div>

This is an example playground working through some basic steps of setting up different graphics APIs (OpenGL, Vulkan).

It's using the <a href="https://odin-lang.org/">Odin programming language</a> (other languages are available). I tried to focus on writing the bare minimum to highlight each functionally-necessary step.

I've used this several times as reference material to provide help and support to others who have had questions about getting up and running with both SDL/GLFW, and OpenGL/Vulkan.

The image you see here is of a model I loaded with my own OBJ loader, rendered using every stage that is highlighted in the examples before it. Plus it's a pretty cute Mini Cooper.

<figure class="portfolio-figure">
	<img src="/img/graphics_playground.webp" alt="A render of a model Mini Cooper" width="520" height="397"/>
	<figcaption>A render of a model Mini Cooper</figcaption>
</figure>



<br>

## Games

---



<br>
<div class="portfolio-header">
	<h3 class="portfolio-title" id="space-racer">Space Racer</h3>
	<div class="portfolio-links">
		<a class="button portfolio-button" href="https://github.com/WalterPlinge/SpaceRacer">GitHub</a>
	</div>
</div>

This was a project I worked on in University, as a group project with a team of 6: I was one of two gameplay programmers, working alongside an artist, a 3d modeller, a map designer, and organised by the project manager.

I worked with several systems within the game, such as gameplay features like movement, physics, and the boost mechanic. I also implemented some UI features, and handled the sound design.

One of my favourite achievements was debugging and fixing a problem with the physics. We already had the vehicle following a basic track, but after we added a section that went upside down, the vehicle would get stuck trying to correct its orientation and start spinning wildly. The issue turned out to be naively calculating a cross product, which happened to invert when the vehicle's up vector was pointing down in world space. I implemented a fix, and then development carried on with our orientation-agnostic driving!

I also created the music for the game. Since I was handling the sound design, I decided to try my hand at composing, which allowed me to also focus on other design aspects, such as exploring the themes of the game and what does and doesn't fit the style.

<figure class="portfolio-figure">
	<img src="/img/spaceracer-small.webp" alt="Racing through a sci-fi space-city" width="1440" height="900"/>
	<figcaption>Racing through a sci-fi space-city</figcaption>
</figure>



<br>
<div class="portfolio-header">
	<h3 class="portfolio-title" id="sunken">Sunken</h3>
	<div class="portfolio-links">
		<a class="button portfolio-button" href="https://github.com/WalterPlinge/sunken">GitHub</a>
	</div>
</div>

A game where you play as a submarine, in the midst of the deep, dark ocean. Your task is to find and destroy a secret base, but beware! You are not alone.

The main concept behind Sunken is centered around how submarines see. Deep under the waves, there are no windows let alone light, so they rely on sound. You can only know what's out there if you can *hear* what's out there. The way submarines achieve this is with SONAR, either passively listening, or actively creating noise and listening for echos. The problem with creating sound is that the something else out there can hear you too.

This concept has a lot of potential for creating a mysterious, and even scary, atmosphere. Sunken takes inspiration from the 3D submarine game "Cold Waters", a game with an intense ambience. Sunken tries to replicate the feeling of being alone in silence by making the player rely on SONAR to locate points of interest. This means you'll have to go hunting for loot, but you may also hear that you aren't alone.

<figure class="portfolio-figure">
	<img src="/img/sunken.webp" alt="The player submarine locating a ship and some resources" width="1920" height="1017"/>
	<figcaption>The player submarine locating a ship and some resources</figcaption>
</figure>



<br>
<div class="portfolio-header">
	<h3 class="portfolio-title" id="wasm4-console">Wasm-4 Console</h3>
</div>

> "<a href="https://wasm4.org/">WASM-4</a> is a low-level fantasy game console for building small games with WebAssembly."

I've had a lot of fun playing around with ideas on this console. It's really easy to get started, and the limitation add an extra dimension of creativity.

Several of my projects with this have been recreating simple ideas from games, such as Flappy Bird (or Flappy Frog if I so please), a "Bloons Tower Defence"-style map and rail system, and a minigame reminiscent of fishing in Club Penguin.

These pictures are of some of my own ideas: a minigolf game experimenting with tilemaps, and a pixel-art paint application playing with the 4 colour limitation.

<figure class="portfolio-figure">
	<img src="/img/wasm4-small.webp" alt="A minigolf game (left); A simple drawing application (right)" width="1910" height="995"/>
	<figcaption>A minigolf game (left); A simple drawing application (right)</figcaption>
</figure>



<br>

## Other

---



<br>
<div class="portfolio-header">
	<h3 class="portfolio-title" id="windaynight">WinDayNight</h3>
	<div class="portfolio-links">
		<a class="button portfolio-button" href="https://handmade.network/p/273/windaynight">Handmade Network</a>
		<a class="button portfolio-button" href="https://github.com/WalterPlinge/windaynight">GitHub</a>
	</div>
</div>

This is a little tool I wrote to toggle the Windows' system & app themes between light and dark mode. I wanted to have the light theme in the day to see content clearly, and then the dark theme at night to ease the strain on my eyes.

My first try included an unwieldly command for Windows' Task Scheduler. So I remade the application to toggle the theme using the registry which is much more sane, and added a couple flags so I could call this on schedule instead. It works like a charm.

<figure class="portfolio-figure">
	<img src="/img/windaynight-original-small.webp" alt="The original logo design (by Phillip Trudeau)" width="256" height="256"/>
	<figcaption>The original logo design (by <a href="https://github.com/pmttavara">Phillip Trudeau</a>)</figcaption>
</figure>



<br>
<div class="portfolio-header">
	<h3 class="portfolio-title" id="websites">Websites</h3>
	<div class="portfolio-links">
		<a class="button portfolio-button" href="https://github.com/WalterPlinge/walterplinge.github.io">GitHub</a>
	</div>
</div>

I wanted to keep this website simple, functional, and fast. I'm using <a href="https://simplecss.org//">Simple.css</a> to help with styling, and I've added a few additions for page structure.

I wrote my own site generator that compiles markdown webpages and populates an html template. This makes it easier to edit my custom styling, since I can update something once and it changes for every page. I am also using a custom GitHub build script to automate deployment.

I also have previous experience with Python Flask with database integration for serving dynamic websites, focusing on content sharing and community interaction.

<figure class="portfolio-figure">
	<img src="/img/website_score.webp" alt="A generic image indicative of web technologies" width="390" height="131"/>
</figure>



<br>
<div class="portfolio-header">
	<h3 class="portfolio-title" id="oss-netpbm">OSS (and Odin Netpbm Library)</h3>
	<div class="portfolio-links">
		<a class="button portfolio-button" href="https://github.com/odin-lang/Odin/tree/master/core/image/netpbm">GitHub</a>
	</div>
</div>

This is me being excited to contribute code to a project that I like, specifically the <a href="https://odin-lang.org/">Odin programming language</a> core library. I wrote a Netpbm image file format reader/writer, covering ALL the official formats (PBM, PGM, PPM, PAM), and even the unofficial PFM.

This is alongside other contributions such as expanding the Vulkan vendor package to simplify loading all the Vulkan procedures, and minor core library touch-ups and quality-of-life additions here and there.

<figure class="portfolio-figure">
	<img src="/img/netpbm_contrib.webp" alt="An example of my contribution to Odin" width="857" height="192"/>
	<figcaption>An example of my contribution to Odin</figcaption>
</figure>



<br>
<div class="portfolio-header">
	<h3 class="portfolio-title" id="advent-of-code">Advent of Code</h3>
	<div class="portfolio-links">
		<a class="button portfolio-button" href="https://github.com/WalterPlinge/aoc">GitHub</a>
	</div>
</div>

I first discovered the Advent of Code through a dedicated channel in the Odin language Disord server in 2021. It looked like fun so I gave it a go.

I love how these puzzles are set out, with the "your naive solution won't cut it" 2nd part to them and the gentle(-ish) increase in difficulty. I managed to get up to day 22, as christmas took over; I would like to go back and finish them at some point. Especially the previous years, I've already made a start on 2015.

In the repo, I have a template source file which I copy into each day. There's a few inconsistencies throughout as I've updated it over time. Currently it's structured to start writing my code in the puzzle function, and fill out the two answer variables. It also comes with a basic benchmark feature and memory leak detection (very handy for those cambrian explosion types).

<figure class="portfolio-figure">
	<img src="/img/aoc.webp" alt="My 2021 run of Advent of Code" width="947" height="668"/>
	<figcaption>My 2021 run of Advent of Code</figcaption>
</figure>



<br>
<div class="portfolio-header">
	<h3 class="portfolio-title" id="duplicate-finder">Duplicate File Finder</h3>
	<div class="portfolio-links">
		<a class="button portfolio-button" href="https://github.com/WalterPlinge/duplicate-finder">GitHub</a>
	</div>
</div>

While organising my device backups, I realised I had several files that were duplicates.

I wanted a way to find them quickly without spending time looking for an app that already exists. So I made my own. That makes sense... right?

This was also a nice exercise in thinking about how to find small optimisations, namely comparing OS-reported size before I compare all the data of 2GB files, and string interning was an interesting addition.

<figure class="portfolio-figure">
	<img src="/img/duplicate_file_finder.webp" alt="Generic Windows file copy dialog window" width="449" height="287"/>
</figure>

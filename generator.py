index_content = {
	'about': (
		'Hello there',
		[
			'''My name is Scott. I'm a programmer interested in game development and various surrounding technologies, such as graphics and visualisations, data structures and algorithms, and a range of low-level to high-level concepts.''',
			'''I graduated from Edinburgh Napier University with a 1st class Bachelor of Science with Honours in Game Development.''',
			'''This is my site for sharing information about things that I've done and projects I've worked on.''',
		]
	),
	'links': (
		'Places to go',
		[('Portfolio', 'portfolio.html')]
	),
}

'''
list of categories
	list of items
		title
		list of links
			name
			url
		image file
		blurb: list of blocks
'''
portfolio_content = {
	'Graphics': [
		(
			'Ray Tracer In C (RTIC)',
			[('GitHub', 'https://github.com/WalterPlinge/rtic')],
			'rtic_w1024_h512_s32_d32_109s.png',
			[
				'''RTIC is one of many ray tracers I have made; this one had its focus on being written in pure C (currently C17) with minimal dependencies.''',
				'''To make my C life a little easier, I only used 2 libraries: Sean Barrett's <a href="https://github.com/nothings/stb/blob/master/stb_ds.h">Dynamic Storage</a> for arrays, and <a href="https://github.com/nothings/stb/blob/master/stb_image_write.h">Image Write</a> for PNG output.''',
				'''I also experimented with code style, from the more common type renaming to the unconventional extra whitespace and alignment.''',
				'''The image you see was rendered using the example world file provided, at 32 samples per pixel.''',
			],
		),
		(
			'Audio Visualiser',
			[],
			'audio_visualiser.png',
			[
				'''This was a cool project I worked on under my course leader at university; looking at different ways of visualising audio. I was the sole developer, from a blank window to adding shader support and handling audio input (and output). I modeled it after <a href="https://www.shadertoy.com/">ShaderToy</a>, making use of modern C++, and only minimal libraries:
<div class="content">
	<ul>
		<li><a href="https://www.opengl.org/sdk/libs/GLEW/">glew</a> + <a href="https://www.glfw.org/">glfw</a> for windowing, input and rendering</li>
		<li><a href="https://github.com/thestk/rtaudio">rtaudio</a> for audio input and output</li>
		<li><a href="https://github.com/adamstark/Gist">gist</a> for audio analysis</li>
	</ul>
</div>''',
				'''This image is of a later prototype shader I wrote, using the audio FFT to show frequency information. I visualised it as a spiral, lining up the octaves, which suits music visualisation very well.''',
				'''You can see the spiral highlights 3 different areas (around the middle bands, roughly 1, 4, 10 o'clock), which indicates a triad chord, and you can even see the notes resonating through multiple octaves, where the spikes are pointing outward. Songs like Rocket Man by Elton John with its guitar slide in the chorus, you could see it sliding up and away around the spiral!''',
				'''(As a side project I have started remaking it, I do not currently have a link to source "yet")''',
			],
		),
		(
			'Graphics Playground',
			[('GitHub', 'https://github.com/WalterPlinge/odin-graphics-playground')],
			'graphics_playground.png',
			[
				'''This is an example playground working through some basic steps of setting up different graphics APIs (OpenGL, Vulkan).''',
				'''It's using the <a href="https://odin-lang.org/">Odin programming language</a> (other languages are available), this is just personal preference, as it allows me to focus on each step I want to highlight, and avoids any extra cruft.''',
				'''I've used this several times as reference material to provide help and support to others who have had questions about getting up and running with both SDL/GLFW, and OpenGL/Vulkan.''',
				'''The image you see here is of a model I loaded with a custom OBJ loader, rendered using every stage that is highlighted in the examples before it. Plus it's a pretty cute Mini Cooper.''',
			],
		),
	],
	'Games': [
		(
			'Space Racer',
			[('GitHub', 'https://github.com/WalterPlinge/SpaceRacer')],
			'spaceracer.png',
			[
				'''This was a project I worked on in University, as a group project with a team of 6: I was one of two gameplay programmers, working alongside an artist, a 3d modeller, a map designer, and organised by the project manager.''',
				'''I worked with several systems within the game, such as gameplay features like movement, physics, and the boost mechanic. I also implemented some UI features, and handled the sound design.''',
				'''One of my favourite achievements in my role of programmer was debugging and fixing a problem with the physics. We already had the vehicle following a basic track, but after we added a section that went upside down, the vehicle would get stuck trying to correct its orientation and would start spinning wildly. The issue turned out to be that it was naively calculating a cross product, which happened to invert when the vehicle's up vector was pointing down in world space. I implemented a fix, and then development carried on with our orientation-agnostic driving!''',
				'''I also created the music for the game. Since I was handling the sound design, I decided to take on the role of composer, which allowed me to also focus on other design aspects, such as exploring the themes of the game and what does and doesn't fit the style.''',
			],
		),
		(
			'Sunken',
			[('GitHub', 'https://github.com/WalterPlinge/sunken')],
			'sunken.png',
			[
				'''A game where you play as a submarine, in the midst of the deep, dark ocean. Your task is to find and destroy a secret base, but beware! You are not alone.''',
				'''The main concept behind Sunken is centered around how submarines see. Deep under the waves, there are no windows, let alone light, so they rely on sound. You can only know what's out there, if you can HEAR what's out there. The way submarines achieve this is with SONAR, either passively listening, or actively creating noise and listening for echos. The problem with creating sound is that the something else out there can hear you too.''',
				'''This concept has a lot of potential for creating a mysterious, and even scary, atmosphere. Sunken takes inspiration from the 3D submarine game "Cold Waters", a game with an intense ambience. Sunken tries to replicate the feeling of being alone in silence by making the player rely on SONAR to locate points of interest. This means you'll have to go hunting for loot, but you may also hear that you aren't alone.''',
			],
		),
		(
			'Wasm-4 Console',
			[],
			'wasm4.jpg',
			[
				'''"<a href="https://wasm4.org/">WASM-4</a> is a low-level fantasy game console for building small games with WebAssembly."''',
				'''I've had a lot of fun playing around with ideas on this console. It's really easy to get started, and the limitation add an extra dimension of creativity.''',
				'''Several of my projects with this have been recreating simple ideas from games, such as Flappy Bird (or Frog, as I did) gameplay, a bloons-style map and rail system, and the fishing minigame from Club Penguin.''',
				'''These pictures are of some of my own ideas: a minigolf game experimenting with tilemaps, and a pixel-art paint application playing with the 4 colour limitation.''',
			],
		),
	],
	'Other': [
		(
			'Websites',
			[('GitHub', 'https://github.com/WalterPlinge/walterplinge.github.io')],
			'web_dev.jpg',
			[
				'''For this website I wanted to keep simple, functional, and fast. I'm using <a href="https://bulma.io/">Bulma</a> to help with styling, and I've added a few additions for page structure. Apart from that, the design and implementation is minimal and straight-to-the-point. I do quite like it.''',
				'''I am also using a custom GitHub build script; this site is generated! This is so I can have an easier and more consistent way to deal with the content. It's also easier to edit my custom styling, since I can update something once and it changes for the whole page.''',
				'''In University I made two websites for my Advanced Web Development module. Both were dynamic sites, serving templated pages from a python flask app, using HTML/CSS/JavaScript and backed by a database. (Unfortunately those aren't being hosted anymore.)''',
				'''The first was a music website that displays information about artists, albums, songs, and genres. One of the most enjoyable parts was working out how I could store all that information in a simple way, so that I could also help the app to fill out the templates more easily. This also helped me focus on the navigation for users and designing it to be user-friendly.''',
				'''The second was an image sharing website. This was more involved, as I added the ability to create and manage user accounts, and allowed users to upload and manage their own content, as well as add comments on other users' posts. Again, the fun part was working out how the data should be stored, and how the backend was going to manage it all. It worked well at keeping unnecessary complexity out of the code.''',
			],
		),
		(
			'WinDayNight',
			[
				('GitHub', 'https://github.com/WalterPlinge/windaynight'),
				('Handmade Network', 'https://handmade.network/p/273/windaynight/'),
			],
			'windaynight.png',
			[
				'''This is a little tool I wrote to toggle the Windows' system & app themes between light and dark mode. I wanted to have the light theme in the day so I could see what I was doing, and I'd have a dark theme at night to be easier on the eyes.''',
				'''The first try included an unwieldly command for Windows' Task Scheduler. So I made this application that would toggle the theme, and added a couple flags so I could call this on schedule instead. It works like a charm.''',
			],
		),
		(
			'Odin Netpbm Library (and OSS)',
			[('GitHub', 'https://github.com/odin-lang/Odin/tree/master/core/image/netpbm')],
			'netpbm_contrib.png',
			[
				'''This is me being excited to contribute code to a project that I like, specifically the <a href="https://odin-lang.org/">Odin programming language</a> core library. I wrote a Netpbm image file format reader/writer, covering ALL the official formats (PBM, PGM, PPM, PAM), and even the unofficial PFM.''',
				'''This is alongside other contributions such as expanding the Vulkan vendor package to simplify loading all the Vulkan procedures, and minor core library touch-ups and quality-of-life additions here and there.''',
			],
		),
		(
			'Advent of Code',
			[('GitHub', 'https://github.com/WalterPlinge/aoc')],
			'aoc.png',
			[
				'''I first discovered the Advent of Code through a dedicated channel in the Odin language Disord server in 2021. It looked like fun so I gave it a go.''',
				'''I love how these puzzles are set out, with the "your naive solution won't cut it" 2nd part to them and the gentle(-ish) increase in difficulty. I managed to get up to day 22, as christmas took over; I would like to go back and finish them at some point. Especially the previous years, I've already made a start on 2015.''',
				'''In the repo, I have a template source file which I copy into each day. There's a few inconsistencies throughout as I updated it over time. Currently it's structured so I can just write my code in the puzzle function, and fill out the two answer variables. It also comes with a basic benchmark feature and memory leak detection (very handy for those cambrian explosion types).''',
			],
		),
		(
			'Duplicate File Finder',
			[('GitHub', 'https://github.com/WalterPlinge/duplicate-finder')],
			'duplicate_file_finder.jpg',
			[
				'''While organising my device backups, I realised I had several files that were duplicates.''',
				'''I wanted a way to find them quickly without spending time looking for an app that already exists. So I made my own. That makes sense... right?''',
				'''This was also a nice exercise in thinking about how to find small optimisations, namely comparing OS-reported size before I compare all the data of 2GB files, and string interning was an interesting addition.''',
			],
		),
	],
}

# page title, header title, content
page_html = '''\
<!DOCTYPE html>
<html style="height: 100%;">
	<head>
		<title>{}</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<meta name="color-scheme" content="light dark"/>
		<meta name="prefers-color-scheme" content="light dark"/>
		<link rel="stylesheet" href="css/styles.css">
		<link rel="icon" href="img/favicon.png">
	</head>
	<body class="has-background-grey-dark has-text-light" style="min-height: 100%;">
		<section class="hero is-primary is-small">
			<div class="hero-body">
				<div class="container">
					<h1 class="title is-1 has-text-weight-bold">
						{}
					</h1>
				</div>
				<div class="container">
					<div class="block">
						<a href="index.html">Home</a>
					</div>
				</div>
			</div>
		</section>
		{}
		<footer class="footer has-background-dark">
			<div class="content has-text-light has-text-centered">
				<p>
					Copyright 2022 <a href="https://walterplinge.github.io">Scott Davidson</a>. The source code is licensed <a href="http://opensource.org/licenses/mit-license.php">MIT</a>. The website content is licensed <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY NC SA 4.0</a>.
				</p>
			</div>
		</footer>
	</body>
</html>'''

index_html = {
	# heading, content
	'about': '''\
		<section class="section" style="height: 100%; min-height: 100%;">
			<div class="container">
				<div class="box has-background-dark">
					<h2 class="subtitle is-3 has-text-light">
						{}
					</h2>
					<div class="block has-text-light">
						{}
					</div>
				</div>
			</div>
		</section>''',

	# heading, list
	'links': '''\
		<section class="section" style="height: 100%; min-height: 100%;">
			<div class="container">
				<div class="box has-background-dark">
					<h2 class="subtitle is-3 has-text-light">
						{}
					</h2>
					<div class="block">
						<div class="content has-text-light">
							<ul>
								{}
							</ul>
						</div>
					</div>
				</div>
			</div>
		</section>''',

	# url, name
	'link-item': '''\
		<li><a href="{}">{}</a></li>''',
}

portfolio_html = {
	# category name, content
	'category': '''\
		<section class="section">
			<div class="container">
				<div class="portfolio-box-section">
					<h2 class="portfolio-title">
						{}
					</h2>
					{}
				</div>
			</div>
		</section>''',

	# item direction, content
	'item': '''\
		<div class="block">
			<div class="portfolio-box-item">
				<div class="{}">
					{}
				</div>
			</div>
		</div>''',

	# all content
	'item-part': '''\
		<div class="portfolio-column">
			{}
		</div>''',

	# item title
	'item-title': '''\
		<p class="portfolio-subtitle">
			{}
		</p>''',

	# item link url, link name
	'item-links': '''\
		<a class="portfolio-button" href="{}">
			{}
		</a>''',

	# item image file name
	'item-image': '''\
		<figure class="image has-ratio">
			<img src="img/{}" alt="Loading image..."/>
		</figure>''',

	# item blurb paragraph
	'item-blurb': '''\
		<div class="block">
			{}
		</div>''',
}



import os
import re
import shutil

import sass



def format_html(html):
	# lets make it flat, it's smaller and link underlines don't break like with beautifulsoup
	return re.sub('\n\t*', '\n', html)

def gen_index():
	blurb_heading = index_content['about'][0]
	blurb_content = ''
	for b in index_content['about'][1]:
		blurb_content += b + '\n<br>\n'

	about_content = index_html['about'].format(blurb_heading, blurb_content)

	links_heading = index_content['links'][0]
	links_items = ''
	for l in index_content['links'][1]:
		# url, name
		links_items += index_html['link-item'].format(l[1], l[0])

	links_content = index_html['links'].format(links_heading, links_items)

	html_content = page_html.format('WalterPlinge', 'Welcome', about_content + links_content)
	return format_html(html_content)

def gen_portfolio():
	item_left_aligned = True
	page_content = ''
	for category_name, category_value in portfolio_content.items():
		category_content = ''
		for item in category_value:

			item_title = portfolio_html['item-title'].format(item[0])

			item_links = ''
			for link in item[1]:
				# url, name
				item_links += portfolio_html['item-links'].format(link[1], link[0])

			item_image = portfolio_html['item-image'].format(item[2])

			item_blurb = ''
			for block in item[3]:
				item_blurb += portfolio_html['item-blurb'].format(block)

			item_content = ''
			for part in [item_title, item_links, item_image, item_blurb]:
				item_content += portfolio_html['item-part'].format(part)

			item_format = 'portfolio-columns' if item_left_aligned else 'portfolio-columns-reverse'
			item_left_aligned = not item_left_aligned

			category_content += portfolio_html['item'].format(item_format, item_content)

		page_content += portfolio_html['category'].format(category_name, category_content)

	html_content = page_html.format('Portfolio', 'Portfolio', page_content)
	return format_html(html_content)



os.makedirs('_site/css', exist_ok=True)

with open('_site/css/styles.css', 'w', encoding='utf-8') as f:
	f.write(sass.compile(filename='sass/styles.sass', output_style='compressed'))

with open('_site/index.html', 'w', encoding='utf-8') as f:
	f.write(gen_index())

with open('_site/portfolio.html', 'w', encoding='utf-8') as f:
	f.write(gen_portfolio())

shutil.copytree('img', '_site/img', dirs_exist_ok=True)

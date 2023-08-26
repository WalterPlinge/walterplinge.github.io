import os
import re
import shutil
import pathlib

import markdown2



def format_html(html):
	html = re.sub('\n\s*', '', html) # remove newline and leading spaces
	return html

def format_css(css):
	css = re.sub('/\*.*\*/', '', css) # remove comments
	css = re.sub('\s+', ' ', css)     # remove consecutive spaces
	match = '[\w%][\w\- ]+[\w(]'      # i think this matches important spaces
	tok = re.split(f'({match})', css) # only preserve important spaces
	css = ''
	for t in tok:
		if re.fullmatch(f'{match}', t):
			css += t
		else:
			css += re.sub('\s+', '', t)
	return css

def parse_meta(header):
	meta = {}
	lines = header.splitlines()
	for line in lines:
		tokens = line.split(':')
		key = tokens[0].strip()
		value = tokens[1].strip()
		meta[key] = value
	return meta



page_html = pathlib.Path('template.html').read_text()

style = pathlib.Path('css/simple.css').read_text()
style += pathlib.Path('css/custom.css').read_text()
style = format_css(style)

markdown_extras = ['tables', 'header-ids']

file_paths = []
for (root, directories, files) in os.walk('pages'):
	for file in files:
		if os.path.splitext(file)[1] == '.md': # only handle markdown files
			path = os.path.join(root, file) # construct file path
			path = os.path.normpath(path)   # normalise separators
			path = path.replace('\\', '/')  # unix separators please
			file_paths.append(path)

for file in file_paths:
	site_path = file.split('/', maxsplit=1)[1] # remove 'pages/'
	site_path = os.path.splitext(site_path)[0] # remove '.md'
	site_path = '_site/' + site_path + '.html' # construct url path
	directory = os.path.split(site_path)[0]    # get directories
	os.makedirs(directory, exist_ok=True)

	content = pathlib.Path(file).read_text()
	content = content.split('%%%', maxsplit=1) # metadata is before the first '%%%'

	meta = parse_meta(content[0])
	title = meta['title']
	banner = meta['banner']

	content = content[1]
	content = markdown2.markdown(content, extras=markdown_extras)
	content = page_html.format(title, banner, content, style)
	content = format_html(content)

	pathlib.Path(site_path).write_text(content)

shutil.copytree('img', '_site/img', dirs_exist_ok=True)

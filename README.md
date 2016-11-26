# microCMS

I created several content management systems in the past, but this is the most minimal one and pain free that I could come up with.
I use it to create my [personal website](http://curious-electric.com).

I stumbled upon this [HN thread](https://news.ycombinator.com/item?id=13009080) and realized it might be useful for other people, too.

# Installation

You need Python 2.7x installed. Just download or clone it, and change the files in 'input' accordingly.

Then run ```doit.sh```.

# Configuration

To create a site, you create a couple of markdown files that will be converted to HTML files.
Then you simply add all pages in the bash script ```doit.sh``` by adding lines like these:

	python generator.py input/index.md styles.css output/index.html

The doit script creates HTML pages in the output folder.
the ```do_ftp.sh``` script (that you derive from the template) uploads the 'output' folder to your provider.

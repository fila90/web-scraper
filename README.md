# web-scraper
Get all images, contents, titles, whatever from your favorite website

## How to:
```python
import scraper

url = 'https://blabladev.com/'

# you need to specify from which tag you want to extract sources 'img', 'a', 'video', etc..
srcs = scraper.get_src(url, 'img')
# it will generate results.txt file where you can see results

# provide any valid html tag 'p', 'h1', 'title', 'a', etc..
content = scraper.get_tag_content(url, 'p')
# it will generate results.txt file where you can results
```

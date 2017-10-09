#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'http://xkcd.com'
# url = 'http://xkcd.com'

os.makedirs('xkcd', exist_ok=True)     # store comics in ./xkcd
# os.mkdir('xkcd', exist_ok=True)
while not url.endswith('#'):
    #  Download the page.
    print('Downloading page %s...' %url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    #  Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        '''
        < div
        id = "comic" >
        < img
        src = "//imgs.xkcd.com/comics/real_estate.png"
        title = "I tried converting the prices into pizzas, to put it in more familiar terms, and it just became a hard-to-think-about number of pizzas."
        alt = "Real Estate"
        srcset = "//imgs.xkcd.com/comics/real_estate_2x.png 2x" / >
        < / div >
        '''
        comicUrl = 'http:' + comicElem[0].get('src')
    #  Download the image.
    print('Downloading image %s...' %(comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()

    #  Save the image to ./xkcd.
    imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # TODO: Get the prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done')



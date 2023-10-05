import pyshorteners

url = input('Enter your url here: ')

#url=https://www.linkedin.com/feed/?trk=guest_homepage-basic_google-one-tap-submit
def shortenurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortenurl(url)
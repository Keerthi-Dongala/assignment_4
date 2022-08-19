import urllib.request
count=0
url='https://www.rguktsklm.ac.in'
resp=urllib.request.urlopen(url)
page1=res.read()
page=str(page1)
def getURL(page):
    start_link=page.find("<a href")
    start_quote=page.find('"',start_link)
    end_quote=page.find('"',start_quote+1)
    url=page[start_quote+1:end_quote]
    return url,n
while True:
    url,n=getURL(page)
    page=page[n:]
    if url:
        print(url)
        count=count+1
    else:
        break
print(count)

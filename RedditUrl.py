import urllib 
def GetPicture (webURL):
    htmlFile =  urllib.urlopen(webURL)
    htmlSource = htmlFile.read()
    ListOfhtmlSource = htmlSource.split()
    #The following is a loop that finds the URL of the image
    for i in range (1 , len (ListOfhtmlSource)):
        #"id='header-img'" this is the id to finding the URL of the image
        if ListOfhtmlSource[i]== "id='header-img'" : 
            t = ListOfhtmlSource[i+1]
            url = t[5:(len(t)-1)]
            filename = ''.join(url.split('/')[-1:])
            #Input the location of where you want your header to be saved in. 
            #The following is an example of a location for my computer, or remove 
            #",'c:\\users\\bill\\Desktop\\Reddit Image\\'+ filename"
            #if you want the file to be in your temporary files.
            urllib.urlretrieve(url,'c:\\users\\bill\\Desktop\\Reddit Image\\'+ filename )   
    htmlFile.close()
 
#input any reddit site that you want the header of
GetPicture("http://www.reddit.com/r/uwaterloo/")
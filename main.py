import os, praw, urllib.parse, requests

class WholememeBot():

    def __init__(self,tag):
        self.botTag = tag
        self.keyPath = 'private'
        self.resPath = 'res'
        self.rAPI = 'reddit'
        self.fAPI = 'facebook'
        self.postLimit = 10
        self.setup_reddit_API()
        self.get_images_from_subreddit('wholesomememes',self.postLimit)

    def format_text(self,text):
        return '[' + self.botTag + '] ' + text

    def printf(self,text):
        print(self.format_text(text))

    def read_keys(self,filename):
        with open(os.path.join(self.keyPath,filename+'.txt'),'r') as r:
            return r.read().splitlines()

    def setup_reddit_API(self):
        secret = self.read_keys(self.rAPI)
        self.printf('Started Reddit API')
        self.r = praw.Reddit(client_id=secret[0],client_secret=secret[1],password=secret[2],username=secret[3],user_agent=secret[4])

    def download_image(self,img_url):
        file_name = os.path.basename(urllib.parse.urlsplit(img_url).path)
        img_path = os.path.join(self.resPath,file_name)
        self.printf('Downloading image URL ' + img_url + ' to ' + img_path)
        resp = requests.get(img_url, stream=True, allow_redirects=False)
        if resp.status_code == 200:
            with open(img_path, 'wb') as image_file:
                image_file.write(resp.content)
            return img_path
        else:
            self.printf('Image failed to download. Status code: ' + str(resp.status_code))

    def get_images_from_subreddit(self,subname,num):
        for post in self.r.subreddit(subname).new(limit=num):
            self.download_image(post.url)

if(__name__=="__main__"):

    wmb = WholememeBot('wmbot')
    print(wmb.read_keys('reddit'))

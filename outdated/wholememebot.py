import praw, glob, facebook, re, requests, os, urllib.parse

#reddit oauth
#trust me, you didn't want to see these lines

#fb oauth

IMAGE_DIR = 'WholesomeMemes'

def run(subname):
    for submission in r.subreddit(subname).new(limit=10):
        if(get_Img(submission.url)==1):
            dl_image(submission.url)
            print('[wmbot] '+submission.id+ " ||| "+submission.url)

def dl_image(img_url): #Copyright 2015 Randal S. Olson
    ''' Downloads i.imgur.com images that reddit posts may point to. '''
    file_name = os.path.basename(urllib.parse.urlsplit(img_url).path)
    print(file_name)
    img_path = IMAGE_DIR + '/' + file_name
    print('[wmbot] Downloading image at URL ' + img_url + ' to ' + img_path)
    resp = requests.get(img_url, stream=True)
    if resp.status_code == 200:
        with open(img_path, 'wb') as image_file:
            for chunk in resp:
                image_file.write(chunk)
        return img_path
    else:
            print('[wmbot] Image failed to download. Status code: ' + resp.status_code)
    return ''

def get_Img(img_url):
    if 'imgur.com' in img_url:
        print('\n[wmbot] imgur')
        return 1
    elif 'reddituploads.com' in img_url:
        print('\n[wmbot] redditupload')
        return 0
    else:
        print('\n[wmbot] unknown source')

def get_api(page,cfg):
    print('[wmbot] setting up facebook connection\n')
    graph = facebook.GraphAPI(cfg[page+'_access_token'])
    print('[wmbot] facebook page_id: '+cfg[page+'_page_id']+'\n')
    return graph

def get_posts(user,graph):
    page = graph.get_object(user)
    posts = graph.get_connections(page['id'],'posts')
    for post in posts['data']:
        try:
            print(post)
            print('\n')
        except UnicodeEncodeError:
            print(post['id'])
            print('\n')

def read(self,path,filename):
    with open(os.path.join(path,filename).strip(),'r') as r:
        rd = r.read().splitlines()
    print(rd)
    return rd

def post(msg,graph):
    status = graph.put_wall_post(msg)

def postPicture(msg,graph):
    status = graph.put_wall_post(msg)

def main():

    api = get_api("wsm",cfg)

    #run('wholesomememes')
    #post('hello',api)
    get_posts('happywholesomememes',api)

if __name__ == '__main__':
    main()

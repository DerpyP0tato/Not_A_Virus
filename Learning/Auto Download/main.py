from urllib import request

remote_url = 'https://download847.mediafire.com/8rx2cjkc65mg/c1ks51nyz02jj4d/hi.txt'

local_file = 'hi.txt'

request.urlretrieve(remote_url,local_file)
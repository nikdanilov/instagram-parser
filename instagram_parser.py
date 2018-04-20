import requests
import json

class Instagram_Parser:

    def __init__(self, username):
        self.data = None
        self.username = username
        self.fetchData()

    def fetchData(self):
        pt = requests.get("https://instagram.com/{}".format(self.username)).text
        jd = pt.split("window._sharedData = ")[1].split(";</script>")[0]
        jj = json.loads(jd)
        self.data = jj

    def getFollowers(self):
        return self.data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count']

    def getFollowing(self):
        return self.data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow']['count']

    def getPostsCount(self):
        return self.data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count']

    def getFullName(self):
        return self.data['entry_data']['ProfilePage'][0]['graphql']['user']['full_name']

    def getProfilePic(self):
        return {
            "lowres": self.data['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url'],
            "highres": self.data['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd']
        }

    def getBio(self):
        return self.data['entry_data']['ProfilePage'][0]['graphql']['user']['biography']


inst = Instagram_Parser("nikita.danil0v")
print(inst.getFollowers(), inst.getFollowing(), inst.getPostsCount(), inst.getFullName())
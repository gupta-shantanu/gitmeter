import requests

GIT_API="https://api.github.com/"
class repository(object):

    """
    repository class containing required information as properties
    """

    def __init__(self,user,repo):
        self.get=requests.get(GIT_API+"repos/%s/%s" %(user,repo)).json()

    def fetch(self,*args,**kwargs):
        for properties in args:
            pass
        self.repData=self.get['name']+"\nStars:"+str(self.get['stargazers_count'])
        
        
            



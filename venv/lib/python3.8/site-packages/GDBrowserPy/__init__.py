import requests, json

class GD:
  def __init__(self):
    pass
  def search(self, name="*"):
    pass
  class LevelDoesNotExist(Exception):
    pass
  class UserDoesNotExist(Exception):
    pass

  class Level:
    def __init__(self,id,download=False):
      self.id = str(id)
      self.url = "https://www.gdbrowser.com/api/level/" + self.id
      if download:
        self.url = self.url + "?download"
      self.data =  requests.get(self.url).json()
      try:
        for i in self.data:
          try:
            value = json.loads(self.data[i])
          except:
            value = self.data[i]
          if type(value) == str:
            command = f"self.{i} = '{value}'"
          else:
            command = f"self.{i} = {value}"
          exec(command)
      except TypeError:
        raise GD.LevelDoesNotExist("-1")
    def leaderboard(self,count=100,weekly=False):
      self.count = count
      self.leaderurl = f"https://www.gdbrowser.com/api/leaderboardLevel/{self.id}?count={self.count}"
      if weekly:
        self.leaderurl = self.leaderurl + "?week"
      return requests.get(self.leaderurl).json()
    def like(self,type,username,password):
      self.accid = GD.User(username).accountID
      self.url = f"https://www.gdbrowser.com/like?ID={self.id}&like={type}&type=1&accountID={self.accid}&password={password}"
  class User:
    def __init__(self,id,forcePlayerID=False):
      self.id = str(id)
      self.url = "https://www.gdbrowser.com/api/profile/" + self.id
      if forcePlayerID:
        self.url = self.url + "?player"
      self.data =  requests.get(self.url).json()
      try:
        for i in self.data:
          try:
            value = json.loads(self.data[i])
          except:
            value = self.data[i]
          if type(value) == str:
            command = f"self.{i} = '{value}'"
          else:
            command = f"self.{i} = {value}"
          exec(command)
      except TypeError:
        raise GD.UserDoesNotExist("-1")
      self.iconObj = GD.Icon(username=self.username)
  class Icon:
    def __init__(self,username=None,form="cube",icon=None,col1=None,col2=None,colG=None,colW=None,glow=None,size="auto",topless=False,forcePlayerID=False,noUser=False,psd=False):
      self.username = str(username)
      self.form = form
      self.icon = icon
      self.col1 = col1
      self.col2 = col2
      self.colG = colG
      self.colW = colW
      self.glow = glow
      self.size = size
      self.topless = topless
      self.forcePlayerID = forcePlayerID
      self.noUser = noUser
      self.psd = psd
      self.url = f"https://www.gdbrowser.com/icon/{self.username}?form={self.form}"
      if self.psd:
        self.url = self.url + "&psd"
      if self.noUser:
        self.url = self.url + "&noUser"
      if self.forcePlayerID:
        self.url = self.url + "&player"
      if self.topless:
        self.url = self.url + "&topless"
      if not(self.glow == None):
          if self.glow:
            self.url = self.url + "&glow=1"
          else:
            self.url = self.url + "&glow=0"
      querys = ["self.colW","self.colG","self.col1","self.col2","self.icon"]
      for query in querys:
        if not(exec(query) == None):
            if exec(query):
              self.url = self.url + "&colW=" + exec(query)
            else:
              self.url = self.url + "&colW=" + exec(query)
    def iconURL():
      return 
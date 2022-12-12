import os
import pyChalk
import json

colours = pyChalk.pyChalk()

class Database:
  def __init__(self, path:str) -> None:
    self.path = path or "database.json"
    self.data = dict()
    self.hooked = False

  def create(self):
    if not os.path.exists(self.path):
      with open(self.path, "w") as f:
        f.write(json.dumps(self.data))

  def hook(self):
    if self.hooked:
      print(colours.fail("Database already hooked"))
    else:
      self.hooked = True
      with open(self.path, "r") as f:
        self.data = json.loads(f.read())

  def unhook(self):
    if self.hooked:
      self.hooked = False
    else:
      print(colours.fail("Database not hooked"))

  def read(self):
    if self.hooked:
      return self.data
    else:
      print(colours.fail("Database not hooked"))

  def write(self, data:dict):
    if self.hooked:
      self.data = data
      with open(self.path, "w") as f:
        f.write(json.dumps(self.data))
    else: 
      print(colours.fail("Database not hooked"))

  def delete(self):
    if self.hooked:
      print(colours.fail("Database is hooked, unhook it first"))
    else:
      if os.path.exists(self.path):
        os.remove(self.path)


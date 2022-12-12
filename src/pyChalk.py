class pyChalk:
  def __init__(self):
    self.colours = {
      'HEADER': '\033[95m',
      'OKBLUE': '\033[94m',
      'OKCYAN': '\033[96m',
      'OKGREEN':'\033[92m',
      'WARNING': '\033[93m',
      'FAIL': '\033[91m',
      'ENDC': '\033[0m',
      'BOLD': '\033[1m',
      'UNDERLINE': '\033[4m'
    }

  def header(self, string:str):
    return self.colours['HEADER'] + string + self.colours['ENDC']

  def blue(self, string:str):
    return self.colours['OKBLUE'] + string + self.colours['ENDC']

  def cyan(self, string:str):
    return self.colours['OKCYAN'] + string + self.colours['ENDC']

  def green(self, string:str):
    return self.colours['OKGREEN'] + string + self.colours['ENDC']

  def warn(self, string:str):
    return self.colours['WARNING'] + string + self.colours['ENDC']

  def fail(self, string:str):
    return self.colours['FAIL'] + string + self.colours['ENDC']

  def bold(self, string:str):
    return self.colours['BOLD'] + string + self.colours['ENDC']

  def underline(self, string:str):
    return self.colours['UNDERLINE'] + string + self.colours['ENDC']

import random,sys,copy
from optparse import OptionParser
try:
  import psyco
  psyco.full()
except ImportError:
  pass
 
class board:
  def __init__(self, list=None):
    if list == None:
      self.board = [[0 for i in range(0,8)] for j in range(0,8)]
      #inicialia rainas em lugares aleatorios
      for i in range(0,8):
        while 1:
          rand_row = random.randint(0,7)
          rand_col = random.randint(0,7)
          if self.board[rand_row][rand_col] == 0:
            self.board[rand_row][rand_col] = "-"
            break    
  
  def __repr__(self):
    mstr = ""
    for i in range(0,8):
      for j in range(0,8):
        mstr = mstr + str(self.board[i][j]) + " "
      mstr = mstr + "\n"
    return (mstr)
 
class queens:
  def __init__(self, numruns, verbocity, passedboard=None):
    self.totalruns = numruns
    self.totalsucc = 0
    self.totalnumsteps = 0
    self.verbocity = verbocity
    for i in range(0,numruns):
      if self.verbocity == True:
        print ("====================")
        print ("TABULEIRO",i)
        print ("====================")
      self.mboard = board(passedboard)
      self.cost = self.calc_cost(self.mboard)
      self.hill_solution()
 
  def hill_solution(self):
    while 1:
      currViolations = self.cost
      self.getlowercostboard()
      if currViolations == self.cost:
        break
      self.totalnumsteps += 1
      if self.verbocity == True:
        print ("Violações ----> ", self.calc_cost(self.mboard))
        print (self.mboard)
    if self.cost != 0:
      if self.verbocity == True:
        print ("RESOLVIDO!")
    else:
      if self.verbocity == True:
        print ("SEM SOLUÇÃO")
      self.totalsucc += 1
    return self.cost
 
  def printstats(self):
    print ("Total de Execuções: ", self.totalruns)
    print ("Total de Successos: ", self.totalsucc)
    print ("Porcentagem de sucesso: ", float(self.totalsucc)/float(self.totalruns))
    print ("Média de iterações: ", float(self.totalnumsteps)/float(self.totalruns))
 
  def calc_cost(self, tboard):
    
    totalhcost = 0
    totaldcost = 0
    for i in range(0,8):
      for j in range(0,8):
        if tboard.board[i][j] == "-":
          totalhcost -= 2
          for k in range(0,8):
            if tboard.board[i][k] == "-":
              totalhcost += 1
            if tboard.board[k][j] == "-":
              totalhcost += 1
          k, l = i+1, j+1
          while k < 8 and l < 8:
            if tboard.board[k][l] == "-":
              totaldcost += 1
            k +=1
            l +=1
          k, l = i+1, j-1
          while k < 8 and l >= 0:
            if tboard.board[k][l] == "-":
              totaldcost += 1
            k +=1
            l -=1
          k, l = i-1, j+1
          while k >= 0 and l < 8:
            if tboard.board[k][l] == "-":
              totaldcost += 1
            k -=1
            l +=1
          k, l = i-1, j-1
          while k >= 0 and l >= 0:
            if tboard.board[k][l] == "-":
              totaldcost += 1
            k -=1
            l -=1
    return ((totaldcost + totalhcost)/2)
 
  #essa unão tenta moer a raina pra qualquer lugar
  def getlowercostboard(self):
    lowcost = self.calc_cost(self.mboard)
    lowestavailable = self.mboard
    for q_row in range(0,8):
      for q_col in range(0,8):
        if self.mboard.board[q_row][q_col] == "-":
          for m_row in range(0,8):
            for m_col in range(0,8):
              if self.mboard.board[m_row][m_col] != "-":
                tryboard = copy.deepcopy(self.mboard)
                tryboard.board[q_row][q_col] = 0
                tryboard.board[m_row][m_col] = "-"
                thiscost = self.calc_cost(tryboard)
                if thiscost < lowcost:
                  lowcost = thiscost
                  lowestavailable = tryboard
    self.mboard = lowestavailable
    self.cost = lowcost
 
if __name__ == "__main__":
 
  parser = OptionParser()
  parser.add_option("-q", "--quiet", dest="verbose",
                   action="store_false", default=True,
                   help="Don't print all the moves... wise option if using large numbers")
 
  parser.add_option("--numrun", dest="numrun", help="Number of random Boards", default=1,
                   type="int")
 
  (options, args) = parser.parse_args()
 
  mboard = queens(verbocity=options.verbose, numruns=options.numrun)
  mboard.printstats()
import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.__dict__.update(kwargs)
    self.contents = []
    self.args = kwargs
    self.drawed_balls = []
    self.transfer()

  def transfer(self):
    for arg in self.args:
      c = self.args[arg]
      for i in range(c):
        self.contents.append(arg)

  def draw(self, number):
    if number > len(self.contents):
      return self.contents
    
    for i in range(number):
      random_num = random.randint(0, len(self.contents) - 1)
      self.drawed_balls.append(self.contents[random_num])
      self.contents.pop(random_num)
      
    return self.drawed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expected = []
  n = num_experiments
  for ball in expected_balls:
    expected.append({'name': ball, 'amount': expected_balls[ball]})

  n = num_experiments
  m = 0

  for i in range(num_experiments):
    drawed = hat.draw(num_balls_drawn)
    random.shuffle(drawed)
    got = []
    for dict in expected:
      count = drawed.count(dict['name'])
      got.append({'name': dict['name'], 'amount': count})

    count_got = 0
    for i in range(len(got)):
      dict_got = got[i]
      dict_ex = expected[i]
      if dict_got['amount'] >= dict_ex['amount']:
        count_got += 1
      else:
        count_got = 0
        break

    if count_got == len(got):
      m += 1
      

    for ball in hat.drawed_balls:
      hat.contents.append(ball)
    hat.drawed_balls = []

  
  probability = m / n
  return probability
  
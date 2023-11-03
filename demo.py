import seaborn as sns
import numpy as np
import pandas as pd

class customer(mesa.Agent):
  """A customer who want to rent an EV for mobility need"""
  def __init__(self, unique_id, model):
    super().__init__(unique_id, model)
    self.wealth = 1


class customerModel(mesa.Model):
  def __init__(self, N):
    """Number of customer agents"""
    self.num_agents = N
    """create agents"""
    for i in range(N):
      a = customer(i, self)

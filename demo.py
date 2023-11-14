import seaborn as sns
import numpy as np
import pandas as pd

class Customer(mesa.Agent):
  """A customer who want to rent an EV for mobility need"""
  def __init__(self, unique_id, model):
    super().__init__(unique_id, model)
    """ Agent's resource"""
    self.wealth = 1
  def step(self):
    print(f"Hi, I am an agent, you can call me {str(self.unique_id)}.")


class CustomerModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, N):
        self.num_agents = N
        # Create scheduler and assign it to the model
        self.schedule = mesa.time.RandomActivation(self)

        # Create agents
        for i in range(self.num_agents):
            a = Customer(i, self)
            # Add the agent to the scheduler
            self.schedule.add(a)

    def step(self):
        """Advance the model by one step."""

        # The model's step will go here for now this will call the step method of each agent and print the agent's unique_id
        self.schedule.step()

def calculateUserAge(user_birthdate,current_date):   # PEP8 naming violation
  age=current_date.year-user_birthdate.year        # Missing spaces around operators
  return age

class userManager:                                   # PEP8 class naming violation
  def __init__(self,name,age,role):               # Missing spaces after commas
    self.name=name                             # Wrong indentation (5 spaces instead of 4)
    self.age=age
    self.role=role

  def process_data(self,data):                    # Inconsistent spacing
    result = None                           # Over-indented
    try:
      result = self.complex_operation(data)
    except Exception as e:                   # Too broad exception
      print(f"Error: {e}")                # Using print instead of logging
    return result                           # Inconsistent return placement

  def complex_operation(self, data):              # Example of cyclomatic complexity
    status = None
    if data.is_valid():
      if data.has_permission:
        if self.role == 'admin':
          if data.size > 0:
            if data.format == 'json':
              status = self.process_json(data)
            else:
              status = self.process_other(data)
          else:
            status = 'empty_data'
        else:
          status = 'permission_denied'
      else:
        status = 'invalid_permission'
    else:
      status = 'invalid_data'
    return status

from typing import List,Dict,Any                    # Missing spaces after commas in imports
import os, sys, json                               # Multiple imports on one line
from ..utils import *                              # Wildcard import

class DataProcessor():                             # Empty parentheses not needed
  def __init__(self):
    self.data=[]                              # Missing space around operator
    self.processed=False                       # Missing space around operator

  def add_data(self,item:Any)->None:            # Missing space after comma, inconsistent type hint spacing
    self.data.append(item)

  def process(self)->List[Dict]:                # Incomplete type hint
    for i in range(len(self.data)):           # Non-Pythonic loop
      item=self.data[i]
      # TODO: Implement processing           # TODO comment without issue reference
    self.processed=True
    return [{'item':x} for x in self.data]    # Missing spaces in dict


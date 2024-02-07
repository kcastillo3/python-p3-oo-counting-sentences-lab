#!/usr/bin/env python3
class MyString:
  def __init__(self, value=''):
      self._value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, new_value):
    self.new_value = new_value
    if not isinstance (new_value,str):
      print("The value must be a string.")
    else:
      self._value = new_value

  def is_sentence(self):
    return self.value.endswith('.')

  def is_question(self):
    return self.value.endswith('?')

  def is_exclamation(self):
    return self.value.endswith('!')

  def count_sentences(self):
    temp_value = self.value.replace('!', '.').replace('?', '.')
    potential_sentences = temp_value.split('.')
    actual_sentences = [sentence for sentence in potential_sentences if sentence.strip()]
    return len(actual_sentences)

    





 


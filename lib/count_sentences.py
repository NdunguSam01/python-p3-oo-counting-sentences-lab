#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self._value=None
    self.value=value

  def get_value(self):
    return self._value
    
  def set_value(self, value):
    if type(value) == str:
      self._value=value
    else:
      print("The value must be a string.")

  value=property(get_value, set_value) 

  def is_sentence(self):
    if type(self.value)== str:
      return self.value.endswith(".")
    else:
      print("The value must be a string.")
  
  def is_question(self):
    if type(self.value)  == str:
      return self.value.endswith("?")
    else:
      print("The value must be a string.")
  
  def is_exclamation(self):
    if type(self.value)  == str:
      return self.value.endswith("!")
    else:
      print("The value must be a string.")
  
  def count_sentences(self):
      if type(self.value) == str:
        # Replace '!' and '?' with '.' to make it easier to split sentences
        modified_value = self.value.replace('!', '.').replace('?', '.')

        # Split the modified value into sentences using '.' as the separator
        sentences = modified_value.split('.')
          
        # Filter out empty strings resulting from consecutive periods
        complete_sentences=[sentence.strip() for sentence in sentences if sentence.strip()]
        return len(complete_sentences)
      
      else:
        print("The value must be a string.")


string=MyString(1234)
string.is_sentence()

new_string = MyString("This is a string! It has three sentences. Right?")
print(new_string.count_sentences()) 

simple_string = MyString("one. two. three?")
print(simple_string.count_sentences())

empty_string = MyString()
print(empty_string.count_sentences())

complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
print(complex_string.count_sentences())
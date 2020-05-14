from Section19_Observer.PropertiesObserver.PropertyObservable import PropertyObservable


class Person(PropertyObservable):
  def __init__(self, age=0):
    super().__init__()
    self._age = age

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, value):
    if self._age == value:
      return
    self._age = value
    self.property_changed('age', value)

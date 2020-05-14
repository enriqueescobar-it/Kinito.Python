from Section19_Observer.DependenciesObserver.PropertyObservable import PropertyObservable


class Person(PropertyObservable):
  def __init__(self, age=0):
    super().__init__()
    self._age = age

  @property
  def can_vote(self):
    return self._age >= 18

  @property
  def age(self):
    return self._age

  # @age.setter
  # def age(self, value):
  #   if self._age == value:
  #     return
  #   self._age = value
  #   self.property_changed('age', value)

  @age.setter
  def age(self, value):
    if self._age == value:
      return

    old_can_vote = self.can_vote

    self._age = value
    self.property_changed('age', value)

    if old_can_vote != self.can_vote:
      self.property_changed('can_vote', self.can_vote)

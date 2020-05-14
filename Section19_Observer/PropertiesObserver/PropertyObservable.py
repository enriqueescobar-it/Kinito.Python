from Section19_Observer.PropertiesObserver.Event import Event


class PropertyObservable:
  def __init__(self):
    self.property_changed = Event()

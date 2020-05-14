from Section19_Observer.DependenciesObserver.Event import Event


class PropertyObservable:
  def __init__(self):
    self.property_changed = Event()

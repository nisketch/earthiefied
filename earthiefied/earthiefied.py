"""Main module."""
import ipyleaflet

class  map(ipyleaflet.Map):
    
 def _init_(self, kwargs):
    super()._init_(**kwargs)
    self.add_control(ipyleaflet.LayersControl())
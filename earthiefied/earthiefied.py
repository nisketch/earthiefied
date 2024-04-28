"""Main module."""
from typing import Self
import ipyleaflet

class  map(ipyleaflet.Map):
    
 def _init_(self, kwargs):
    super()._init_(**kwargs)
    Self.add_control(ipyleaflet.LayersControl())
# So the goal here is to have a catalog of all the items in your game
# To correctly generate a games items they need to be bundled in a list
# A list in programming terms is anything in square brackets [] to put it simply

# When a list is described its described as a list of x where x is the type of variable within it
# IE: ["apple", "pear", "grape"] is a list of strings (anything inside "" OR '' are considered strings)

# Logging = output. How you'll figure out whats going wrong
import logging

# Built in AP imports
from BaseClasses import Item, ItemClassification

# These come from the other files in this example. If you want to see the source ctrl + click the name 
from .Types import ItemData
from typing import List, Dict, TYPE_CHECKING

# This is just making sure nothing gets confused dw about what its doing exactly
if TYPE_CHECKING:
    from . import APSkeletonWorld

def create_itempool(world: "APSkeletonWorld") -> List[Item]:

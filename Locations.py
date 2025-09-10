# Look at init or Items.py for more information on imports
from typing import Dict, TYPE_CHECKING
import logging

from .Types import LocData

if TYPE_CHECKING:
    from . import APSkeletonWorld

# This is technique in programming to make things more readable for booleans
# A boolean is true or false
def did_include_extra_locations(world: "APSkeletonWorld") -> bool:
    return bool(world.options.ExtraLocations)

# This is used by ap and in Items.py
# Theres a multitude of reasons to need to grab how many locations there are
def get_total_locations(world: "APSkeletonWorld") -> int:
    # This is the total that we'll keep updating as we count how many locations there are
    total = 0
    for name in location_table:
        # If we did not turn on extra locations (see how readable it is with that thing from the top)
        # AND the name of it is found in our extra locations table, then that means we dont want to count it
        # So continue moves onto the next name in the table
        if not did_include_extra_locations(world) and name in extra_locations:
            continue

        # If the location is valid though, count it
        if is_valid_location(world, name):
            total += 1

    return total

def get_location_names() -> Dict[str, int]:
    # This is just a fancy way of getting all the names and data in the location table and making a dictionary thats {name, code}
    # If you have dynamic locations then you want to add them to the dictionary as well
    names = {name: data.ap_code for name, data in location_table.items()}

    return names

# The check to make sure the location is valid
# I know it looks like the same as when we counted it but thats because this is an example
# Things get complicated fast so having a back up is nice
def is_valid_location(world: "APSkeletonWorld", name) -> bool:
    if not did_include_extra_locations(world) and name in extra_locations:
        return False
    
    return True

# You might need more functions as well so be liberal with them
# My advice, if you are about to type the same thing in a second time, turn it into a function
# Even if you only do it once you can turn it into a function too for organization

# Heres where you do the next fun part of listing out all those locations
# Its a lot
# My advice, zone out for half an hour listening to music and hope you wake up to a completed list
ap_skeleton_locations = {
    # You can take a peak at Types.py for more information but,
    # LocData is code, region in this instance
    # Regions will be explained more in Regions.py
    # But just know that it's mostly about organization
    # Place locations together based on where they are in the game and what is needed to get there


    # Comments are only used to say where the cubes are in order to help with logic, not to assign items to cubes

    #0 Cubes (Villageville)
    "Cube 1": LocData(20050100, "Villageville"),
    "Cube 2": LocData(20050101, "Villageville"), #bits
    "Anti-Cube 1": LocData(20050102, "Villageville"), #Mayor McMayor's house
    "Anti-Cube 2": LocData(20050103, "Villageville"), #Boiler room; Requires 1 key and First person
    "Villageville - Island Chest": LocData(20050104, "Villageville"),
    "Villageville - Mayor McMayor Fireplace Chest": LocData(20050105, "Villageville"),
    "Villageville - Boiler Room Map": LocData(20050106, "Villageville"), #Boiler Room; Requires 1 key

    #2 Cubes (Natural Region) 4

    # 1 Anti-Cube
    # left off at: Nature Hub -> Bell Tower
    
    
    
}

extra_locations = {
    "ml7's house": LocData(20050102, "Sibiu"),
}

# Like in Items.py, breaking up the different locations to help with organization and if something special needs to happen to them
event_locations = {
    "Beat Final Boss": LocData(20050110, "Big Hole in the Floor")
}

# Also like in Items.py, this collects all the dictionaries together
# Its important to note that locations MUST be bigger than progressive item count and should be bigger than total item count
# Its not here because this is an example and im not funny enough to think of more locations
# But important to note
location_table = {
    **ap_skeleton_locations,
    **extra_locations,
    **event_locations
}

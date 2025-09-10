from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, Range

# If youve ever gone to an options page and seen how sometimes options are grouped
# This is that
def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in ap_skeleton_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list

class IncludeKeys(Toggle):
    """
    Determines whether keys will be added to the item pool.
    """
    display_name = "Include Keys"

class IncludeOwls(Toggle):
    """
    Determines whether owls will be added to the item pool.
    """
    display_name = "Include Owls"

class IncludeMaps(Toggle):
    """
    Determines whether maps will be added to the item pool.
    """
    display_name = "Include Maps"

#in TODO it says "3D vision", I'm going to assume that means first person camera
#TODO: when it's disabled should it default in inventory on start or to first game completion? I might make it an option later.
class IncludeFirstPerson(Toggle):
    """
    Determines whether the first person camera will be added to the item pool.
    """
    display_name = "Include First Person"

class TrapAmount(Range):
    """
    How much junk to replace with rotation traps, percentage-wise.
    """
    display_name = "Speed Change Trap Weight"
    range_start = 0
    range_end = 100
    default = 20 #this is an estimate

class Deathlink(Toggle):
    """
    Enables Deathlink.
    """
    display_name = "Deathlink"

#I'm using the Apworld skeleton, and currently I have no idea what this does
@dataclass
class APSkeletonOptions(PerGameCommonOptions):
    StartingChapter:            StartingChapter
    ExtraLocations:             ExtraLocations
    TrapChance:                 TrapChance
    ForcefemTrapWeight:         ForcefemTrapWeight
    SpeedChangeTrapWeight:      SpeedChangeTrapWeight

# This is where you organize your options
# Its entirely up to you how you want to organize it
ap_skeleton_option_groups: Dict[str, List[Any]] = {
    "Check Options": [IncludeKeys, IncludeOwls, IncludeMaps, IncludeFirstPerson],
    "Other Options": [TrapAmount, Deathlink]
}

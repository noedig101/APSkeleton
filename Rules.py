from worlds.generic.Rules import add_rule, set_rule
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import APSkeletonWorld

# This is the last big thing to do (at least for me)
# This is where you add item
def set_rules(world: "APSkeletonWorld"):
    player = world.player
    options = world.options

    # Chapter Access
    add_rule(world.multiworld.get_entrance("Menu -> Green Hill Zone", player),
             lambda state: state.has("Green Hill Zone", player))
    add_rule(world.multiworld.get_entrance("Menu -> Romania", player),
             lambda state: state.has("Romania", player))
    add_rule(world.multiworld.get_entrance("Menu -> The Sewer", player),
             lambda state: state.has("The Sewer", player))
    
    add_rule(world.multiworld.get_entrance("The Sewer -> Big Hole in the Floor", player),
             lambda state: state.has("A cute rat") and state.has("Estrogen") and state.has("Testosterone"))
    
    world.multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
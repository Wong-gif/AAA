# game setup
WIDTH    = 1200
HEIGTH   = 800
FPS      = 60
TILESIZE = 64

#ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = "graphics_qx/font/joystix.ttf"
UI_FONT_SIZE = 18

#general colour
WATER_COLOUR = "#71ddee"
UI_BG_COLOUR = "#222222"
UI_BORDER_COLOUR = "#111111"
TEXT_COLOUR = "#EEEEEE"

#ui colours 
HEALTH_COLOUR = "red"
ENERGY_COLOUR = "blue"
UI_BORDER_COLOUR_ACTIVE = "gold"

#weapons
weapons_data = {
    "lance" : {"cooldown" : 400, "damage" : 30, "graphic" : "graphics_qx/weapons_farming/lance/full.png"},
    "axe" : {"cooldown" : 300, "damage" : 20, "graphic" : "graphics_qx/weapons_farming/axe/full.png"},
    "rapier" : {"cooldown" : 50, "damage" : 8, "graphic" : "graphics_qx/weapons_farming/rapier/full.png"}
}

#magic
magic_data = {
    "flame" : {"strength": 5, "cost": 20, "graphic": "graphics_qx/special_effects_farming/flame/fire.png"},
    "heal" : {"strength": 20, "cost": 10, "graphic": "graphics_qx/special_effects_farming/heal/heal.png"}
}
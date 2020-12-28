# https://github.com/mide/minecraft-overviewer/blob/master/config/config.py
import os
from observer import MultiplexingObserver, LoggingObserver, JSObserver

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/{}".format(poi['EntityId'])
        return "Last known location for {}".format(poi['EntityId'])


# Only signs with "-- RENDER --" in them, and no others. Otherwise, people
# can't have secret bases and the render is too busy anyways.
def signFilter(poi):
    if poi['id'] in ['Sign', 'minecraft:sign']:
        if '-- RENDER --' in poi.values():
            return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])

worlds['Day'] = "/home/minecraft/server/world"
worlds['Night'] = "/home/minecraft/server/world"
outputdir = "/home/minecraft/render/"
texturepath = "/home/minecraft/{}.jar".format(os.environ['MINECRAFT_VERSION'])

# Construct the LoggingObserver
loggingObserver = LoggingObserver()

# Construct a basic JSObserver
jsObserver = JSObserver(outputdir) # This assumes you have set the outputdir previous to this line

# Set the observer to a MultiplexingObserver
observer = MultiplexingObserver(loggingObserver, jsObserver)

markers = [
    dict(name="Players", filterFunction=playerIcons),
    dict(name="Signs", filterFunction=signFilter)
]

renders["day_nw"] = {
    'world': 'Day',
    'title': 'North West',
    'rendermode': 'smooth_lighting',
    "dimension": "overworld",
    'markers': markers,
    "northdirection": "upper-left"
}

renders["day_ne"] = {
    'world': 'Day',
    'title': 'North East',
    'rendermode': 'smooth_lighting',
    "dimension": "overworld",
    'markers': markers,
    "northdirection": "upper-right"
}

renders["day_sw"] = {
    'world': 'Day',
    'title': 'South West',
    'rendermode': 'smooth_lighting',
    "dimension": "overworld",
    'markers': markers,
    "northdirection": "lower-left"
}

renders["day_se"] = {
    'world': 'Day',
    'title': 'South East',
    'rendermode': 'smooth_lighting',
    "dimension": "overworld",
    'markers': markers,
    "northdirection": "lower-right"
}

renders["night_nw"] = {
    'world': 'Night',
    'title': 'North West',
    'rendermode': 'smooth_night',
    "dimension": "overworld",
    'markers': markers,
    "northdirection": "upper-left"
}

renders["night_ne"] = {
    'world': 'Night',
    'title': 'North East',
    'rendermode': 'smooth_night',
    "dimension": "overworld",
    'markers': markers,
    "northdirection": "upper-right"
}

renders["night_sw"] = {
    'world': 'Night',
    'title': 'South West',
    'rendermode': 'smooth_night',
    "dimension": "overworld",
    'markers': markers,
    "northdirection": "lower-left"
}

renders["night_se"] = {
    'world': 'Night',
    'title': 'South East',
    'rendermode': 'smooth_night',
    "dimension": "overworld",
    'markers': markers,
    "northdirection": "lower-right"
}

# Only for Pixelmon
#renders["UltraSpace"] = {
#    'world': 'minecraft',
#    'title': 'North West',
#    'rendermode': [Base(), EdgeLines(), SmoothLighting(strength=0.5)],
#    "dimension": "UltraSpace",
#    'markers': markers,
#    "northdirection": "upper-left"
#}

#renders["cave"] = {
#    'world': 'minecraft',
#    'title': 'Underground',
#    'rendermode': [Base(), EdgeLines(opacity=0.2), Cave(only_lit=True), SmoothLighting(strength=0.5), NoFluids()],
#    "dimension": "overworld",
#    'markers': markers
#}

#renders["nether"] = {
#    "world": "minecraft",
#    "title": "Nether",
#    "rendermode": 'nether_smooth_lighting',
#    "dimension": "nether",
#    'markers': markers
#}

#renders["end"] = {
#    "world": "minecraft",
#    "title": "End",
#    "rendermode": [Base(), EdgeLines(), SmoothLighting(strength=0.5)],
#    "dimension": "end",
#    'markers': markers
#}

#renders["overlay_biome"] = {
#    'world': 'minecraft',
#    'rendermode': [ClearBase(), BiomeOverlay()],
#    'title': "Biome Coloring Overlay",
#    "dimension": "overworld",
#    'overlay': ["day_nw"]
#}

#renders["overlay_mobs"] = {
#    'world': 'minecraft',
#    'rendermode': [ClearBase(), SpawnOverlay()],
#    'title': "Mob Spawnable Areas Overlay",
#    "dimension": "overworld",
#    'overlay': ["day_nw"]
#}

#renders["overlay_slime"] = {
#    'world': 'minecraft',
#    'rendermode': [ClearBase(), SlimeOverlay()],
#    'title': "Slime Chunk Overlay",
#    "dimension": "overworld",
#    'overlay': ["day"]
#}

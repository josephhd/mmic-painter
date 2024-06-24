import matplotlib.pyplot as pyplot
from matplotlib import cm
# from matplotlib.patches import Polygon
import matplotlib.patches as mpatches
import numpy as np

from gdspy import *


#######################################################################################################
### CONFIG HERE ###

# if you have a style guide, you can import it here, otherwise comment this line
pyplot.style.use('style.mplstyle')

# Load a GDSII file into a new library
file = 'georgia_oscillator.gds'

# configure figure size (in inches)
fig, ax = pyplot.subplots(figsize=(3.5, 3))

# use matplotlib's built in colormap to define plot colors
# for color maps: https://matplotlib.org/stable/users/explain/colors/colormaps.html
color_list = np.linspace(0, 1, 20)
tab20 = [ cm.tab20(x) for x in color_list ]

colormap = tab20

# DEFINE LAYER COLORS HERE
# to see the layers in a given dxf file, see lines 129-130
color_dict = {
    # bond pads
    302 : colormap[5], # DM_BondPad
    305 : colormap[5], # DM_RFPAD
    304 : colormap[5], # DM_DCPAD
    
    # caps and inductors
    48  : colormap[0], # du_cap
    # 126 : colormap[1], # du_ind
    
    # via layers
    13 : colormap[6], # backvia
    8  : colormap[6], # via1
    10 : colormap[6], # via2

    # metal layers
    9  : colormap[14], # met1
    11 : colormap[15], # met2

    
    # transistor layers
    31 : colormap[12], # TOBI
    1  : colormap[7],  # mesa

    # resistor layers
    7 : colormap[3], # TFR

    # other
    # 6  : colormap[6], # ohmic
    # 17 : colormap[19],# span
}

# DEFINE LAYER DRAWING ORDER HERE (lower values drawn first) if a layer is not included here, it will not be drawn
order_dict = {
    302 : 5, # DM_BondPad
    305 : 4, # DM_RFPAD
    304 : 3, # DM_DCPAD

    48 : 4,  # du_cap
    
    13 : 3,  # backvia
    
    9  : 0, # met1
    11 : 1, # met2
    
    31 : 6, # TOBI
    1  : 5, # mesa

    7 : 2   # TFR
}

# DEFINE LAYER LEGEND NAMES HERE
legend_names = {
    302    : "Bond Pad",   # DM_BondPAD
    9      : "Metal 1",    # met1
    11     : "Metal 2",    # met2
    48     : "Capacitor",  # du_cap
    13     : "Back Via",   # backvia
    31     : "TOBI",       # TOBI
    1      : "Mesa",       # mesa
    7      : "TFR"         # TFR
}

#######################################################################################################
gds = GdsLibrary(infile=file)

### Print GDS cell information ###
# for k, v in gds.cells.items():
    # print("GDS Cell Info:", k, v, "GDS Cell Layers: ", v.get_layers())

#######################################################################################################
polygon_dict = {}

for k, c in gds.cells.items():   
    polygons = c.get_polygons(by_spec=True)

    for k, shapes in polygons.items():
        layer = k[0]

        for s in shapes:
            if layer in color_dict.keys():
                p = mpatches.Polygon(s, closed=True, facecolor=color_dict[layer])

                if layer in polygon_dict.keys():
                    polygon_dict[layer].append(p)
                else:
                    polygon_dict[layer] = [p]

# convert order_dict to a sorted list of tuples, then iterate over the sorted list and draw the polygons in the specified draw order
polygons = []
sorted_order = sorted(order_dict.items(), key=lambda kv:kv[1])

for k,v in sorted_order:
    if k in polygon_dict.keys():
        polygons.extend(polygon_dict[k])
    else:
        print("Layer " + str(k) + " not found in dictionary.")

# draw polygons
for p in polygons:
    ax.add_patch(p)

# create legend
legend_handles = []
for k, v in legend_names.items():
    if k in color_dict.keys():
        legend_handles.append(mpatches.Patch(color=color_dict[k], label=v))

bbox = c.get_bounding_box()
ax.set_xlim([bbox[0, 0], bbox[1, 0]])
ax.set_ylim([bbox[0, 1], bbox[1, 1]])

#######################################################################################################
### Figure Styling ###
#######################################################################################################

ax.legend(handles=legend_handles, loc='center left', bbox_to_anchor=(1, 0.5))

ax.set_axis_off()
ax.axis('equal')
fig.tight_layout()

fig.savefig('figure.pdf', format='pdf', pad_inches=0, dpi=300)
# fig.savefig('figure.png', format='png', pad_inches=0, dpi=300)

pyplot.show()
# arcplot

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/szkics/arcplot/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/release)

[arcplot](https://pypi.org/project/arcplot/) is a library based on matplotlib for seamless creation of arc diagrams.

## usage

![alt text](https://raw.githubusercontent.com/szkics/arcplot/main/img/italian-railway.png)

```py
from arcplot import ArcDiagram

nodes = [
    "Rome",
    "Naples",
    "Florence",
    "Bari",
    "Taranto",
    "Verona",
    "Venice",
    "Bologna",
    "Bolzano",
    "Milan",
    "Turin",
    "Genoa",
]
title = "Railway connections between Italian cities"
arc_diagram = ArcDiagram(nodes, title)
custom_colors = [
    "#386641",
    "#f2e8cf",
    "#8b3422",
    "#6f7714",
    "#ff9b54",
    "#e2d9c5",
    "#9a8237",
    "#dbab85",
    "#d64620",
    "#f6bd60",
    "#283618",
    "#a98467",
]
arc_diagram.set_custom_colors(custom_colors)
arc_diagram.set_background_color("#262522")
arc_diagram.connect(
    "Milan", "Genoa", linewidth=119
)  # passing the distance in km between the two cities as arc linewidth
arc_diagram.connect("Milan", "Verona", linewidth=140)
arc_diagram.connect("Milan", "Turin", linewidth=126)
arc_diagram.connect("Milan", "Bologna", linewidth=201)
arc_diagram.connect("Rome", "Genoa", linewidth=403)
arc_diagram.connect("Rome", "Florence", linewidth=232)
arc_diagram.connect("Rome", "Naples", linewidth=189)
arc_diagram.connect("Rome", "Bari", linewidth=375)
arc_diagram.connect("Florence", "Genoa", linewidth=200)
arc_diagram.connect("Florence", "Bologna", linewidth=80)
arc_diagram.connect("Naples", "Taranto", linewidth=252)
arc_diagram.connect("Naples", "Bari", linewidth=219)
arc_diagram.connect("Venice", "Verona", linewidth=120)
arc_diagram.connect("Venice", "Bologna", linewidth=131)
arc_diagram.connect("Bolzano", "Verona", linewidth=122)
arc_diagram.connect("Bari", "Taranto", linewidth=78)
arc_diagram.connect("Genoa", "Turin", linewidth=122)
arc_diagram.show_plot()
```

![alt text](https://raw.githubusercontent.com/szkics/arcplot/main/img/the-office.png)

```py
nodes = [
    "Angela",
    "Pam",
    "Karen",
    "Holly",
    "Kelly",
    "Jan",
    "Michael",
    "Jim",
    "Andy",
    "Roy",
    "Ryan",
    "Darrel",
    "Dwight",
]
title = "The Office relationships"
arc_diagram = ArcDiagram(nodes, title)
arc_diagram.set_color_map("Pastel2")
arc_diagram.set_background_color("black")
arc_diagram.connect("Pam", "Jim")
arc_diagram.connect("Pam", "Roy")
arc_diagram.connect("Michael", "Holly")
arc_diagram.connect("Michael", "Jan")
arc_diagram.connect("Karen", "Jim")
arc_diagram.connect("Kelly", "Ryan")
arc_diagram.connect("Kelly", "Darrel")
arc_diagram.connect("Angela", "Dwight")
arc_diagram.connect("Angela", "Andy")
arc_diagram.connect("Jim", "Roy", arc_position="below")
arc_diagram.connect("Jim", "Dwight", arc_position="below")
arc_diagram.connect("Andy", "Dwight", arc_position="below")
arc_diagram.save_plot_as("the-office.png", resolution="300") # resolution is optional, defaults to 'figure'
```

![alt text](https://raw.githubusercontent.com/szkics/arcplot/main/img/the-good.png)


```py
nodes = ["The Good", "The Bad", "The Ugly"]
title = "Characters pointing guns at each other in Sergio Leone's film"
arc_diagram = ArcDiagram(nodes, title)
arc_diagram.set_background_color("#c7a27d")
arc_diagram.connect("The Good", "The Bad")
arc_diagram.connect("The Good", "The Ugly")
arc_diagram.connect("The Ugly", "The Bad")
arc_diagram.show_plot()
```

## function list

```py
ArcDiagram(nodes, title) # for initializing an ArcDiagram the entities to connect and the title is required.
.set_background_color(string) # for setting background color of the matplotlib figure.
.set_color_map(string) # for setting color map, choose from: https://matplotlib.org/stable/users/explain/colors/colormaps.html
.set_custom_colors(color_list) # for setting colors of nodes from a custom color list, 
# the length of the color list must be the same as the length of the node list.
.connect(start, end, linewidth=100, arc_position="below") # for creating an arc between two entities
# optional parameter linewidth sets linewidth proportionally to other arc linewidths.
# arc_position="below" draws arc below the x axis, default is "above". 
.show_plot() # for checking the results of the data visualization process.
.save_plot_as(file_name, resolution="100") # for saving file as an image with an optional resolution setting for higher-quality images.
```

## installation

```bash
pip install arcplot
```
# arcplot

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/szkics/arcplot/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/release)
[![Downloads](https://static.pepy.tech/badge/Arcplot)](https://pepy.tech/project/Arcplot)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/szkics/arcplot)

[arcplot](https://pypi.org/project/arcplot/) is a library based on matplotlib for seamless creation of custom arc diagrams.

## usage

![alt text](https://raw.githubusercontent.com/szkics/arcplot/main/img/italian-railway-connections.png)

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
arc_diagram.set_label_rotation_degree(45)
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

![alt text](https://raw.githubusercontent.com/szkics/arcplot/main/img/painters.png)

```py
title = "Friendships Between Post-, Neo- and Impressionist Painters"
nodes = [
    "Vincent van Gogh",
    "Paul Gauguin",
    "Eugène Boch",
    "Émile Bernard",
    "Louis Anquetin",
    "Henri de Toulouse-Lautrec",
    "Paul Cézanne",
    "Paul Signac",
    "Georges Seurat",
    "Camille Pissarro",
    "Edgar Degas",
    "Édouard Manet",
    "Claude Monet",
    "Pierre-Auguste Renoir",
]

connections = [
    ("Vincent van Gogh", "Paul Gauguin"),
    ("Vincent van Gogh", "Émile Bernard"),
    ("Vincent van Gogh", "Eugène Boch"),
    ("Vincent van Gogh", "Paul Signac"),
    ("Vincent van Gogh", "Henri de Toulouse-Lautrec"),
    ("Vincent van Gogh", "Louis Anquetin"),
    ("Vincent van Gogh", "Paul Cézanne"),
    ("Paul Gauguin", "Émile Bernard"),
    ("Paul Gauguin", "Eugène Boch"),
    ("Émile Bernard", "Eugène Boch"),
    ("Émile Bernard", "Henri de Toulouse-Lautrec"),
    ("Émile Bernard", "Louis Anquetin"),
    ("Émile Bernard", "Paul Cézanne"),
    ("Henri de Toulouse-Lautrec", "Louis Anquetin"),
    ("Henri de Toulouse-Lautrec", "Paul Signac"),
    ("Paul Signac", "Georges Seurat"),
    ("Paul Signac", "Camille Pissarro"),
    ("Camille Pissarro", "Paul Cézanne"),
    ("Camille Pissarro", "Paul Gauguin"),
    ("Camille Pissarro", "Vincent van Gogh"),
    ("Camille Pissarro", "Georges Seurat"),
    ("Camille Pissarro", "Paul Signac"),
    ("Camille Pissarro", "Édouard Manet"),
    ("Camille Pissarro", "Claude Monet"),
    ("Camille Pissarro", "Pierre-Auguste Renoir"),
    ("Camille Pissarro", "Edgar Degas"),
    ("Claude Monet", "Paul Signac"),
    ("Claude Monet", "Pierre-Auguste Renoir"),
    ("Claude Monet", "Édouard Manet"),
    ("Édouard Manet", "Pierre-Auguste Renoir"),
    ("Édouard Manet", "Edgar Degas"),
]
arc_diagram_painters = ArcDiagram(nodes, title)

arc_diagram_painters.set_label_rotation_degree(80)
arc_diagram_painters.set_legend_labels(
    ["Post-Impressionist", "Neo-Impressionist", "Impressionist"]
)

for connection in connections:
    arc_diagram_painters.connect(connection[0], connection[1])

arc_diagram_painters.set_background_color("black")
arc_diagram_painters.set_color_map("summer")
arc_diagram_painters.save_plot_as("painters.png")
```

![alt text](https://raw.githubusercontent.com/szkics/arcplot/main/img/back_to_the_future.png)


```py
nodes = [
    "1885",
    "1955",
    "1985",
    "1985A",
    "2015",
]

title = "Back To The Future Time Travels \n Top: Back To The Future \n Bottom: Back To The Past"
arc_diagram = ArcDiagram(nodes, title)
arc_diagram.set_background_color("#222124")
arc_diagram.set_color_map("autumn")
arc_diagram.connect("1885", "1985")
arc_diagram.connect("1955", "1985")
arc_diagram.connect("1985", "2015")
arc_diagram.connect("2015", "1985A", arc_position="below")
arc_diagram.connect("2015", "1955", arc_position="below")
arc_diagram.connect("1985", "1955", arc_position="below")
arc_diagram.connect("1985A", "1955", arc_position="below")
arc_diagram.connect("1955", "1885", arc_position="below")
arc_diagram.save_plot_as("back_to_the_future.png")
```

## function list

```py
ArcDiagram(nodes, title) # for initializing an ArcDiagram the entities to connect and the title is required.
.set_background_color(string) # for setting background color of the matplotlib figure.
.set_color_map(string) # for setting color map, choose from: https://matplotlib.org/stable/users/explain/colors/colormaps.html
.set_custom_colors(color_list) # for setting colors of nodes from a custom color list, 
# the length of the color list must be the same as the length of the node list.
.set_label_rotation_degree(45) # rotates the labels in 45 degree, default is 0.
.set_legend_labels(list_of_labels) # adds a legend to the plot with configurable labels.
.connect(start, end, linewidth=100, arc_position="below") # for creating an arc between two entities
# optional parameter linewidth sets linewidth proportionally to other arc linewidths.
# arc_position="below" draws arc below the x axis, default is "above". 
.show_plot() # for checking the results of the data visualization process.
.save_plot_as(file_name, resolution="100") # for saving file as an image with an optional resolution setting for higher-quality images.
```

## installation

```bash
pip install arcplot==0.1.3
```
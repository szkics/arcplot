# arcplot

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/szkics/arcplot/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/release)

arcplot is a library based on matplotlib for seamless creation of arc diagrams.

## usage

```py
from arcplot import ArcDiagram

nodes = ["The Good", "The Bad", "The Ugly"]
title = "Characters pointing guns at each other in Sergio Leone's film"
arc_diagram = ArcDiagram(nodes, title)
arc_diagram.set_background_color("#c7a27d")
arc_diagram.connect("The Good", "The Bad")
arc_diagram.connect("The Good", "The Ugly")
arc_diagram.connect("The Ugly", "The Bad")
arc_diagram.show_plot()
```

![alt text](https://raw.githubusercontent.com/szkics/arcplot/main/img/the-good.png?token=GHSAT0AAAAAACNTK4WQAFBU5WC324BUT3SMZOMMLZQ)


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
arc_diagram.save_plot_as("the-office.png", resolution="300") # resolution is optional, defaults to 'figure'
```

![alt text](https://raw.githubusercontent.com/szkics/arcplot/main/img/the-office.png?token=GHSAT0AAAAAACNTK4WRC5YHOB45DMKKFHTCZOMML2A)

## function list

```py
ArcDiagram(nodes, title) # for initializing an ArcDiagram the entities to connect and the title is required.
.set_background_color(string) # for setting background color of the matplotlib figure.
.set_color_map(string) # for setting color map, choose from: https://matplotlib.org/stable/users/explain/colors/colormaps.html
.connect(start, end) # for creating an arc between two entities.
.show_plot() # for checking the results of the data visualization process.
.save_plot_as(file_name, resolution="100") # for saving file as an image with an optional resolution setting for higher-quality images.
```

## installation

```bash
pip install arcplot
```
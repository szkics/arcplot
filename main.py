from arcplot import ArcDiagram, show_arc_plot, save_arc_plot_as
import pandas as pd

df = pd.read_csv("./data/connections-dataset.csv")
show_arc_plot(
    df, start_node="from", end_node="to", weights="weights", positions="position"
)
save_arc_plot_as(
    df,
    start_node="from",
    end_node="to",
    weights="weights",
    positions="position",
    title="Connections",
    file_name="./img/connections.png",
)

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
arc_diagram.save_plot_as("./img/italian-railway-connections.png")

nodes = [
    "1885",
    "1955",
    "1985",
    "1985A",
    "2015",
]

title = "Back To The Future Time Travels \n Top: Back To The Future \n Bottom: Back To The Past"
time_travels = ArcDiagram(nodes, title)
time_travels.set_background_color("#222124")
time_travels.set_color_map("autumn")
time_travels.connect("1885", "1985")
time_travels.connect("1955", "1985")
time_travels.connect("1985", "2015")
time_travels.connect("2015", "1985A", arc_position="below")
time_travels.connect("2015", "1955", arc_position="below")
time_travels.connect("1985", "1955", arc_position="below")
time_travels.connect("1985A", "1955", arc_position="below")
time_travels.connect("1955", "1885", arc_position="below")
time_travels.save_plot_as("./img/back_to_the_future.png")

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
impressionist_painters = ArcDiagram(nodes, title)

impressionist_painters.set_label_rotation_degree(80)
impressionist_painters.set_legend_labels(
    ["Post-Impressionist", "Neo-Impressionist", "Impressionist"]
)

for connection in connections:
    impressionist_painters.connect(connection[0], connection[1])

impressionist_painters.set_background_color("black")
impressionist_painters.set_color_map("summer")
impressionist_painters.save_plot_as("./img/painters.png")

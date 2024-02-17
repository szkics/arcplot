from arcplot import ArcDiagram

nodes = ["The Good", "The Bad", "The Ugly"]
title = "Characters pointing guns at each other in Sergio Leone's film"
arc_diagram = ArcDiagram(nodes, title)
arc_diagram.set_background_color("#c7a27d")
arc_diagram.connect("The Good", "The Bad")
arc_diagram.connect("The Good", "The Ugly")
arc_diagram.connect("The Bad", "The Ugly")
arc_diagram.save_plot_as("the-good.png")

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
arc_diagram.save_plot_as("the-office.png")

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
title = "Railway connection between Italian cities"
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
arc_diagram.set_background_color("black")
arc_diagram.connect("Milan", "Genoa", thickness=119)
arc_diagram.connect("Milan", "Verona", thickness=140)
arc_diagram.connect("Milan", "Turin", thickness=126)
arc_diagram.connect("Milan", "Bologna", thickness=201)
arc_diagram.connect("Rome", "Genoa", thickness=403)
arc_diagram.connect("Rome", "Florence", thickness=232)
arc_diagram.connect("Rome", "Naples", thickness=189)
arc_diagram.connect("Rome", "Bari", thickness=375)
arc_diagram.connect("Florence", "Genoa", thickness=200)
arc_diagram.connect("Florence", "Bologna", thickness=80)
arc_diagram.connect("Naples", "Taranto", thickness=252)
arc_diagram.connect("Naples", "Bari", thickness=219)
arc_diagram.connect("Venice", "Verona", thickness=120)
arc_diagram.connect("Venice", "Bologna", thickness=131)
arc_diagram.connect("Bolzano", "Verona", thickness=122)
arc_diagram.connect("Bari", "Taranto", thickness=78)
arc_diagram.connect("Genoa", "Turin", thickness=122)
arc_diagram.save_plot_as("italian-railway.png")
# arc_diagram.show_plot()

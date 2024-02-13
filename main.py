from arcplot import ArcDiagram

nodes = ["The Good", "The Bad", "The Ugly"]
title = "Characters pointing guns at each other in Sergio Leone's film"
arc_diagram = ArcDiagram(nodes, title)
arc_diagram.set_background_color("#c7a27d")
arc_diagram.connect("The Good", "The Bad")
arc_diagram.connect("The Good", "The Ugly")
arc_diagram.connect("The Ugly", "The Bad")
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
arc_diagram.save_plot_as("the-office.png")

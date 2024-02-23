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
arc_diagram.save_plot_as("italian-railway.png")

nodes = [
    "1885",
    "1955",
    "1985",
    "1985A",
    "2015",
]

title = "Back To The Future time travels - top: back to the future, bottom: back to the past"
arc_diagram = ArcDiagram(nodes, title)
arc_diagram.set_background_color("#222124")
arc_diagram.set_color_map("PuOr")
arc_diagram.connect("1885", "1985")
arc_diagram.connect("1955", "1985")
arc_diagram.connect("1985", "2015")
arc_diagram.connect("2015", "1985A", arc_position="below")
arc_diagram.connect("2015", "1955", arc_position="below")
arc_diagram.connect("1985", "1955", arc_position="below")
arc_diagram.connect("1985A", "1955", arc_position="below")
arc_diagram.connect("1955", "1885", arc_position="below")
arc_diagram.save_plot_as("back_to_the_future.png")

# nodes_collaboration = [
#     'Albert Einstein', 'Mileva Marić', 'Niels Bohr', 'Max Planck', 'David Hilbert',
#     'J. Robert Oppenheimer', 'Enrico Fermi', 'Hans Bethe', 'Leo Szilard', 'Edward Teller','Marie Curie',
# ]

# title = 'Collaborations Between Physicists'

# arc_diagram_scientists = ArcDiagram(nodes_collaboration, title)
# # arc_diagram_scientists.set_color_map('plasma')
# # arc_diagram_scientists.set_background_color('lightgray')
# arc_diagram_scientists.set_label_rotation_degree(90)

# connections_collaboration = [
#     (0, 1), (0, 2), (0, 3), (0, 4),  # Einstein's collaborations
#     (5, 6), (6, 7), (7, 5), (5, 8), (5, 9), # Oppenheimer's collaborations
#     (0, 10), (0, 8),  # Einstein's letters to Curie and Szilard
# ]

# for node1, node2 in connections_collaboration:
#     arc_diagram_scientists.connect(nodes_collaboration[node1], nodes_collaboration[node2])

# # # Connect nodes based on correspondences
# # arc_diagram_scientists.connect("Albert Einstein", "Leo Szilard")
# # arc_diagram_scientists.connect("Leo Szilard", "J. Robert Oppenheimer")
# # arc_diagram_scientists.connect("J. Robert Oppenheimer", "Niels Bohr")
# # arc_diagram_scientists.connect("Niels Bohr", "Werner Heisenberg")
# # arc_diagram_scientists.connect("Werner Heisenberg", "Erwin Schrödinger")
# # arc_diagram_scientists.connect("Erwin Schrödinger", "Max Planck")
# # arc_diagram_scientists.connect("Max Planck", "Enrico Fermi")
# # arc_diagram_scientists.connect("Enrico Fermi", "Richard Feynman")
# # arc_diagram_scientists.connect("Richard Feynman", "Marie Curie")
# # arc_diagram_scientists.connect("Marie Curie", "Albert Einstein")

# arc_diagram_scientists.show_plot()


title = "Friendships Between Impressionist, Post-Impressionist and Neo-Impressionist Painters"
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

arc_diagram_painters = ArcDiagram(nodes, title)

arc_diagram_painters.set_label_rotation_degree(90)

# arc_diagram_painters.connect("Vincent van Gogh", "Paul Gauguin")
# arc_diagram_painters.connect("Vincent van Gogh", "Émile Bernard")
# arc_diagram_painters.connect("Vincent van Gogh", "John Peter Russell")
# arc_diagram_painters.connect("Vincent van Gogh", "Henri de Toulouse-Lautrec")
# arc_diagram_painters.connect("Vincent van Gogh", "Paul Signac")
# arc_diagram_painters.connect("Vincent van Gogh", "Georges Seurat")
# arc_diagram_painters.connect("Vincent van Gogh", "Camille Pissarro")
# arc_diagram_painters.connect("Vincent van Gogh", "Paul Cézanne")
# arc_diagram_painters.connect("Vincent van Gogh", "Édouard Manet")
# arc_diagram_painters.connect("Vincent van Gogh", "Claude Monet")
# arc_diagram_painters.connect("Vincent van Gogh", "Pierre-Auguste Renoir")

# the four of the major Post-Impressionists: Cézanne, Seurat, Gauguin, and van Gogh.
arc_diagram_painters.connect("Vincent van Gogh", "Paul Gauguin")
arc_diagram_painters.connect("Vincent van Gogh", "Émile Bernard")
arc_diagram_painters.connect("Vincent van Gogh", "Eugène Boch")
arc_diagram_painters.connect("Vincent van Gogh", "Paul Signac")
# arc_diagram_painters.connect("Vincent van Gogh", "Camille Pissarro")
arc_diagram_painters.connect("Vincent van Gogh", "Henri de Toulouse-Lautrec")
arc_diagram_painters.connect("Vincent van Gogh", "Louis Anquetin")
arc_diagram_painters.connect("Vincent van Gogh", "Paul Cézanne")

arc_diagram_painters.connect("Paul Gauguin", "Émile Bernard")
# arc_diagram_painters.connect("Paul Gauguin", "Camille Pissarro")
arc_diagram_painters.connect("Paul Gauguin", "Eugène Boch")

arc_diagram_painters.connect("Émile Bernard", "Eugène Boch")
arc_diagram_painters.connect("Émile Bernard", "Henri de Toulouse-Lautrec")
arc_diagram_painters.connect("Émile Bernard", "Louis Anquetin")
arc_diagram_painters.connect("Émile Bernard", "Paul Cézanne")

arc_diagram_painters.connect("Henri de Toulouse-Lautrec", "Louis Anquetin")
arc_diagram_painters.connect("Henri de Toulouse-Lautrec", "Paul Signac")

arc_diagram_painters.connect("Paul Signac", "Georges Seurat")
arc_diagram_painters.connect("Paul Signac", "Camille Pissarro")
# arc_diagram_painters.connect("Paul Signac", "Claude Monet")

arc_diagram_painters.connect("Camille Pissarro", "Paul Cézanne")
arc_diagram_painters.connect("Camille Pissarro", "Paul Gauguin")
arc_diagram_painters.connect("Camille Pissarro", "Vincent van Gogh")
arc_diagram_painters.connect("Camille Pissarro", "Georges Seurat")
arc_diagram_painters.connect("Camille Pissarro", "Paul Signac")
arc_diagram_painters.connect("Camille Pissarro", "Édouard Manet")
arc_diagram_painters.connect("Camille Pissarro", "Claude Monet")
arc_diagram_painters.connect("Camille Pissarro", "Pierre-Auguste Renoir")
arc_diagram_painters.connect("Camille Pissarro", "Edgar Degas")

arc_diagram_painters.connect("Claude Monet", "Paul Signac")
arc_diagram_painters.connect("Claude Monet", "Pierre-Auguste Renoir")
arc_diagram_painters.connect("Claude Monet", "Édouard Manet")

arc_diagram_painters.connect("Édouard Manet", "Pierre-Auguste Renoir")
arc_diagram_painters.connect("Édouard Manet", "Edgar Degas")

arc_diagram_painters.set_background_color("black")
# arc_diagram_painters.set_color_map("PuOr")
# arc_diagram_painters.set_color_map("Wistia")
arc_diagram_painters.set_color_map("summer")

arc_diagram_painters.save_plot_as("painters.png")

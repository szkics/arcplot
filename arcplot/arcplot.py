import matplotlib.pyplot as plt
from matplotlib import colormaps
from matplotlib.colors import ListedColormap
import numpy as np
from operator import itemgetter


class ArcDiagram:
    def __init__(self, nodes, title):
        self.nodes = nodes
        self.title = title
        self.arc_coordinates = []
        self.colors = plt.cm.viridis(np.linspace(0, 1, len(nodes)))
        self.background_color = "white"
        self.__label_rotation_degree = 0

    def connect(self, start_node, end_node, linewidth=0.1, arc_position="above"):
        start = self.nodes.index(start_node)
        end = self.nodes.index(end_node)

        arc_center = (start + end) / 2
        radius = abs(end - start) / 2

        if arc_position == "below":
            theta = np.linspace(180, 360, 100)
        else:
            theta = np.linspace(0, 180, 100)

        x = arc_center + radius * np.cos(np.radians(theta))
        y = radius * np.sin(np.radians(theta))
        self.arc_coordinates.append((x, y, start, linewidth))

    def save_plot_as(self, file_name, resolution="figure"):
        fig, ax = self.__plot()
        plt.savefig(file_name, dpi=resolution, bbox_inches="tight")

    def set_background_color(self, color):
        self.background_color = color

    def set_color_map(self, color_map_name):
        color_map = colormaps[color_map_name]
        self.colors = color_map(np.linspace(0, 1, len(self.nodes)))

    def set_custom_colors(self, color_list):
        self.colors = ListedColormap(color_list).colors

    def set_label_rotation_degree(self, degree):
        self.__label_rotation_degree = degree

    def show_plot(self):
        fig, ax = self.__plot()
        plt.show()

    def __plot(self):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_facecolor(self.background_color)

        # plot nodes as points
        node_positions = np.arange(len(self.nodes))
        ax.scatter(
            node_positions, np.zeros_like(node_positions), color=self.colors, s=100
        )

        max_value = max(self.arc_coordinates, key=itemgetter(3))[3]
        # plot connections as arcs
        for x, y, index, raw_linewidth in self.arc_coordinates:
            ax.plot(
                x,
                y,
                color=self.colors[index],
                zorder=1,
                linewidth=self._map_to_linewidth(raw_linewidth, max_value),
            )

        plt.xticks(rotation=self.__label_rotation_degree)
        ax.set_xticks(node_positions)
        ax.set_xticklabels(self.nodes)
        ax.set_yticks([])
        ax.set_title(self.title)

        return fig, ax

    def _map_to_linewidth(self, value, max_value):
        if value < 1:
            return 1
        else:
            return (10 * value) / max_value

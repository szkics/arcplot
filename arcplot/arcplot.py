import matplotlib.pyplot as plt
from matplotlib import colormaps
from matplotlib.colors import ListedColormap
import numpy as np
from operator import itemgetter


class ArcDiagram:

    def __init__(self, *args):

        if len(args) != 2:
            self.help()
            raise ValueError("ArcDiagram(node_list, title_string) takes 2 arguments.")

        self.__nodes = args[0]
        self.__title = args[1]
        self.__arc_coordinates = []
        self.__colors = plt.cm.viridis(np.linspace(0, 1, len(self.__nodes)))
        self.__background_color = "white"
        self.__label_rotation_degree = 0
        self.__legend_labels = []

    def connect(self, start_node, end_node, linewidth=0.1, arc_position="above"):
        start = self.__nodes.index(start_node)
        end = self.__nodes.index(end_node)

        arc_center = (start + end) / 2
        radius = abs(end - start) / 2

        if arc_position == "below":
            theta = np.linspace(180, 360, 100)
        else:
            theta = np.linspace(0, 180, 100)

        x = arc_center + radius * np.cos(np.radians(theta))
        y = radius * np.sin(np.radians(theta))
        self.__arc_coordinates.append((x, y, start, linewidth))

    def help(self):
        function_list = """
        ArcDiagram(node_list, title_string)
        .set_background_color(string)
        .set_color_map(string)
        .set_custom_colors(color_list)
        .set_label_rotation_degree(arc_degree)
        .set_legend_labels(list_of_labels)
        .connect(start, end, linewidth=100, arc_position="below")
        .show_plot()
        .save_plot_as(file_name, resolution="100")
        """
        print(function_list)

    def set_background_color(self, color):
        self.__background_color = color

    def set_color_map(self, color_map_name):
        color_map = colormaps[color_map_name]
        self.__colors = color_map(np.linspace(0, 1, len(self.__nodes)))

    def set_custom_colors(self, color_list):
        self.__colors = ListedColormap(color_list).colors

    def set_label_rotation_degree(self, degree):
        self.__label_rotation_degree = degree

    def set_legend_labels(self, legend_labels):
        self.__legend_labels = legend_labels

    def save_plot_as(self, file_name, resolution="figure"):
        fig, ax = self.__plot()
        plt.savefig(file_name, dpi=resolution, bbox_inches="tight")

    def show_plot(self):
        fig, ax = self.__plot()
        plt.show()

    def __label_color_distribution(self, colors, n):
        if n <= 0:
            return []

        step = (len(colors) - 1) / (n - 1)
        indices = [round(i * step) for i in range(n)]
        return [colors[i] for i in indices]

    def __plot(self):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_facecolor(self.__background_color)

        # plot nodes as points
        node_positions = np.arange(len(self.__nodes))
        ax.scatter(
            node_positions, np.zeros_like(node_positions), color=self.__colors, s=100
        )

        max_value = max(self.__arc_coordinates, key=itemgetter(3))[3]
        # plot connections as arcs
        for x, y, index, raw_linewidth in self.__arc_coordinates:
            ax.plot(
                x,
                y,
                color=self.__colors[index],
                zorder=1,
                linewidth=self._map_to_linewidth(raw_linewidth, max_value),
            )

        plt.xticks(rotation=self.__label_rotation_degree)
        ax.set_xticks(node_positions)
        ax.set_xticklabels(self.__nodes)
        ax.set_yticks([])
        ax.set_title(self.__title)

        if self.__legend_labels != []:
            legend_labels = self.__legend_labels
            label_colors = self.__label_color_distribution(
                self.__colors, len(legend_labels)
            )
            ax.legend(
                handles=[
                    plt.Line2D(
                        [0],
                        [0],
                        marker="o",
                        color="w",
                        label=label,
                        markerfacecolor=label_colors[i],
                        markersize=10,
                    )
                    for i, label in enumerate(legend_labels)
                ],
                loc="upper right",
            )

        return fig, ax

    def _map_to_linewidth(self, value, max_value):
        if value < 1:
            return 1
        else:
            return (10 * value) / max_value

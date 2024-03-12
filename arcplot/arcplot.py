import matplotlib.pyplot as plt
from matplotlib import colormaps
from matplotlib.colors import ListedColormap
import numpy as np
import pandas as pd
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


def fast_arc_diagram(
    df: pd.DataFrame,
    start_node: str,
    end_node: str,
    weights=None,
    positions=None,
    invert_positions: bool = False,
    bg_color="white",
    cmap="viridis",
    title="My Diagram",
):
    """
    Wrapper for the ArcDiagram class, which creates diagrams from a pandas dataframe.
    Args:
        df (pd.DataFrame): The dataframe containing the data.
        start_node (str): The name of the column containing the start node.
        end_node (str): The name of the column containing the end node.
        weights (str, optional): The name of the column containing the weights. Defaults to None.
        positions (str, optional): The name of the column containing the positions. Defaults to None.
        invert_positions (bool, optional): Whether to invert the positions. Defaults to False.
        bg_color (str, optional): The background color. Defaults to 'white'.
        cmap (str, optional): The color map. Defaults to 'viridis'.
        title (str, optional): The title of the diagram. Defaults to 'My Diagram'.
    Raises:
        ValueError: If start_node or end_node are not columns in the dataframe.
        ValueError: If start_node and end_node do not have the same length.
        ValueError: If positions is not a column in the dataframe.
        ValueError: If positions does not have 1 or 2 unique values.
        ValueError: If weights is not a column in the dataframe.
    """

    # check if ArcDiagram is installed
    try:
        from arcplot import ArcDiagram
    except:
        raise ImportError(
            "ArcDiagram is not installed. Please install it using pip install arcplot"
        )

    data = df.copy()

    if start_node not in data.columns or end_node not in data.columns:
        raise ValueError("start_node and end_node must be columns in the dataframe")

    if len(data[start_node]) != len(data[end_node]):
        raise ValueError("start_node and end_node must have the same length")

    # get all unique nodes
    nodes = data[start_node].unique().tolist() + data[end_node].unique().tolist()
    nodes = list(set(nodes))

    # initialize the diagram
    arcdiag = ArcDiagram(nodes, title)

    # get positions
    if positions:
        if positions not in data.columns:
            raise ValueError("positions must be a column in the dataframe")
        else:
            n_positions = data[positions].nunique()
            if n_positions not in [1, 2]:
                raise ValueError("positions must have 1 or 2 unique values")
            else:
                if n_positions == 1:
                    posMap = {data[positions].unique()[0]: "above"}
                else:
                    posMap = {
                        data[positions].unique()[0]: "above",
                        data[positions].unique()[1]: "below",
                    }
                data[positions] = data[positions].map(posMap)

                if invert_positions:
                    data[positions] = data[positions].map(
                        {"below": "above", "above": "below"}
                    )
    else:
        data[positions] = "above"

    # get weights
    if not weights:
        data[weights] = 0.1
    else:
        if weights not in data.columns:
            raise ValueError("weights must be a column in the dataframe")

    # connect the nodes
    for connection in data.iterrows():
        arcdiag.connect(
            connection[1][start_node],
            connection[1][end_node],
            linewidth=connection[1][weights],
            arc_position=connection[1][positions],
        )

    # custom colors
    arcdiag.set_background_color(bg_color)
    arcdiag.set_color_map(cmap)

    # plot the diagram
    arcdiag.show_plot()

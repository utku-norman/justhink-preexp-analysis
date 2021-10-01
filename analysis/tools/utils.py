import math

import networkx as nx

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns


def pick_colors(participants=range(1, 10)):
    # palette = sns.color_palette('colorblind')
    palette = sns.color_palette('bright')
    color_list = list(palette)

    colors = {p: color_list[p-1] for p in participants}
    # Swaps for opposite colors for better visuals.
    colors[8] = color_list[9]
    colors[9], colors[1] = colors[1], colors[9]
    colors[3], colors[1] = colors[1], colors[3]
    colors[2], colors[6] = colors[6], colors[2]
    colors[2], colors[1] = colors[1], colors[2]
    colors[3], colors[6] = colors[6], colors[3]
    colors[7], colors[1] = colors[1], colors[7]

    colors[6], colors[1] = colors[1], colors[6]

    return colors


def plot_comparison(
        comparison_df, getter,
        participants=None, fig=None, ax=None, offset=0.01,
        zero_offset=0, xvalues=['1', '2'],  title='', ylabel='',
        ylim=(-0.08, 1.05), ygrid=False, yticks=False,
        save=True, export_file=None, verbose=False):
    """Graph the pre-test versus post-test scores."""
    if participants is None:
        participants = sorted(comparison_df.index)
    if ax is None:
        fig, ax = plt.subplots(1, figsize=(5, 7))

    # Positions.
    list1 = list()
    list2 = list()
    positions = dict()
    for participant in participants:
        row = comparison_df.loc[participant]
        values = getter(row)

        # Compute offset to prevent overlapping lines.
        v1, v2 = round(values[0], 2), round(values[1], 2)
        p0 = values[0] - list1.count(v1) * offset
        p1 = values[1] - list2.count(v2) * offset
        list1.append(v1)
        list2.append(v2)
        if zero_offset is not None:
            if values[0] == 0:
                p0 = p0 + zero_offset
            if values[1] == 0:
                p1 = p1 + zero_offset

        if verbose:
            print(participant, values, p0, p1)
        positions[participant] = (p0, p1)

    # Plot.
    colors = pick_colors(participants)
    for participant in sorted(participants):
        position = positions[participant]
        if math.isnan(position[0]) or math.isnan(position[1]):
            marker, size = 'X', 14
        else:
            marker, size = 'o', 8  # 'D'

        # Plot a line segment for the participant.
        sns.lineplot(
            x=xvalues, y=position, marker=marker, ms=size,
            ls='--', color=colors[participant], label=str(participant),
            legend=False, ax=ax)

    ax.set_ylabel(ylabel, labelpad=0)
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    if ylim:
        ax.set_ylim(ylim[0], ylim[1])

    # Turn on/off grid on the left Axis.
    ax.grid(ygrid)

    ax.set_title(title)

    leg = plt.legend(sorted(participants), loc='upper right', frameon=True, ncol=2)
    # leg = plt.legend(sorted(participants), loc='upper left', frameon=True)
    # # Get the bounding box of the original legend.
    # bb = leg.get_bbox_to_anchor().inverse_transformed(ax.transAxes)
    # # Change to location of the legend.
    # x_offset = 1.05
    # bb.x0 = bb.x0 + x_offset
    # bb.x1 = bb.x1 + x_offset
    # leg.set_bbox_to_anchor(bb, transform=ax.transAxes)

    if export_file is not None and save:
        plt.savefig(export_file, bbox_inches='tight')
        print(export_file)


def draw_network(G, labels=None, ax=None):
    x_values = nx.get_node_attributes(G, 'x')
    y_values = nx.get_node_attributes(G, 'y')

    pos = {u: (x_values[u], y_values[u]) for u in G.nodes()}

    if ax is None:
        fig, ax = plt.subplots()

    if labels is None:
        labels = {u: '{}-{}'.format(u, d['text'].split()[-1])
                  for u, d in G.nodes(data=True)}

    nx.draw(
        G, pos=pos, with_labels=True, labels=labels,
        nodelist=[u for u in G.nodes()], ax=ax)

    labels = nx.get_edge_attributes(G, 'cost')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
    ax.margins(0.1)

    return ax

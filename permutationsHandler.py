import matplotlib.pyplot as plt
import networkx as nx


class ListPermutations:
    def __init__(self, list_data):
        """
        Initializes the ListPermutations class with the given list data.

        Parameters:
            list_data (list): The list of elements to generate permutations for.
        """
        self.list_data = list_data
        self.G = nx.MultiGraph()
        self._new_node = self._node_generator()
        print(f"\nPermutations of  {list_data} .\n")


    def permutation_iterator(self,):
        """
        Returns an iterator that yields all permutations of the list data.
        """
        permutation_generator = self._permutation_generator()
        while True:
            try:
                perm = next(permutation_generator)
                yield perm
            except StopIteration:
                break

    def _permutation_generator(self, ):
        """
        Generates permutations of the list data and constructs a graph representing the permutation tree.
        """
        root_node = next(self._new_node)
        self.G.add_node(root_node, label='root')
        for perm in self._generate_permutation_tree(elements=self.list_data, parent_node=root_node):
            yield perm


    def _generate_permutation_tree(self, elements, parent_node):
        """
        Recursively generates the permutation tree.

        Parameters:
            elements (list): The current list of elements to generate permutations for.
            parent_node (int): The parent node in the graph.
        """
        if len(elements) == 1:
            current_node = next(self._new_node)
            self.G.add_node(current_node, label=elements[0])
            self.G.add_edge(parent_node, current_node)
            return [elements]

        perms = []
        for i in range(len(elements)):
            current = elements[i]
            current_node = next(self._new_node)
            self.G.add_node(current_node, label=current)
            self.G.add_edge(parent_node, current_node)
            remaining = elements[:i] + elements[i + 1:]
            for p in self._generate_permutation_tree(elements=remaining, parent_node=current_node):
                perms.append([current] + p)
        return perms

    def _node_generator(self):
        """
        Generates unique node identifiers for the graph.
        """
        count = 0
        while True:
            yield count
            count += 1

    def tree_display(self,):
        """
        Displays the permutation tree using matplotlib and networkx.
        """
        pos = nx.spring_layout(self.G, seed=2)
        labels = nx.get_node_attributes(self.G, 'label')
        nx.draw_networkx_nodes(self.G, pos, node_size=700, node_color='skyblue')
        nx.draw_networkx_edges(self.G, pos, edgelist=self.G.edges(), width=2, edge_color='gray')
        nx.draw_networkx_labels(self.G, pos, labels, font_size=16)
        plt.show()
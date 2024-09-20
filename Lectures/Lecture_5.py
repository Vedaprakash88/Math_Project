# graphs are networkdiagrams and cannot be represented in python directly - therefore, we need to use graph libraries.
nodes = {'A', 'B', 'C', 'D', 'E', 'F'}
edges = {('A', 'C'), ('C', 'E'), ('C', 'F'), ('F', 'E'), ('E', 'B'), ('E', 'G'), ('B', 'D')}
G = (nodes, edges)
lst1 = []
fnd = False


def is_there_a_way(graph, node1, node2):
    """
    This function returns True if there is a way from one node to another, False otherwise.
    :param graph: a graph (tuple of nodes and edges)
    :param node1: the name of the origin node
    :param node2: the name of the destination node
    :return:
    """
    for i in range(len(graph)):
        for tpl in graph:
            if node1 == tpl[0]:
                if node2 == tpl[1]:
                    lst1.append(tpl[1])
                    return True
                if not node1 in lst1:
                    lst1.append(node1)
                if not tpl[1] in lst1:
                    lst1.append(tpl[1])
                node1 = tpl[1]


if is_there_a_way(edges, 'C', 'D') is True:
    print('True')  # --> True
    print(lst1)
else:
    print('False')

if is_there_a_way(edges, 'B', 'G') is True:
    print('True')  # --> False
    print(lst1)
else:
    print('False')

######################################################################################
edges = {
('a','c'),
('c','b'),
('c','g'),
('c','i'),
('f','i'),
('f','c'),
('g','i'),
('g','h'),
('i','j'),
('d','g'),
('d','e'),
('h','d')}
#################################################################################################
"Professor's answer"

nodes = {'A', 'B', 'C', 'D', 'E', 'F'}
edges = {('A','C'), ('C','E'), ('C','F'), ('F','E'), ('E','B'), ('E', 'G'),('B','D')}
G = (nodes, edges)

def is_there_a_way(graph, node1, node2):
    '''
    This function returns True if there is a way from one node to another, False otherwise.
    :param node1:
    :param node2:
    :return:
    '''
    _, edges = graph

    to_explore = []
    explored = []

    current_node = node1

    while current_node != node2:
        for src, dst in edges:
            if src == current_node and not (dst in explored or dst in to_explore):
                to_explore.append(dst)

        if not to_explore:
            return False

        explored.append(current_node)
        current_node = to_explore.pop()
    else:
        return True

if __name__ == '__main__':
    print(is_there_a_way(G, 'C', 'D'))
    print(is_there_a_way(G, 'B', 'G'))

#######################################################################################
#clean code - leetcode
#separation of concerns: Splitting your code
#######################################################################################
# from graph.start import is_there_a_way
# import os
#
# my_path = 'abc' + '/' + 'cde'
#
# my_path = os.path.join('abc', 'cde')
#
#
# result = is_there_a_way(({},{('a','b')}), 'a', 'b')
#
# print(result)
#########################################################################################
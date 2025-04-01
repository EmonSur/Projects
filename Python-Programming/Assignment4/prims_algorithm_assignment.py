# import the following libraries
import random
import heapq
import time

class Vertex:
    """ A Vertex in a graph. """

    def __init__(self, element):
        """ Create a vertex, with data element. """
        self._element = element
    
    def element(self):
        """ Return the data for the vertex. """
        return self._element

class Edge:
    """ An edge in a graph. """

    def __init__(self, v, w, element):
        """ Create an edge between vertices v and w, with label element."""
        self._vertices = (v,w)
        self._element = element
    
    def vertices(self):
        """ Return an ordered pair of the vertices of this edge."""
        return self._vertices
        
    def element(self):
        """ Return the data element for this edge. """
        return self._element
    
    def start(self):
        """ Return the first vertex in the ordered pair. """
        return self._vertices[0]


class Graph:
    """ Represent a simple graph. """

    def __init__(self):
        """ Create an initial empty graph. """
        self._structure = dict()   

    def add_vertex(self, element):
        """ Add and return a new vertex with data element. """
        
        v = Vertex(element)
        self._structure[v] = dict() # create an empty dict, ready for edges
        return v

    def add_edge(self, v, w, element):
        """ Add and return an edge, with element, between two vertices v and w. """
        e = Edge(v, w, element)
        self._structure[v][w] = e
        self._structure[w][v] = e
        return e

    def vertices(self):
        """ Return a list of all vertices in the graph. """
        return self._structure.keys()

    def edges(self):
        """ Return a list of all edges in the graph. """
        edgeList = []
        for v in self._structure:
            for w in self._structure[v]:
                #to avoid duplicates, only return if v is the first vertex
                if self._structure[v][w].start() == v:
                    edgeList.append(self._structure[v][w])
        return edgeList
    
    def get_vertex_by_element(self, element):
        """ Return the vertex with the given element, if it exists. """
        for vertex in self.vertices():
            if vertex.element() == element:
                return vertex
        return None
    
def create_random_connected_graph(n, m_max, edge_ratio):
    """ Create a random connected graph with n vertices and edges based on a given ratio. """
    graph = Graph()
    for i in range(n):
        graph.add_vertex(i)
    vertices = list(graph.vertices())

    # Connect each vertex to at least one other to ensure the graph is initially connected
    for i in range(1, n):
        w = random.randint(1, 20)
        graph.add_edge(vertices[i - 1], vertices[i], w)

    # Calculate the total number of edges to be added based on the edge ratio
    total_edges = int(m_max * edge_ratio)
    added_edges = n - 1  # Count of edges added to ensure connectivity

    while added_edges < total_edges:
        v1, v2 = random.sample(vertices, 2)
        if v1 != v2:
            # Directly check in the adjacency structure if the edge does not exist
            if v2 not in graph._structure[v1] and v1 not in graph._structure[v2]:
                w = random.randint(1, 20)
                graph.add_edge(v1, v2, w)
                added_edges += 1

    return graph




def prims_algorithm(graph, start_vertex, use_heap=True):
    """
    Implement Prim's algorithm to find the minimum spanning tree of a graph.
    
    Args:
        use_heap -- If True, use a heap otherwise use an unsorted list.
    """

    visited = {start_vertex}
    edges = [] 
    mst = [] 

    def add_edges(vertex):
        for adj_vertex, edge in graph._structure[vertex].items():
            if adj_vertex not in visited:
                edge_detail = (edge.element(), vertex.element(), adj_vertex.element(), adj_vertex)
                if use_heap:
                    heapq.heappush(edges, edge_detail)
                else:
                    edges.append(edge_detail)

    add_edges(start_vertex)

    while edges and len(visited) < len(graph.vertices()):
        if use_heap:
            weight, u_elem, v_elem, to_vertex = heapq.heappop(edges)
        else:
            edges.sort(key=lambda x: x[0])  # Sort by weight if using an unsorted list
            weight, u_elem, v_elem, to_vertex = edges.pop(0)

        if to_vertex not in visited:
            visited.add(to_vertex)
            u_vertex = graph.get_vertex_by_element(u_elem)
            mst.append((u_vertex, to_vertex, weight))
            add_edges(to_vertex)

    return mst

def evaluate_prims_runtime(vertices_counts, edge_ratios, use_heap=True):
    results = []
    for n in vertices_counts:
        m_max = n * (n - 1) // 2
        for ratio in edge_ratios:
            graph = create_random_connected_graph(n, m_max, ratio)
            start_vertex = list(graph.vertices())[0]
            
            start_time = time.perf_counter()
            mst = prims_algorithm(graph, start_vertex, use_heap)
            end_time = time.perf_counter()
            runtime = end_time - start_time
            mst_edges_count = len(mst)

            results.append((n, (m_max * ratio) // 1, runtime, mst_edges_count))
    
    return results 

def print_results(results_heap, results_unsorted_list):
    """ Print the results in a table format for easy comparison in a pleasing manner. """

    print(f"{'Vertices':>8} | {'Total Edges':>11} | {'Edge Ratio':>10} | {'Heap Time (s)':>13} | {'Unsorted List Time (s)':>22} | {'MST Edges':>10}")
    print('-' * 90)

    for (heap_result, unsorted_list_result) in zip(results_heap, results_unsorted_list):
        vertices, edges, heap_time, mst_edges = heap_result
        _, _, unsorted_list_time, _ = unsorted_list_result
        edge_ratio = edges / (vertices * (vertices - 1) / 2)  # Calculate the edge ratio
        print(f"{vertices:>8} | {edges:>11} | {edge_ratio:>10.2f} | {heap_time:>13.6f} | {unsorted_list_time:>22.6f} | {mst_edges:>10}")

if __name__ == "__main__":
    # Test larger graphs and broader density ranges
    vertices = [50, 100, 200, 400, 800]  # Test with larger graph sizes to see performance impact
    edge_ratios = [0.05, 0.1, 0.25, 0.5, 0.75, 1.0]  # From very sparse to fully connected

    # Evaluate using both heap-based and unsorted list-based priority queues
    results_heap = evaluate_prims_runtime(vertices, edge_ratios, True)
    results_unsorted_list = evaluate_prims_runtime(vertices, edge_ratios, False)

    print("Heap-based Priority Queue Results:")
    print_results(results_heap, True)

    print("\nUnsorted List Priority Queue Results:")
    print_results(results_unsorted_list, False)


               


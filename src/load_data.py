import json
from src.graph import Graph

def load_city_map(graph, file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        for node in data['nodes']:
            graph.add_node(node)
        for edge in data['edges']:
            graph.add_edge(edge['from'], edge['to'], edge['distance'])

def load_traffic_data(graph, file_path):
    with open(file_path, 'r') as f:
        traffic_data = json.load(f)
        for data in traffic_data:
            from_node = data['from']
            to_node = data['to']
            travel_time = data['travel_time']
            graph.distances[(from_node, to_node)] = travel_time
            graph.distances[(to_node, from_node)] = travel_time

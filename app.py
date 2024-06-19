from flask import Flask, request, jsonify
from src.graph import Graph
from src.dijkstra import shortest_path
from src.load_data import load_city_map, load_traffic_data

app = Flask(__name__)

# Initialize the graph
graph = Graph()

# Load data from JSON files
load_city_map(graph, 'data/city_map.json')

@app.route('/shortest-path', methods=['GET'])
def get_shortest_path():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    
    # Load and update traffic data
    load_traffic_data(graph, 'data/traffic_data.json')
    
    distance, path = shortest_path(graph, origin, destination)
    return jsonify({'distance': distance, 'path': path})

if __name__ == '__main__':
    app.run(debug=True)

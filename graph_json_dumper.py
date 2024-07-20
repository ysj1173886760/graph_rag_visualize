import pandas as pd
import networkx as nx
import json

def load_graph(graphml: str | nx.Graph) -> nx.Graph:
     """Load a graph from a graphml file or a networkx graph."""
     return nx.parse_graphml(graphml) if isinstance(graphml, str) else graphml

# 指定Parquet文件的路径
base_file_path = './ragtest/output/20240720-155321/artifacts/'
file_name = "create_base_extracted_entities.parquet"

# 使用pandas读取Parquet文件
df = pd.read_parquet(base_file_path + file_name)

graphml = df["entity_graph"].iloc[0]

graph = load_graph(graphml)

nodes = [{'id': n, 'key': n, 'label': graph.nodes[n]['type'], **{k: graph.nodes[n][k] for k in graph.nodes[n] if k != 'type'}} for n in graph.nodes]
edges = [{'source': u, 'target': v, **data} for u, v, data in graph.edges(data=True)]

graph_data = {
    'nodes': nodes,
    'edges': edges
}
json_file_path = 'graph_data.json'
with open(json_file_path, 'w') as json_file:
    json.dump(graph_data, json_file, indent=4)
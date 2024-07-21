import pandas as pd
import networkx as nx
import csv

def load_graph(graphml: str | nx.Graph) -> nx.Graph:
     """Load a graph from a graphml file or a networkx graph."""
     return nx.parse_graphml(graphml) if isinstance(graphml, str) else graphml

# 指定Parquet文件的路径
base_file_path = './ragtest/output/20240720-155321/artifacts/'
file_name = "create_summarized_entities.parquet"

# 使用pandas读取Parquet文件
df = pd.read_parquet(base_file_path + file_name)

graphml = df["entity_graph"].iloc[0]

graph = load_graph(graphml)

# nodes = [{'id': n, 'key': n, 'label': graph.nodes[n]['type'], **{k: graph.nodes[n][k] for k in graph.nodes[n] if k != 'type'}} for n in graph.nodes]
# edges = [{'source': u, 'target': v, **data} for u, v, data in graph.edges(data=True)]

# 导出节点到CSV文件
with open('nodes.csv', 'w', newline='') as csvfile:
    fieldnames = ['id'] + list(next(iter(graph.nodes(data=True)))[1].keys())  # 获取节点属性作为列名
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for node, attr in graph.nodes(data=True):
        writer.writerow({'id': node, **attr})

# 导出边到CSV文件
with open('edges.csv', 'w', newline='') as csvfile:
    fieldnames = ['source', 'target'] + list(next(iter(graph.edges(data=True)))[2].keys())  # 获取边属性作为列名
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for source, target, attr in graph.edges(data=True):
        writer.writerow({'source': source, 'target': target, **attr})
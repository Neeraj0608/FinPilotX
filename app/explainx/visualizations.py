import plotly.graph_objects as go
import plotly.express as px
import networkx as nx
import matplotlib.pyplot as plt

def create_radar_chart(categories, values, title):
    """Create a radar chart for multi-factor risk comparison."""
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Risk Profile',
        marker=dict(color='#00FFA3')
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1]),
            bgcolor='rgba(30, 33, 48, 1)',
        ),
        showlegend=False,
        title=title,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )
    return fig

def create_network_graph():
    """Create a network graph showing feature correlations (Mock for demo)."""
    G = nx.Graph()
    features = ['Income', 'Age', 'Debt', 'Credit', 'Jobs', 'Assets']
    G.add_nodes_from(features)
    
    # Add some random edges
    edges = [('Income', 'Debt'), ('Income', 'Assets'), ('Debt', 'Credit'), ('Age', 'Jobs')]
    G.add_edges_from(edges)
    
    pos = nx.spring_layout(G)
    
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=features,
        marker=dict(
            showscale=False,
            color='#00FFA3',
            size=20,
            line_width=2))

    fig = go.Figure(data=[edge_trace, node_trace],
                 layout=go.Layout(
                    title='Feature Correlation Network',
                    showlegend=False,
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    font=dict(color='white')
                 ))
    return fig

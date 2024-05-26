/*
Weighted Unidirected Graph
Input Format:
[num_of_vertices] [num_of_edges]
[Node 1] [Node 2] [Weight]   <-  will be multiple lines (number of lines = num_of_edges) 
*/

#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9+7;
map<pair<char, char>, int> Edge;
map<char, vector<pair<char, int>>> Vertex;

void make_graph(int n){
    Vertex.clear();
    Edge.clear();

    char u, v; int w;
    for(int i = 0; i < n; i++){
        cin >> u >> v >> w;
        Vertex[u].push_back({v, w});
        Vertex[v].push_back({u, w});
        Edge[{u, v}] = w;
        Edge[{v, u}] = w;
    }
}

int main() {
    int num_of_vertices, num_of_edges;
    cin >> num_of_vertices >> num_of_edges;

    make_graph(num_of_edges);

    return 0;
}

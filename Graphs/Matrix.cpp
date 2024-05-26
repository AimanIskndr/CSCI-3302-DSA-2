/*
Weighted Unidirected Graph Matrix Representation (Notes: This only apply if the node is represented as a number)
Input Format:
[num_of_vertices] [num_of_edges]
[Node 1] [Node 2] [Weight]   <-  will be multiple lines (number of lines = num_of_edges) 
*/

#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9 + 7;
vector<vector<int>> graph;

void make_graph(int num_of_vertices, int num_of_edges) {
    graph.assign(num_of_vertices, vector<int>(num_of_vertices, INF)); // set default value to INF
    
    int u, v, w;
    for (int i = 0; i < num_of_edges; i++) {
        cin >> u >> v >> w;
        graph[u][v] = w;
        graph[v][u] = w;
    }
}

int main(){
    int num_of_vertices, num_of_edges;
    cin >> num_of_vertices >> num_of_edges;

    make_graph(num_of_vertices, num_of_edges);

    return 0;
}

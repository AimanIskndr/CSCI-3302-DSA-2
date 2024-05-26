/*
Weighted Unidirected Graph as a Class
Input Format:
[num_of_vertices] [num_of_edges]
[Node 1] [Node 2] [Weight]   <-  will be multiple lines (number of lines = num_of_edges) 
*/

#include <bits/stdc++.h>
using namespace std;

class WeightedUndirectedGraph{
private:
    map<pair<char, char>, int> edge;
    map<char, vector<pair<char, int>>> vertex;

public:
    void make_graph(int num_of_edges){
        vertex.clear();
        edge.clear();

        char u, v;
        int w;
        for(int i = 0; i < num_of_edges; i++){
            cin >> u >> v >> w;
            vertex[u].push_back({v, w});
            vertex[v].push_back({u, w});
            edge[{u, v}] = w;
            edge[{v, u}] = w;
        }
    }
};

int main(){
    int num_of_vertices, num_of_edges;
    cin >> num_of_vertices >> num_of_edges;

    WeightedUndirectedGraph graph;
    graph.make_graph(num_of_edges);

    return 0;
}

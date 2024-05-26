/*
Dijkstra Algorithm with Adjacency List inputs (Weighted Unidirected Graph)
Input Format:
[num_of_vertices] [num_of_edges]
[Node 1] [Node 2] [Weight]   <-  will be multiple lines (number of lines = num_of_edges) 
*/

#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9+7;
map<pair<char, char>, int> Edge;
map<char, vector<pair<char, int>>> Vertex;
map<char, int> dist;
map<char, char> previous;

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

void dijkstra(char start){
    for(auto &v : Vertex){
        dist[v.first] = INF;
    }
    dist[start] = 0;

    priority_queue<pair<int, char>, vector<pair<int, char>>, greater<pair<int, char>>> pq;
    pq.push({0, start});

    while(!pq.empty()){
        char cur = pq.top().second;
        int curDist = pq.top().first;
        pq.pop();

        if(curDist > dist[cur])
            continue;

        for(auto neighbor : Vertex[cur]){
            char next = neighbor.first;
            int weight = neighbor.second;
            if(dist[cur] + weight < dist[next]){
                dist[next] = dist[cur] + weight;
                pq.push({dist[next], next});
                previous[next] = cur;
            }
        }
    }
}

int main() {
    int num_of_vertices, num_of_edges;
    cin >> num_of_vertices >> num_of_edges;

    make_graph(num_of_edges);

    char start = 'a';
    dijkstra(start);

    cout << "Vertex\tPrev\tShortest Distance\n";
    for(auto [n, d] : dist)
        cout << n <<"\t"<<previous[n]<<"\t"<<d<<"\n";

    return 0;
}

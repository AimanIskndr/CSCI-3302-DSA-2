//Simple DSU without path compression
#include <bits/stdc++.h>
using namespace std;

class DisjointSet{
private:
    vector<int> parent;

public:
    DisjointSet(int size){
        parent.resize(size);
    }

    void make_set(int v){
        parent[v] = v;
    }

    int find_set(int v){
        if(v == parent[v])
            return v;
        return find_set(parent[v]);
    }

    void union_sets(int a, int b){
        a = find_set(a);
        b = find_set(b);
        if(a != b)
            parent[b] = a;
    }
};

#include <bits/stdc++.h>

using namespace std;

void dfs(int v, vector<vector<int>> &g, vector<bool> &vstd)
{
  vstd[v] = true;
  cout << (v + 1) << endl;

  for (auto u : g[v])
  {
    if (!vstd[u])
    {
      dfs(u, g, vstd);
    }
  }
}

int main(void)
{
  int n; // number of nodes in graph
  int e; // number of edges in graph
  cin >> n >> e;

  vector<vector<int>> g(n);
  vector<bool> vstd(n, false);

  for (int i = 0; i < e; i++)
  {
    int u, v;
    cin >> u >> v;
    --u;
    --v;
    g[u].push_back(v);
    g[v].push_back(u);
  }

  for (int i = 0; i < n; i++)
  {
    if (!vstd[i])
      dfs(i, g, vstd);
  }

  return 0;
}

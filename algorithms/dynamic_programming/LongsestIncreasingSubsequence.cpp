#include <bits/stdc++.h>

using namespace std;

int ceilFind(vector<int> &ar, int l, int r, int k)
{
  while (r - l > 1)
  {
    int m = l + (r - l) / 2;
    if (ar[m] >= k)
    {
      r = m;
    }
    else
      l = m;
  }
  return r;
}

int findLIS(vector<int> &ar)
{
  vector<int> tar(ar.size()), ans(ar.size(), 0);
  int len = 1;
  tar[0] = ar[0];

  for (int i = 1; i < ar.size(); i++)
  {
    if (ar[i] < tar[0])
      tar[0] = ar[i];
    else if (tar[len - 1] < ar[i])
      tar[len++] = ar[i];
    else
      tar[ceilFind(tar, -1, len - 1, ar[i])] = ar[i];
  }
  return len;
}

int main(void)
{
  int n;
  cin >> n;
  if (n == 0)
  {
    cout << 0 << endl;
    return 0;
  }
  vector<int> ar(n);
  for (auto &it : ar)
    cin >> it;

  cout << findLIS(ar) << endl;
}

#include <bits/stdc++.h>

using namespace std;

int main(void)
{
  int n;
  cin >> n;
  vector<int> prices(n);

  for (auto &it : prices)
    cin >> it;

  vector<int> ans(n + 1);

  for (int i = 1; i <= n; i++)
  {
    ans[i] = prices[i - 1];
    for (int j = 0; j < i / 2; j++)
    {
      ans[i] = max(ans[i], ans[j] + ans[i - j]);
    }
  }
  //for (int i = 0; i <)
  cout << ans[n] << endl;
}
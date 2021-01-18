#include <bits/stdc++.h>

using namespace std;

int findMaxProfit(int max_wt, vector<int> &wts, vector<int> &val, int &n)
{
  vector<vector<int>> dp(n + 1, vector<int>(max_wt + 1, 0));

  for (int i = 1; i <= n; i++)
  {
    for (int j = 1; j <= max_wt; j++)
    {
      if (j - wts[i - 1] < 0)
        dp[i][j] = dp[i - 1][j];
      else
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wts[i - 1]] + val[i - 1]);
    }
  }

  return dp[n][max_wt];
}

int main(void)
{
  int max_wt, n;
  cin >> max_wt >> n;

  vector<int> wts(n), val(n);

  for (int i = 0; i < n; i++)
  {
    cin >> wts[i] >> val[i];
  }

  cout << findMaxProfit(max_wt, wts, val, n) << endl;

  return 0;
}
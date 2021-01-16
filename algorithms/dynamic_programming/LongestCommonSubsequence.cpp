#include <bits/stdc++.h>

using namespace std;

string findLCS(string &s1, string &s2)
{
  int n = s1.size() + 1, m = s2.size() + 1;
  vector<vector<int>> dp(n, vector<int>(m + 1, 0));

  for (int i = 1; i < n; i++)
  {
    for (int j = 1; j < m; j++)
    {
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
      if (s1[i - 1] == s2[j - 1])
      {
        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1);
      }
    }
  }

  string ans;

  int i = n - 1, j = m - 1;

  while (i > 0 && j > 0)
  {
    if (dp[i][j] == dp[i - 1][j])
    {
      i = i - 1;
    }
    else if (dp[i][j] == dp[i][j - 1])
    {
      j = j - 1;
    }
    else
    {
      ans.push_back(s1[i - 1]);
      --i;
      --j;
    }
  }
  reverse(ans.begin(), ans.end());
  return ans;
}

int main(void)
{
  string s1, s2;
  cin >> s1 >> s2;
  cout << findLCS(s1, s2) << endl;
}
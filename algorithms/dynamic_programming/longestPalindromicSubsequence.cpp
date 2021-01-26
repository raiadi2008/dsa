#include <bits/stdc++.h>

using namespace std;

// longest palindromic subsequence
string findLPS(string &s)
{
  if (s.size() < 2)
    return s;
  vector<vector<int>> dp(s.size(), vector<int>(s.size(), 0));

  for (int i = 0; i < s.size(); i++)
    dp[i][i] = 1;

  for (int i = 1; i < s.size(); i++)
  {
    for (int j = 0; j + i < s.size(); j++)
    {
      if (s[i + j] == s[j])
      {
        dp[j][j + i] = dp[j + 1][j + i - 1] + 2;
      }
      else
      {
        dp[j][j + i] = max(dp[j + 1][j + i], dp[j][j + i - 1]);
      }
    }
  }
  //cout << "run 1" << endl;

  string ans = string(dp[0][s.size() - 1], ' ');

  //cout << "size of palindrome = " << dp[0][s.size() - 1] << endl;

  int i = 0, j = s.size() - 1, x = 0, y = dp[0][s.size() - 1] - 1;

  while (x <= y)
  {
    if (dp[i][j] == dp[i][j - 1])
    {
      --j;
    }
    else if (dp[i][j] == dp[i + 1][j])
    {
      i++;
    }
    else
    {
      ans[x] = ans[y] = s[i];
      x++;
      y--;
      i++;
      j--;
    }
  }
  return ans;
}

int main(void)
{
  string s;
  cin >> s;

  cout << findLPS(s) << endl;
  return 0;
}

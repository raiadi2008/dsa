#include <bits/stdc++.h>

using namespace std;

vector<int> computeLPS(string &str)
{
  vector<int> lps(str.size(), 0);

  int i = 0, len = 1;
  lps[0] = -1;
  while (len < str.size())
  {
    if (str[i] == str[len])
    {
      lps[len] = i;
      ++i;
    }
    else
    {
      i = 0;
    }
    ++len;
  }

  // cout << "LPS = ";
  // for (int i : lps)
  //   cout << i << " ";
  // cout << endl;

  return lps;
}

vector<int> allMatch(string &pattern, string &txt)
{
  vector<int> lps = computeLPS(pattern);
  vector<int> res;
  //cout << "__debug" << endl;
  for (int i = 0, j = 0; i < txt.size();)
  {
    if (pattern[j] == txt[i])
    {
      if (j == pattern.size() - 1)
      {
        res.push_back(i - j);
        j = lps[j] + 1;
      }
      else
      {
        j++;
      }
      i++;
    }
    else
    {
      while (j != -1)
      {
        j = lps[j];
        if (pattern[j + 1] == txt[i])
        {
          break;
        }
        //cout << "j = " << j << endl;
      }

      j = j + 1;

      if (j == 0 && txt[i] != pattern[j])
      {
        i++;
      }
    }
  }
  return res;
}

int main(void)
{
  string str, pattern;
  cout << "Enter the text or the string : ";
  cin >> str;
  cout << "Enter the pattern to be matched:  ";
  cin >> pattern;

  vector<int> ans = allMatch(pattern, str);
  cout << "All match found: " << ans.size() << endl;
  if (ans.size() > 0)
  {
    for (int i : ans)
      cout << i << " ";
    cout << endl;
  }

  return 0;
}
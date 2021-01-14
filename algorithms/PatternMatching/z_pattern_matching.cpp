#include <bits/stdc++.h>

using namespace std;

// 0  1  2  3  4  5  6
// a  a  b  a  a  b  a
vector<int> calculateZArray(string &str)
{
  vector<int> zArr = vector<int>(str.size());

  int left = 0, right = 0;
  for (int i = 1; i < str.size(); i++)
  {
    if (i > right)
    {
      left = right = i;
      while (right < str.size() && str[right] == str[right - left])
        ++right;

      zArr[i] = right - left;
      --right;
    }
    else
    {
      int k = i - left;

      if (zArr[k] + i <= right)
      {
        zArr[i] = zArr[k];
      }
      else
      {
        left = i;
        while (right < str.size() && str[right] == str[right - left])
          right++;
        zArr[i] = right - left;
        --right;
      }
    }
  }
  return zArr;
}

vector<int> findAllMatch(string &T, string &p)
{
  string pandT = p + "$" + T;
  vector<int> zArr = calculateZArray(pandT);

  vector<int> ans;

  for (int i = 1; i < zArr.size(); i++)
  {
    if (zArr[i] == p.size())
    {
      ans.push_back(i - p.size() - 1);
    }
  }

  return ans;
}

int main(void)
{
  string T, p;
  cout << "Enter the text : ";
  cin >> T;
  cout << "Enter the pattern : ";
  cin >> p;

  vector<int> ans = findAllMatch(T, p);

  if (ans.size() == 0)
    cout << "no match found" << endl;
  else
  {
    cout << "total match : " << ans.size() << endl;
    for (auto i : ans)
      cout << i << " ";
  }
  cout << endl;

  return 0;
}

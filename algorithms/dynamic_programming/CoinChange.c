#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int change, cnt_coins;
  scanf("%d%d", &change, &cnt_coins);
  int coins[cnt_coins];

  for (int i = 0; i < cnt_coins; i++)
    scanf("%d", &coins[i]);

  int dp[cnt_coins + 1][change + 1];

  for (int i = 0; i <= cnt_coins; i++)
  {
    for (int j = 0; j <= change; j++)
    {
      if (j == 0)
      {
        dp[i][j] = 1;
      }
      else if (i == 0)
      {
        dp[i][j] = 0;
      }
      else
      {
        if (j - coins[i - 1] >= 0)
        {
          dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]];
        }
        else
        {
          dp[i][j] = dp[i - 1][j];
        }
      }
    }
  }

  printf("%d\n", dp[cnt_coins][change]);
  return 0;
}
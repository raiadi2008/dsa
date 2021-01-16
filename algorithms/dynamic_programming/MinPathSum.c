#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int n, m;
  scanf("%d%d", &n, &m);

  int ar[n][m], tc[n][m];

  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      scanf("%d", &ar[i][j]);
    }
  }

  tc[0][0] = ar[0][0];
  for (int i = 1; i < n; i++)
  {
    tc[i][0] = tc[i - 1][0] + ar[i][0];
  }

  for (int i = 1; i < m; i++)
  {
    tc[0][i] = tc[0][i - 1] + ar[0][i];
  }

  for (int i = 1; i < n; i++)
  {
    for (int j = 1; j < n; j++)
    {
      tc[i][j] = tc[i - 1][j] < tc[i][j - 1] ? tc[i - 1][j] + ar[i][j] : tc[i][j - 1] + ar[i][j];
    }
  }

  printf("%d", tc[n - 1][m - 1]);

  return 0;
}

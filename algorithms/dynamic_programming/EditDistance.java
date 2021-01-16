import java.util.Scanner;

class EditDistance {

  static int findMinEdits(String A, String B) {
    int[][] dp = new int[A.length() + 1][B.length() + 1];

    for (int i = 0; i <= A.length(); i++) {
      for (int j = 0; j <= B.length(); j++) {
        if (i == 0) {
          dp[i][j] = j;
        } else if (j == 0) {
          dp[i][j] = i;
        } else if (A.charAt(i - 1) == B.charAt(j - 1)) {
          dp[i][j] = dp[i - 1][j - 1];
        } else {
          dp[i][j] = 1 + Math.min(dp[i][j - 1], Math.min(dp[i - 1][j], dp[i - 1][j - 1]));
        }
      }
    }

    return dp[A.length()][B.length()];
  }

  public static void main(String[] args) {
    String string1, string2;
    Scanner scan = new Scanner(System.in);

    string1 = scan.nextLine();
    string2 = scan.nextLine();

    scan.close();

    System.out.println(findMinEdits(string1, string2));
  }
}
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int t = 0; t < T; t++) {
            int n = sc.nextInt();
            int arr[] = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            int ans = 1;
            for (int i = 0; i < n; i++) {
                int max = arr[i], min = arr[i];
                int dup = 0;
                Set hs = new HashSet<>();
                for (int j = i; j < n; j++) {
                    if (!hs.add(arr[j])) {
                        dup++;
                    }

                    max = Math.max(max, arr[j]);
                    min = Math.min(min, arr[j]);
                    if (max - min+1==hs.size()) {
                        ans = Math.max(ans, j-i+1);
                    }
                }
            }
            System.out.println(ans);
        }
    }
}

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long m = (long) 1e9 + 7;
        int t = sc.nextInt();
        while (t-- > 0) {

            long a = sc.nextInt();
            long n = sc.nextInt();
            long ans = 1;

            while (n > 0) {
                if ((n & 1) == 1) {
                    ans = (ans * a) % m;
                }
                a = (a * a) % m;
                n >>= 1;
            }
            System.out.println(ans % m);

        }

    }
}

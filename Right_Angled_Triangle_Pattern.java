import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        for(int k=1;k<=t;k++){
            System.out.println("Case #"+k+":");
            int n=sc.nextInt();
            for(int i=1;i<=n;i++){
                for(int j=0;j<n-i;j++){
                    System.out.print(" ");
                }
                for(int j=0;j<i;j++){
                    System.out.print("*");
                }
                System.out.println();
            }
        }
    }
}
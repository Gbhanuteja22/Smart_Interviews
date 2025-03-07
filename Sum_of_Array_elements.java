import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        long t=sc.nextLong();
        while(t-->0){
            long sum=0;
            long n=sc.nextLong();
            if(n>=1){
                for(int i=0;i<n;i++){
                    sum+=sc.nextLong();
                }
            }
            System.out.println(sum);
        }
    }
}
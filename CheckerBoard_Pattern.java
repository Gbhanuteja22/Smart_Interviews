import java.io.*;
import java.util.*;

public class Main {
    public static void white(){
        System.out.print("--");
    }
    public static void black(){
        System.out.print("**");
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        for(int k=1;k<=t;k++){
            System.out.println("Case #"+k+":");
            int n=sc.nextInt();
            for(int i=0;i<n;i++){
                for(int p=0;p<2;p++){
                for(int j=0;j<n;j++){
                    if((i+j)%2==0){
                        black();
                    }else{
                        white();
                    }
                }
                System.out.println();
                }
            }
        }
    }
}
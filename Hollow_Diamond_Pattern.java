import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        for(int k=1;k<=t;k++){
            System.out.println("Case #"+k+":");
            int n=sc.nextInt();
            for(int i=0;i<(n/2)+1;i++){
                for(int j=0;j<(n/2)-i;j++){
                    System.out.print(" ");
                }
                for(int j=0;j<2*i+1;j++){
                    if(j == 0 || j == 2*i){
                        System.out.print("*");
                    }else{
                        System.out.print(" ");
                    }
                }
                System.out.println();
            }
            for(int i=(n/2)-1;i>=0;i--){
                for(int j=0;j<(n/2)-i;j++){
                    System.out.print(" ");
                }
                for(int j=0;j<2*i+1;j++){
                    if(j==0 || j==2*i){
                        System.out.print("*");
                    }else{
                        System.out.print(" ");
                    }
                }
                System.out.println();
            }
        }
    }
}
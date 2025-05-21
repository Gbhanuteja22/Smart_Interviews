import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            String str=sc.next();
            Map<Character,Integer> count=new HashMap<>();
            for(char ch:str.toCharArray()){
                count.put(ch,count.getOrDefault(ch,0)+1);
            }
            int nimsum=0;
            for(int i:count.values()){
                nimsum^=i;
            }
            if(nimsum==0){
                System.out.println("Banta");
            }else{
                System.out.println("Santa");
            }
        }
    }
}

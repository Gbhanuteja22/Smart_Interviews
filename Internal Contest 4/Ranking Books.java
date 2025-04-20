import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt(); 
            Set<Long> myset=new HashSet<>();
            for(int i=0;i<n;i++){
                myset.add(sc.nextLong());
            }
            List<Long> books=new ArrayList<>(myset);
            int m=sc.nextInt();
            List<Long> pages=new ArrayList<>();
            Collections.sort(books,Collections.reverseOrder());
            for(int i=0;i<m;i++){
                long x=sc.nextLong();
                int low=0;
                int high=books.size();
                while(low<high){
                    int mid=low+(high-low)/2;
                    if(books.get(mid)>x){
                        low=mid+1;
                    }else{
                        high=mid;
                    }
                }
                System.out.print((low+1)+" ");
            }
            System.out.println();
        }
    }
}

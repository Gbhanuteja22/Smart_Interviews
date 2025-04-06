import java.io.*;
import java.util.*;

public class Main {
    public static int find1(TreeSet<Long> ones,long idx){ 
        if (ones.isEmpty()){
            return -1;
        }
        Long left=ones.floor(idx);
        Long right=ones.ceiling(idx);
        int leftdist=Integer.MAX_VALUE;
        int rightdist=Integer.MAX_VALUE;
        if(left!=null){
            leftdist=(int)(idx-left);
        }
        if(right!=null){
            rightdist=(int)(right-idx);
        }
        int mindist=Math.min(leftdist,rightdist);
        return mindist;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            long n=sc.nextLong();
            int q=sc.nextInt();
            TreeSet<Long> ones=new TreeSet<>();
            while(q-->0){
                int ops=sc.nextInt();
                long idx=sc.nextLong();
                if(ops==1){
                    if(ones.contains(idx)){
                        ones.remove(idx);
                    }else{
                        ones.add(idx);
                    }
                }else{
                    int ans=find1(ones,idx);
                    System.out.println(ans);
                }
            }
        }
    }
}

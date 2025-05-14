import java.io.*;
import java.util.*;

public class Main {
    public static class Node{
        int data;
        Node left,right;
        Node(int data){
            this.data=data;
        }
    }
    public static Node insert(Node root,int val){
        if(root==null){ 
            return new Node(val);
        }
        if(val<root.data) root.left=insert(root.left,val);
        else root.right=insert(root.right,val);
        return root;
    }
    public static List<Integer> rightview(Node root){
        List<Integer> res=new ArrayList<>();
        recurright(root,0,res);
        return res;
    }
    public static void recurright(Node root,int level,List<Integer> res){
        if(root==null) return;
        if(res.size()==level) res.add(root.data);
        recurright(root.right,level+1,res);
        recurright(root.left,level+1,res);
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            Node root=null;
            for(int i=0;i<n;i++){
                int val=sc.nextInt();
                root=insert(root,val);
            }
            List<Integer>res= rightview(root);
            for(int i:res){
                System.out.print(i+" ");
            }
            System.out.println();
        }
    }
}

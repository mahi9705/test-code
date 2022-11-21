import java.util.Scanner;
import java.util.ArrayList;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> ans = new ArrayList<Integer>();
        int i = 1;
        while(ans.size()<n){
            ArrayList<Integer> a = new ArrayList<Integer>();
            while(i>0){
                a.add(i%10);
                i/=10;
            }
            if(!(a.contains(3)  a.contains(4)  a.contains(7))){
                ans.add(i);
            }
            i++;
        }
        System.out.println(ans.get(n-1));
    }
}
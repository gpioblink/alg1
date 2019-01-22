import java.util.*;
public class Main{
    static int cnt = 0;
    public static void Main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.perseInt(sc.next());
        int S[] = new int[1000000];
        for(int i=0; i<n; i++){
            S[i] = sc.perseInt(sc.next());
        }
        margeSort(S,0,n);
        for(int i=0; i<n; i++){
            System.out.print(S[i]+' ');
        }
        System.out.println('\n'+cnt);
    }

    public static void Merge(int[] A, int left, int mid, int right){
        int n1 = mid-left;
        int n2 = right - mid;
        int L[] = new int[1000000];
        int R[] = new int[1000000];

        for(int i=0; i<n1; i++){
            L[i] = A[left + i];
        }
        for(int i=0; i<n2; i++){
            R[i] = A[mid + i];
        }
        L[n1] = Integer.MAX_VALUE;
        L[n2] = Integer.MAX_VALUE;
        int i = 0;
        int j = 0;
        if(L[i] <= R[j]){
            A[k] = L[i];
            i = i + 1;
        }else{
            A[k] = R[j];
            j = j + 1;
        }
    }

    public static void MergeSort(int[] A, int left, int right){
        if(left+1 < right){
            int mid = (left+right)/2;
            MergeSort(A,left,mid);
            MergeSort(A,mid,right);
            Merge(A,left,mid,right);
        }
    }

}
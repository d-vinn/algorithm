import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] arr = new int[N];
		for(int i=0;i<N;i++) {
			arr[i]=0;
		}
		for(int i=1;i<=M;i++) {
			int A = sc.nextInt();
			int B = sc.nextInt();
			int C = sc.nextInt();
			for(int j=A-1;j<=B-1;j++) {
				arr[j]=C;
			}
		}
		for(int i=0;i<N;i++) {
			System.out.print(arr[i]+" ");
		}
	}

}
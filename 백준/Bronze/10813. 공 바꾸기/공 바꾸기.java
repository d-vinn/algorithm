import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(); //바구니 개수
		int M = sc.nextInt(); //바꾸는 횟수
		int[] arr = new int[N]; //바구니 
		for(int i=0;i<N;i++) {
			arr[i] = i+1;
		}
		for(int i=0;i<M;i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int c = arr[a-1];
			arr[a-1]=arr[b-1];
			arr[b-1]=c;
		}
		for(int i=0;i<N;i++) {
			System.out.print(arr[i]+" ");
		}
	}

}

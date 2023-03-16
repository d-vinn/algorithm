import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] count = new int[N];
		
		for(int i=0;i<N;i++) {
			count[i] = sc.nextInt();
		}
		
		int cnt = 0;
		int v = sc.nextInt();
		for(int j=0;j<count.length;j++) {
			if(v == count[j]) {
				cnt++;
			}
		}
		System.out.println(cnt);
	}

}

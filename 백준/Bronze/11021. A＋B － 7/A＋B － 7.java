import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		for(int i=1;i<=N;i++) {
			System.out.printf("Case #%d: %d\n", i, sc.nextInt()+sc.nextInt());
		}
	}

}

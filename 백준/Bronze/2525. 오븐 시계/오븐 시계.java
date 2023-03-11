import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();
		if(B+C>59) {
			if((A+(B+C)/60)>23) {
				System.out.printf("%d %d", (A+(B+C)/60)-24, (B+C)%60);
			}else {
				System.out.printf("%d %d", A+(B+C)/60, (B+C)%60);
			}
		}else {
			System.out.printf("%d %d", A, B+C);
		}
	}

}
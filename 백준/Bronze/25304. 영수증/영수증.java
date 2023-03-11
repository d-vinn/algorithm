import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int X = sc.nextInt();
		int N = sc.nextInt();
		int sum = 0;
		for(int i=1;i<=N;i++) {
			sum = sum + sc.nextInt()*sc.nextInt();
		}
		if(X==sum) {
			System.out.println("Yes");
		}else {
			System.out.println("No");
		}
	}

}

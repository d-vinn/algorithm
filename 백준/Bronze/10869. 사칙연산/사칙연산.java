import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		double A = sc.nextDouble();
		double B = sc.nextDouble();
		int C = (int)(A+B);
		int D = (int)(A-B);
		int E = (int)(A*B);
		int F = (int)(A/B);
		int G = (int)(A%B);
		System.out.println(C);
		System.out.println(D);
		System.out.println(E);
		System.out.println(F);
		System.out.println(G);
	}

}
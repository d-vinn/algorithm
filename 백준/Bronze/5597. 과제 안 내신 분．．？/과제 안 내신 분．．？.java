import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[31];
		
		for(int i=1;i<29;i++) {
			int success = sc.nextInt();
			arr[success] = 1;
		}
		
		for(int i=1;i<31;i++) {
			if(arr[i]!=1) {
				System.out.println(i);
			}
		}
		

	}

}

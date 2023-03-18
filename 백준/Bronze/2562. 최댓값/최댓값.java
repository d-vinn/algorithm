import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[9];
		for(int i=0;i<9;i++) {
			arr[i]=sc.nextInt();
		}
//		int[] new_arr = new int[9];
//		for(int i=0;i<9;i++) {
//			Arrays.sort(arr);
//			new_arr[i]=arr[i];
//		}
//		int max = new_arr[8];
//		for(int i=0;i<9;i++) {
//			if(arr[i]==max) {
//				System.out.println(max + "\n" + i);
//			}
//		}
		
		int count = 0;
		int max = 0;
		int index = 0;
		
		for(int value : arr) {
			count++;
			if(value>max) {
				max = value;
				index = count;
			}
		}
		System.out.println(max + "\n" + index);
	}

}

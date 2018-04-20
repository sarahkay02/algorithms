// determine if an integer is odd
public class Value {

	// determine if an integer is odd. maybe static
	public boolean isOdd(int n) {
		return (n % 2 == 1);
	}

	// use isOdd() and print out resulting values
	public static void main(String[] args) {
		for (int i=0; i<6; i++) {
			System.out.println(i + " " + isOdd(i));
		}
	}
}





// in head, use <link rel="stylesheet" href="main.css"? and put it in the same folder

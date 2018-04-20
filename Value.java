// determine if an integer is odd
public class Value {

	// determine if an integer is odd
	public boolean isOdd(int n) {
		return (n & 1) != 0;
	}

	// use isOdd() and print out resulting values
	public static void main(String[] args) {
		Value value = new Value();
		for (int i=-5; i<6; i++) {
			System.out.println(i + " " + value.isOdd(i));
		}
	}
}

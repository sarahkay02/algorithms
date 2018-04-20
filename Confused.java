
public class Confused {
	private static boolean indecision() {
		try {
			return true;
		} finally {
			int x = 1;
		}
	}
	

	public static void main(String[] args) {
		System.out.println(indecision());
	}

}

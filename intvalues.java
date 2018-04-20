
public class intvalues {
	
	private static void maxvals(int m) {
		System.out.println(m);
		for (int i=m-10; i <=m; i++) {
			System.out.println(i);
		}
	}

	public static void main(String[] args) {
		int maxvalue = Integer.MAX_VALUE;
		maxvals(maxvalue);
	}

}

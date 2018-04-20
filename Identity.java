
public class Identity {
	public static int[][] identity(int[][] A, int n) {
		for (int i=0; i < n; i++) {
			for (int j=0; j < n; j++) {
				if (i == j) {
					A[i][j] = 1;
				}
				
				else {
					A[i][j] = 0;
				}
			}
		}
		return A;
	}

	public static void main(String[] args) {
		int n = 3;
		int[][] A = new int[n][n];
		
		identity(A, n);
		
		// print out the array
		for (int i=0; i < n; i++) {
			for (int j=0; j < n; j++) {
				System.out.print(A[i][j] + " ");
			}
		System.out.println("\n");
		}
	}
}

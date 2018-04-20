import java.util.*;

public class passgen {
	public static Random rand = new Random();
	

	private static String passGen(int n) {
		String password = "";
		
		// 33-126 are type-able symbols (excludes ASCII codes such as "NULL", "TAB", or extended symbols
		// concatenate randomly generated characters to existing password
		for (int i=0; i < n; i++) {
			int character = 33 + rand.nextInt(94);			// 94 = (126 -33 + 1)
			password = password + (char)character;			// (char) casts int to ASCII symbol
		}
		
		return password;
	}


	public static void main(String[] args) {
		// generate and print 5 passwords of varying lengths (6-18 characters)
		for (int i=0; i < 5; i++) {
			int n = 8 + rand.nextInt(9);
			System.out.println(passGen(n));
		}
	}
}



// chance of repeated password, using 94 different possible symbols
// each char/digit has a 94 different possibilities, so the number of combinations for password of n chars is 94^n;
// 5 chars: 7,339,040,224 = 10^9
// 6 chars: 689,869,781,056 = 10^11
// 7 chars: 64,847,759,419,264 = 10^13
// ...
// 16 chars: 37,157,429,083,410,091,685,945,089,785,856 = 10^31

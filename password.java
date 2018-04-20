import java.util.Random;

public class password {
	public static Random rand = new Random();
	

	private static String passGen(int n) {
		String password = "";
		
		/* 65-90 are uppercase letters
		   97-122 are lowercase letters
		   48-57 are numbers
		   33-47, 58-64, 91-96 and 123-126 are various symbols
	    */
		
		// concatenate randomly generated characters to existing password
		for (int i=0; i < n; i++) {
			// first, pick the category of characters to choose from
			int category = rand.nextInt(4);
			int character = 0;
			
			// then choose the char within that category
			// uppercase
			if (category == 0) {			
				character = 65 + rand.nextInt(91-65);
			}
			
			// lowercase
			else if (category == 1) {
				character = 97 + rand.nextInt(123-97);
			}
			
			// numbers
			else if (category == 3) {
				character = 48 + rand.nextInt(58-48);
			}
			
			// symbols
			else {
				// pick a category of symbols to choose from
				int category2 = rand.nextInt(4);
				
				if (category2 == 0) {
					character = 33 + rand.nextInt(48-33);
				}
				
				else if (category2 == 1) {
					character = 58 + rand.nextInt(65-58);
				}
				
				else if (category2 == 2) {
					character = 91 + rand.nextInt(97-91);
				}
				
				else {
					character = 123 + rand.nextInt(127-123);
				}
			}
			
			password = password + (char)character;
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

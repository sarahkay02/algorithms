import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Lab12 {

    static String hashString(String message, String algorithm) {
        // compute the hash value of message using algorithm and return a string representation of it
        byte[] hashedBytes = null;        // will store the hash value of message

        try {
            // instantiate the specified algorithm
            // it may not exist, thus the try-catch
            MessageDigest digest = MessageDigest.getInstance(algorithm);

            // compute the hash value of the message
            hashedBytes = digest.digest(message.getBytes("UTF-8"));

        } catch (NoSuchAlgorithmException | UnsupportedEncodingException e) {
            e. printStackTrace();
        }

        // convert hash value (in byte[]) to a hex String and return result
        return bToH(hashedBytes);

    } // hashString()


    static String bToH(byte[] value) {
        // converts value to a String of hex digits
        StringBuilder sb = new StringBuilder(value.length*2);

        for (byte b : value) {
            sb.append(String.format("%02x",  b));        // each byte has 2 hex digits
            // need 2x the length of the string, since each byte has 2 hex digits, and each hex digit is a character, and each character needs a byte

        }

        return sb.toString();

    } // bToH


    public static void main(String[] args) {
        String digest = hashString("It was the best of times, it was the worst of times.\n", "MD5");
        System.out.println(digest);

    }

}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class converthex {

    public static String hexToString(String hex) {
        StringBuilder text = new StringBuilder();
        for (int i = 0; i < hex.length(); i += 2) {
            String byteString = hex.substring(i, i + 2);
            char ch = (char) Integer.parseInt(byteString, 16);
            text.append(ch);
        }
        return text.toString();
    }

    public static void main(String[] args) throws IOException {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            String input;
            while ((input = br.readLine()) != null) {
                String decoded = hexToString(input);
                System.out.println(decoded);
            }
        }
    }
}

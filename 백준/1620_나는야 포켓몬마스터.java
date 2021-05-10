import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class 백준_1620_나는야포켓몬마스터 {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		HashMap<String, String> pokemon = new HashMap<String, String>();
		for(int i=1;i<=N;i++) {
			String s = bf.readLine();
			pokemon.put(Integer.toString(i), s);
			pokemon.put(s, Integer.toString(i));
		}
		
		while(M-->0)
			System.out.println(pokemon.get(bf.readLine()));
		
	}

}

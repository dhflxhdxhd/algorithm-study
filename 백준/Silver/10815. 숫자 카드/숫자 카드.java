import java.io.*;
import java.util.*;

// 10815. 숫자 카드
public class Main {

    static int n,m;
    static int[] sang, cards, result;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        n = Integer.parseInt(br.readLine());
        sang = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            sang[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(sang);

        m = Integer.parseInt(br.readLine());
        cards = new int[m];
        result = new int[m];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }

        hasCards();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            sb.append(result[i]+" ");
        }

        System.out.println(sb);
    }

    private static void hasCards(){
        for (int i = 0; i < m; i++) {
            int status = findCard(cards[i]);
            result[i] = status;
        }
    }

    private static int findCard(int card){
        int result = 0;

        // 이분탐색으로 상근이가 카드를 가지고 있는지 확인
        int left = 0;
        int right = n-1;

        while(left <= right){
            int mid = left + (right - left) / 2;

            if(sang[mid] < card){
                left = mid + 1;
            }else if(sang[mid] > card){
                right = mid - 1;
            }else{
                result = 1;
                return result;
            }
        }

        return result;
    }
}


import java.io.*;
import java.util.*;

// 3079. 입국심사
public class Main {

    static int n,k;
    static long minTime = Long.MAX_VALUE;
    static int[] timeGroup;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken()); // 심사받는 사람 수

        timeGroup = new int[n]; // 심사대에서 소요되는 시간 모음
        long maxTime = 0;
        for (int i = 0; i < n; i++) {
            timeGroup[i] = Integer.parseInt(br.readLine());
            maxTime = Math.max(maxTime, timeGroup[i]);
        }
        Arrays.sort(timeGroup);

        getMinTime(maxTime);
        System.out.println(minTime);
    }

    private static void getMinTime(long maxTime){
        long left = 0; // 가장 작은
        long right = maxTime * k; // 최대 소요 시간
        while(left <= right){
            long mid = left + (right-left)/2; // 예상 최소 소요시간

            long available = 0;
            // mid값으로 모든 사람이 다 확인할 수 있는지 체크
            for(int time : timeGroup){
                long count = mid / time;

                if(available >= k){
                    break;
                }
                available += count;
            }

            if(available >= k){
                right = mid - 1;
                minTime = Math.min(minTime, mid);
            }else{
                left = mid + 1;
            }
        }
    }
}


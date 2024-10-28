
import java.io.*;
import java.util.*;

// 1039. 교환
class CountNum{
    int number;
    int count;

    public CountNum(int number, int count) {
        this.number = number;
        this.count = count;
    }
}
public class Main {

    static int maxValue = Integer.MIN_VALUE;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        getMaxValue(n,k);
        int result = maxValue == Integer.MIN_VALUE ? -1 : maxValue;
        System.out.println(result);
    }

    private static void getMaxValue(int n, int k){
        Queue<CountNum> queue = new ArrayDeque<>();
//        boolean[][] visited = new boolean[1000000+1][k+1];
        Set<String> visited = new HashSet<String>();

        queue.offer(new CountNum(n,0));
//        visited[n][0] = true;
        visited.add(n+","+0);

        while(!queue.isEmpty()){
            CountNum current = queue.poll();
            int currentNum = current.number;
            int currentCount = current.count;

            if(currentCount == k){
                maxValue = Math.max(maxValue, currentNum);
                continue;
            }

            int len = String.valueOf(currentNum).length();
            for(int i=0; i<len-1; i++){
                for(int j=i+1; j<len; j++){
                    int swapNumber = swapPlaces(currentNum, i, j);
                    String nextSet = swapNumber+","+(currentCount+1);
                    if (swapNumber != 0 && !visited.contains(nextSet)){
                        queue.offer(new CountNum(swapNumber, currentCount+1));
                        visited.add(nextSet);
                    }
//                    if(swapNumber != 0 && !visited[swapNumber][currentCount+1]){
//                        queue.offer(new CountNum(swapNumber, currentCount+1));
//                        visited[swapNumber][currentCount+1] = true;
//                    }
                }
            }
        }
    }

    private static int swapPlaces(int number, int idx1, int idx2){
        char[] numberArr = String.valueOf(number).toCharArray();
        char temp = numberArr[idx1];
        numberArr[idx1] = numberArr[idx2];
        numberArr[idx2] = temp;

        if(numberArr[0] == '0'){
            return 0;
        }else{
            return Integer.parseInt(new String(numberArr));
        }
    }
}

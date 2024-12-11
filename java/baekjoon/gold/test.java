package baekjoon.gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class test {
    static int N, cnt;
    static char[] signal;
    static boolean[] visited;
    static char[] orders = {'R', 'G', 'Y'};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        signal = br.readLine().toCharArray();
        visited = new boolean[N];

        dfs(0, "", 0);
        System.out.println(cnt);
    }

//    public static void dfs(int order, int currentIndex) {
//        if (order == 3) {
//            cnt++;
//            return;
//        }
//
//        for (int i = currentIndex; i < N; i++) {
//            if (signal[i] == orders[order]) {
//                dfs(order + 1, i + 1);
//            }
//        }
//    }

    public static void dfs(int depth, String str, int currentIdx) {
        System.out.println("Depth: " + depth + ", Current str: " + str + ", Visited: " + Arrays.toString(visited));
        if(depth == 3) {
            if(str.charAt(0) == 'R' && str.charAt(1) == 'G' && str.charAt(2) == 'Y') {
                cnt++;
            }
            return;
        }

        for (int i = currentIdx; i < N; i++) {
            if(!visited[i]) {
                visited[i] = true;
                dfs(depth + 1, str + signal[i], i+1);
                visited[i] = false;
            }
        }
    }
}

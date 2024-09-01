package baekjoon;

import java.io.*;
import java.util.*;

// 14719. 빗물
public class Boj_14719 {

    static int[][] world;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        st = new StringTokenizer(br.readLine());
        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        world = new int[h][w];
        st = new StringTokenizer(br.readLine());
    }
}

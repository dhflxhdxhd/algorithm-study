package baekjoon;

import java.io.*;
import java.util.*;

// 2151. 맥주 거울 설치
public class Boj_9205 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine()); // 테스트 케이스 개수

        int stores = Integer.parseInt(br.readLine()); // 맥주를 파는 편의점의 개수

    }

    /**
     * 맨해튼 거리를 이용해 두 좌표 사이의 거리를 계산하는 메소드
     * @param x1
     * @param x2
     * @param y1
     * @param y2
     * @return 두 좌표 사이의 거리
     */
    private static int getDistance(int x1, int x2, int y1, int y2){
        return Math.abs(x1-x2) + Math.abs(y1-y2);
    }
}

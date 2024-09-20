package baekjoon;

import baekjoon.model.BoardNode;
import baekjoon.model.Node;

import java.io.*;
import java.util.*;

// 2151. 거울 설치
public class Boj_2151 {

    static ArrayList<BoardNode> mirrors = new ArrayList<>(); // 거울을 설치할 수 있는 위치
    static char[][] map;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); // 집의 크기

        map = new char[n][n];
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < n; j++) {
                char temp = str.charAt(j);
                map[i][j] = str.charAt(j);

                if(temp == '!'){
                    mirrors.add(new BoardNode(i,j));
                }
            }
        }

    }
}

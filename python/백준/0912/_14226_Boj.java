package ssafy.Boj;

import java.io.*;
import java.util.*;

/*
14226. 이모티콘
저장 :화면에 있는 이모티콘 모두 복사 -> 클립보드에 저장
붙여넣기 : 클립보드에 있는 모든 이모티콘 -> 화면에 붙여넣기
1) if clipboard is empty -> X
2) 클립보드에 있는 이모티콘 개수가 화면에 추가
삭제 : 화면에 있는 이모티콘 중 하나 삭제

? S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값 ? 
*/

class Emoticons {
    int screen;
    int clipboard;
    int time;
    
    public Emoticons(int screen, int clipboard, int time) {
        super();
        this.screen = screen;
        this.clipboard = clipboard;
        this.time = time;
    } 
}


public class _14226_Boj {
    static int s;
    static boolean[][] visited; // visited[화면][클립보드]
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = Integer.parseInt(br.readLine());
        
        visited = new boolean[1001][1001];
        
        makeEmoticon();
        
    }
    
    static void makeEmoticon() {
        int new_cCount = 1;
        int new_sCount = 0;
        
        Queue<Emoticons> queue = new LinkedList<>();
        queue.offer(new Emoticons(1, 0, 0));
        
        while (!queue.isEmpty()) {
            Emoticons temp = queue.poll();
            int sCount = temp.screen;
            int cCount = temp.clipboard;
            int time = temp.time;
            
            visited[sCount][cCount] = true;
            if(sCount == s) {
                System.out.println(time);
                return;
            }
            

            for (int i = 0; i < 3; i++) {
                // 저장 : 화면에 있는 이모티콘 모두 복사 -> 클립보드에 저장
                if(i == 0 ) {
                	new_sCount = sCount;
                	new_cCount = sCount;
                // 붙여넣기 : : 클립보드에 있는 모든 이모티콘 -> 화면에 붙여넣기
                    
                }else if(i == 1 ) {
                    if(cCount != 0) {
                    	new_sCount = sCount + cCount;
                    	new_cCount = cCount;
                    }
                // 삭제    
                }else if(i == 2) {
                	new_sCount = sCount - 1;
                	new_cCount = cCount;
                }
                
                // 중복체크
                if(inArea(new_sCount, new_cCount) &&  !visited[new_sCount][new_cCount]) {
                    visited[new_sCount][new_cCount] = true;
                    queue.offer(new Emoticons(new_sCount, new_cCount, time+1));
                }
            }
        }
    }
    
    static boolean inArea(int sCount, int cCount) {
        return sCount > 0 && sCount < 1001 && cCount > 0 && cCount < 1001;
    }
}
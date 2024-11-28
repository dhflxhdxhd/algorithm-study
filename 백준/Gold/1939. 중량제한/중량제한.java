
import java.io.*;
import java.util.*;

// 1939. 중량제한
class Island {
    int destination;
    int weight;

    public Island(int destination, int weight) {
        this.destination = destination;
        this.weight = weight;
    }
}
public class Main {

    static int n,m;
    static List<Island>[] world;
    static boolean[] isVisited;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        world = new ArrayList[n+1];
        for(int i=1; i<n+1; i++) {
            world[i] = new ArrayList<>();
        }

        int maxWeight = Integer.MIN_VALUE;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            world[from].add(new Island(to, weight));
            world[to].add(new Island(from, weight));

            maxWeight = Math.max(maxWeight, weight);
        }

        st = new StringTokenizer(br.readLine());
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());

        int result = getPossibleMaxWeight(start, end, maxWeight);
        System.out.println(result);
    }

    private static int getPossibleMaxWeight(int start, int end, int maxWeight){
        int left = 0;
        int right = maxWeight;

        while(left <= right){
            int mid = left + (right - left)/2;
            isVisited = new boolean[n+1];
            if(canMove(start,end, mid)){
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }

        return left-1;
    }

    private static boolean canMove(int start, int end, int tempWeight){
        if(start == end){
            return true;
        }

        isVisited[start] = true;

        for (Island temp : world[start]){
            if(!isVisited[temp.destination] && temp.weight >= tempWeight){
                if(canMove(temp.destination, end, tempWeight)){
                    return true;
                }
            }
        }

        return false;
    }
}

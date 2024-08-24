import java.io.*;
import java.util.*;

class Node implements Comparable<Node>{
    int vertex; // 정점
    int weight; // 간선(가중치)

    public Node(int vertex, int weight) {
        this.vertex = vertex;
        this.weight = weight;
    }

    @Override
    public String toString() {
        return "(" + vertex + " , " + weight + ")";
    }

    // 가중치 기준 오름차순 정렬
    @Override
    public int compareTo(Node other) {
        return this.weight - other.weight;
    }
}

// 1238. 파티
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); // 학생 수 (정점)
        int m = Integer.parseInt(st.nextToken()); // 단방향 도로 개수 (간선)
        int x = Integer.parseInt(st.nextToken()); // 목적지

        List<List<Node>> adjList = new ArrayList<>(n+1);
        for (int i = 0; i <= n; i++) {
            adjList.add(new ArrayList<>());
        }

        for (int i = 1; i < m+1; i++) {
            st = new StringTokenizer(br.readLine());

            int startNode = Integer.parseInt(st.nextToken());
            int endNode = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            adjList.get(startNode).add(new Node(endNode, weight));
        }

//        int[] distance = new int[n+1];
//        Arrays.fill(distance, Integer.MAX_VALUE);
        int[][] distance = new int[n+1][n+1];
        for (int i = 0; i < n+1; i++) {
            Arrays.fill(distance[i], Integer.MAX_VALUE);
        }

        for (int i = 1; i < n+1 ; i++) {
            dijkstra(adjList, distance[i], i); // 목적지에서 각 집으로 돌아가는 경우
//            System.out.println(i+"번\t" + Arrays.toString(distance[i]));
        }

        int[] roundDistance = new int[n+1];
        Arrays.fill(roundDistance, 0);
        for (int i = 1; i < n+1; i++) {

            // 목적지 마을이라면
            if(i == x){
                roundDistance[i] = 0;
            }else{
                roundDistance[i] = distance[i][x] + distance[x][i]; // x번 마을까지 가는 최소비용 + 다시 집으로 돌아오는 최소비용
            }
        }

        int maxTime = Arrays.stream(roundDistance).max().getAsInt();
        System.out.println(maxTime);
    }

    private static void dijkstra(List<List<Node>> adjList, int[] distance, int start){
        PriorityQueue<Node> pq = new PriorityQueue<>();
        distance[start] = 0;
        pq.add(new Node(start, 0));

        while(!pq.isEmpty()){
            Node cNode = pq.poll();
            int cVertex = cNode.vertex;
            int cWeight = cNode.weight;

            for (Node adjNode : adjList.get(cVertex)){
                int newDist = cWeight + adjNode.weight;

                if(newDist < distance[adjNode.vertex]){
                    distance[adjNode.vertex] = newDist;
                    pq.add(new Node(adjNode.vertex, newDist));
                }
            }
        }
    }
}
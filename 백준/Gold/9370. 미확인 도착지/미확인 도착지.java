import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

// Node 클래스: 정점과 해당 정점까지의 가중치를 나타냄
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

// 9370. 미확인 도착지
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int T = Integer.parseInt(br.readLine()); // 테스트 케이스 수

        for (int test = 0; test < T; test++) {
            st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken()); // 교차로(정점) 개수
            int E = Integer.parseInt(st.nextToken()); // 도로(간선) 개수
            int t = Integer.parseInt(st.nextToken()); // 목적지 후보의 개수

            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken()); // 출발지
            int g = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());

            List<List<Node>> adjList = new ArrayList<>(V+1);
            for (int i = 0; i <= V; i++) {
                adjList.add(new ArrayList<>());
            }

            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int d = Integer.parseInt(st.nextToken());

                // a와 b 사이 가중치 d (양방향 도로)
                adjList.get(a).add(new Node(b,d));
                adjList.get(b).add(new Node(a,d));
            }


            int[] destOptions = new int[t]; // 목적지 후보 담는 배열
            for (int i = 0; i < t; i++) {
                destOptions[i] = Integer.parseInt(br.readLine());
            }

            int[] sDist = new int[V+1]; // 최단 경로 비용 담는 배열
            int[] gDist = new int[V+1]; // 최단 경로 비용 담는 배열
            int[] hDist = new int[V+1]; // 최단 경로 비용 담는 배열
            Arrays.fill(sDist, Integer.MAX_VALUE);
            Arrays.fill(gDist, Integer.MAX_VALUE);
            Arrays.fill(hDist, Integer.MAX_VALUE);

            dijkstra(adjList, sDist, start);
            dijkstra(adjList, gDist, g);
            dijkstra(adjList, hDist, h);

            List<Integer> dest = new LinkedList<>();

            // 목적지 후보만큼 체크
            for (int i = 0; i < t; i++) {
                int targetDest = destOptions[i];

                // 방법 1
                int gToh = sDist[g] + gDist[h] + hDist[targetDest];
                int hTog = sDist[h] + hDist[g] + gDist[targetDest];

                if(gToh == sDist[targetDest]){
                    dest.add(targetDest);
                }else if(hTog == sDist[targetDest]){
                    dest.add(targetDest);
                }
            }

            Collections.sort(dest);
            String result = dest.stream()
                    .map(String::valueOf)
                    .collect(Collectors.joining(" "));

            System.out.println(result);
        }
    }

    static void dijkstra(List<List<Node>> adjList, int[] distance, int start){
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
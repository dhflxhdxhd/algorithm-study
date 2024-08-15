// 데이크스트라(다익스트라) 알고리즘을 이용하여 입력 노드들 사이의 최단 경로와 최단 비용을 출력한다.
// Output the shortest path and shortest cost between input nodes using Dijkstra Algorithm 
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#define size 8


int path[size][size]; // 선행정점.
int check[size]; // 한 정점으로 가는 정점 표시
int distance[size]; // 최단 거리  
bool visited[size]; // 방문한 노드

// 그래프 -> 인접행렬
// 999는 무한값으로 임의 설정
int a[size][size] = {
	{0,1,7,2,999,999,999},
	{1,0,999,999,2,4,999,999},
	{7,999,0,999,999,2,3,999},
	{2,999,999,0,999,999,5,999},
	{999,2,999,999,0,1,999,999},
	{999,4,2,999,1,0,999,6},
	{999,999,3,5,999,999,0,2},
	{999,999,999,999,999,6,2,0}
};

// 출발 정점에서 갈 수 있는 각 노드의 최소비용. -> 출발
// 즉, 가장 최소 거리를 가지는 정점 반환
int get_smallest_node() {
	int min = 999;
	int index = 0; // 가장 최단 거리가 짧은 노드(인덱스)

	// 선형 탐색 : 반복 0~7
	for (int i = 0; i < size; i++) {
		// 조건이라면.
		// 조건 : 현재 최소 값보다 작은 비용 && 방문하지 않음
		if (distance[i] < min && !visited[i]) {
			// min값에 노드의 최소비용 값을 넣음. 
			min = distance[i];
			index = i;
		}
	}
	return index;
}

// path 인접행렬 초기화
void path_init(int path[][size]) {
	int i, j;
	for (i = 0; i < size; i++) {
		for (j = 0; j < size; j++) {
			path[i][j] = 999;
		}
	}
}

// 데이크스트라 함수 구성
void dijkstra(int start, int finish) {

	start = start - 1;
	finish = finish - 1;

	for (int i = 0; i < size; i++) {
		distance[i] = a[start][i];
		path[i][0] = start;
		check[i] = 1;
	}

	// 출발노드에서 출발노드는 0
	// 시작점 방문
	visited[start] = true;
	distance[start] = 0;

	for (int i = 0; i < size - 2; i++) {
		// 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문처리
		int now = get_smallest_node();
		visited[now] = true;

		// 현재 노드와 연결된 다른 노드 확인
		for (int j = 0; j < size; j++) {
			if (!visited[j]) {
				// 현재 노드를 거쳐서 노드에 인접한 노드로 이동하는 거리가 현재 그 노드로 가는 최소비용보다 더 작을 경우
				if (distance[now] + a[now][j] < distance[j]) {

					if (i == 0) {//처음에는 인접한 정점에 연결
						path[j][check[j]] = now + 1; //갱신된 경로를 경로 배열에 저장
						check[j]++;
					}
					else {
						for (int k = 0; k < (check[now] + 1); k++) {//저장된 만큼 반복
							path[j][k] = path[now][k]; //경로를 갱신
							path[j][k + 1] = now + 1; //끝부분에 자기자신을 저장
							check[j]++;
						}
					}
					distance[j] = distance[now] + a[now][j];
				}
			}
		}
	}

	//최단 경로 출력
	printf("%d번=>", start + 1);
	for (int j = 0; j < size; j++) {
		if (path[finish][j] != 0) {
			printf("%d번->", path[finish][j]);
		}
	}
	printf("%d번\n", finish + 1);

	// 최단 비용 출력
	int nodeToNode = distance[finish];
	printf("최단 비용 : %d\n", nodeToNode);


}

int main() {
	int start_node, finish_node;

	printf("시작 노드와 종료 노드를 선택하시오.\n");
	// 시작 노드 번호와 도착 노드 번호 입력 받음
	scanf_s("%d %d", &start_node, &finish_node);
	// 다익스트라 알고리즘을 이용

	// start_node부터 finish_node까지의 최단경로와 최단비용.
	dijkstra(start_node, finish_node);  // 1번 노드 -> 7번 노드
}


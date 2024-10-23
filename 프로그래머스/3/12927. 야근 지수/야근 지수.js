class MaxHeap {
    constructor() {
        this.heap = [];
    }

    insert(value) {
        this.heap.push(value);
        this.bubbleUp();
    }

    bubbleUp() {
        let index = this.heap.length - 1;
        const element = this.heap[index];

        while (index > 0) {
            let parentIndex = Math.floor((index - 1) / 2);
            let parent = this.heap[parentIndex];

            if (element <= parent) break; // 부모보다 작으면 종료
            this.heap[parentIndex] = element;
            this.heap[index] = parent;
            index = parentIndex;
        }
    }

    extractMax() {
        const max = this.heap[0];
        const end = this.heap.pop(); // 마지막 요소를 꺼냄
        if (this.heap.length > 0) {
            this.heap[0] = end;
            this.bubbleDown(); // 새로운 루트를 아래로 내림
        }
        return max;
    }

    bubbleDown() {
        let index = 0;
        const length = this.heap.length;
        const element = this.heap[0];

        while (true) {
            let leftChildIndex = 2 * index + 1;
            let rightChildIndex = 2 * index + 2;
            let leftChild, rightChild;
            let swap = null;

            if (leftChildIndex < length) {
                leftChild = this.heap[leftChildIndex];
                if (leftChild > element) {
                    swap = leftChildIndex;
                }
            }
            if (rightChildIndex < length) {
                rightChild = this.heap[rightChildIndex];
                if ((swap === null && rightChild > element) ||
                    (swap !== null && rightChild > leftChild)) {
                    swap = rightChildIndex;
                }
            }
            if (swap === null) break; // 더 이상 교환할 것이 없으면 종료
            this.heap[index] = this.heap[swap];
            this.heap[swap] = element;
            index = swap;
        }
    }

    isEmpty() {
        return this.heap.length === 0;
    }
}

function solution(n, works) {
    // 작업량이 0보다 큰 경우만 남긴다.
    works = works.filter(work => work > 0);

    // 우선순위 큐를 생성하고 작업량을 삽입
    const maxHeap = new MaxHeap();
    for (const work of works) {
        maxHeap.insert(work);
    }

    // n 시간이 남았을 때 피로도 최소화
    for (let i = 0; i < n; i++) {
        if (maxHeap.isEmpty()) break; // 남은 작업량이 없으면 종료

        // 가장 큰 작업량 감소
        const maxWork = maxHeap.extractMax(); // 최대 작업량 꺼내기
        if (maxWork > 1) {
            maxHeap.insert(maxWork - 1); // 작업량 감소 후 다시 넣기
        }
    }

    // 최종 피로도 계산
    let fatigue = 0;
    while (!maxHeap.isEmpty()) {
        const value = maxHeap.extractMax();
        fatigue += Math.pow(value, 2);
    }

    return fatigue;
}
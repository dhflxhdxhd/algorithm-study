#include <stdio.h>

// 쉘 정렬 함수 정의
void shellSort (int Arr[], int n) {
    // 간격 설정
    int gap = n/2;
    
    // 간격이 0보다 클 때까지 
    while(gap>0){
        // 간격이 짝수라면 홀수로 만들어 준다. 
        if((gap%2==0)){
            gap ++;
        }

        for (int i=0; i<gap; i++){
            // 서브리스트를 삽입정렬 이용하여 정렬
            for (int j=gap+i; j<n; j+=gap){
                int k = Arr[j];
                int l = j;
                
                while(l>gap-1 && Arr[l-gap]>k){
                    Arr[l] = Arr[l-gap];
                    l -= gap;
                }
                Arr[l] = k;
            }
        }
        // 간격을 다시 2로 나눠 계속 반복 실행
        gap = gap /2;
    }

    // 정렬한 리스트 출력
    for(int i=0; i<n; i++){
        printf("%d ", Arr[i]);
    }
    printf("\n");
}

int main(void) {
    // 정렬할 배열 설정
    int Array[] = {10, 8, 6, 20, 4, 3, 22, 1, 0, 15, 16};
    // Array의 요소 개수
    int ArraySize = sizeof(Array) / sizeof(int);

    // 쉘 정렬
    shellSort(Array,ArraySize);
}

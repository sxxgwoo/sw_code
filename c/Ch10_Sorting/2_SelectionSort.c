#include <stdio.h>

// 선택 정렬 함수: 오름차순 정렬
void SelSort(int arr[], int n)
{
	int i, j;
	int maxIdx;
	int temp;

	// i: 현재 정렬 위치 (왼쪽에서부터 정렬 시작)
	for(i = 0; i < n - 1; i++)
	{
		// i번째 위치에 올 가장 작은 값의 인덱스를 찾기 시작
		maxIdx = i;

		// i 이후의 구간에서 최소값의 인덱스를 찾음
		for(j = i + 1; j < n; j++)
		{
			if(arr[j] < arr[maxIdx])
				maxIdx = j;  // 더 작은 값이 있으면 인덱스 갱신
		}

		// 현재 위치(i)와 최소값 위치(maxIdx)를 교환
		temp = arr[i];
		arr[i] = arr[maxIdx];
		arr[maxIdx] = temp;
	}
}

int main(void)
{
	int arr[4] = {3, 4, 2, 1};  // 정렬할 배열
	int i;

	// 배열 크기 구해서 요소 개수 전달
	SelSort(arr, sizeof(arr) / sizeof(int));

	// 정렬된 결과 출력
	for(i = 0; i < 4; i++)
		printf("%d ", arr[i]);

	printf("\n");
	return 0;
}
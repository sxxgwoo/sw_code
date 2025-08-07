#include <stdio.h>

// 버블 정렬 함수: 오름차순 정렬
void BubbleSort(int arr[], int n)
{
	int i, j;
	int temp;

	// 총 n-1회 반복 (가장 큰 수를 뒤로 밀어냄)
	for(i = 0; i < n - 1; i++)
	{
		// 정렬되지 않은 구간에서 인접한 두 수를 비교
		for(j = 0; j < (n - i) - 1; j++)
		{
			// 앞의 수가 뒤의 수보다 크면 자리 교환
			if(arr[j] > arr[j + 1])
			{
				// swap
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}

int main(void)
{
	int arr[4] = {3, 2, 4, 1};   // 정렬할 배열
	int i;

	// 배열 크기를 요소 개수로 변환하여 전달
	BubbleSort(arr, sizeof(arr) / sizeof(int));

	// 정렬된 결과 출력
	for(i = 0; i < 4; i++)
		printf("%d ", arr[i]);

	printf("\n");
	return 0;
}
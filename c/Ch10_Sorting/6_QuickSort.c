#include <stdio.h>

// 배열의 두 요소를 교환하는 함수
void Swap(int arr[], int idx1, int idx2)
{
	int temp = arr[idx1];
	arr[idx1] = arr[idx2];
	arr[idx2] = temp;
}

// 배열을 분할하는 함수 (퀵 정렬의 핵심)
int Partition(int arr[], int left, int right)
{
	int pivot = arr[left];     // 피벗: 가장 왼쪽 값을 기준으로 선택
	int low = left + 1;        // 왼쪽에서 오른쪽으로 이동하는 포인터
	int high = right;          // 오른쪽에서 왼쪽으로 이동하는 포인터

	while (low <= high)        // 포인터가 교차하기 전까지 반복
	{
		// pivot보다 큰 값을 만날 때까지 low 증가
		while (pivot >= arr[low] && low <= right)
			low++;

		// pivot보다 작은 값을 만날 때까지 high 감소
		while (pivot <= arr[high] && high >= left + 1)
			high--;

		// low와 high가 교차하지 않았으면 두 값을 교환
		if (low <= high)
			Swap(arr, low, high);
	}

	// 피벗과 high 위치 값을 교환하여 피벗을 제자리로 이동
	Swap(arr, left, high);

	// 피벗의 최종 위치를 반환
	return high;
}

// 퀵 정렬 함수 (재귀 호출로 구현)
void QuickSort(int arr[], int left, int right)
{
	if (left <= right)    // 정렬할 구간이 남아있다면
	{
		// 피벗 기준으로 배열을 분할하고 피벗 위치를 받아옴
		int pivot = Partition(arr, left, right);

		// 왼쪽 부분 배열 정렬
		QuickSort(arr, left, pivot - 1);

		// 오른쪽 부분 배열 정렬
		QuickSort(arr, pivot + 1, right);
	}
}

int main(void)
{
	int arr[7] = {3, 2, 4, 1, 7, 6, 5};  // 일반적인 예시
	// int arr[3] = {3, 3, 3};                // 중복값이 있는 예시

	int len = sizeof(arr) / sizeof(int);  // 배열의 길이 계산
	int i;

	// 배열 전체를 퀵 정렬 수행
	QuickSort(arr, 0, len - 1);

	// 정렬 결과 출력
	for (i = 0; i < len; i++)
		printf("%d ", arr[i]);

	printf("\n");
	return 0;
}

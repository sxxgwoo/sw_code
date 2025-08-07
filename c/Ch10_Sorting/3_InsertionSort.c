#include <stdio.h>

// 삽입 정렬 함수: 오름차순 정렬
void InserSort(int arr[], int n)
{
	int i, j; // 여기에 선언을 했기에 마지막 j가 for문 밖을 나와도 살아있음
	int insData;

	// i = 현재 삽입하려는 값의 인덱스 (두 번째 원소부터 시작)
	for(i = 1; i < n; i++)
	{
		insData = arr[i];   // 삽입할 데이터를 임시로 저장

		// 이미 정렬된 왼쪽 부분 배열에서 insData가 들어갈 위치 찾기
		for(j = i - 1; j >= 0; j--)
		{
			if(arr[j] > insData)
				arr[j + 1] = arr[j];  // 현재 값보다 크면 오른쪽으로 한 칸 이동
			else
				break;  // insData보다 작거나 같으면 그 위치 뒤가 삽입 위치
		}

		// 찾은 위치에 insData 삽입
		arr[j + 1] = insData;
	}
}

int main(void)
{
	int arr[5] = {5, 3, 2, 4, 1};  // 정렬할 배열
	int i;

	// 배열 크기 전달
	InserSort(arr, sizeof(arr) / sizeof(int));

	// 정렬 결과 출력
	for(i = 0; i < 5; i++)
		printf("%d ", arr[i]);

	printf("\n");
	return 0;
}
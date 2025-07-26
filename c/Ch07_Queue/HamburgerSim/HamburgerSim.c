#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "CircularQueue.h"

#define CUS_COME_TERM 15

#define CHE_BUR 0
#define BUL_BUR 1
#define DUB_BUR 2

#define CHE_TERM 12
#define BUL_TERM 15
#define DUB_TERM 24

int main(void)
{
    int makeProc = 0;   // 조리 중인 햄버거가 얼마나 시간이 남았는지 저장
    int cheOrder = 0, bulOrder = 0, dubOrder = 0;  // 주문 받은 햄버거 종류별 개수 저장
    int sec = 0;  // 시간 저장

    Queue que;
    QueueInit(&que);

    srand(time(NULL));

    // 아래 for문의 1회 회전은 1초의 시간 흐름을 의미함
    for(sec = 0; sec < 3600; sec++)
    {
        if(sec % CUS_COME_TERM == 0)    // 손님이 들어오는 시간
        {
            switch(rand() % 3)  // 손님이 주문하는 버거 종류 (랜덤 선택)
            {
                case 0:
                    Enqueue(&que, CHE_TERM);  // 치즈버거 주문
                    cheOrder++;
                    break;
                case 1:
                    Enqueue(&que, BUL_TERM);  // 불고기버거 주문
                    bulOrder++;
                    break;
                case 2:
                    Enqueue(&que, DUB_TERM);  // 더블버거 주문
                    dubOrder++;
                    break;
            }
        }

        if(makeProc <= 0 && !QIsEmpty(&que))  // 조리 중인 햄버거가 없고 주문이 있는 경우
            makeProc = Dequeue(&que);  // 조리 중인 햄버거 시간 저장
        
        makeProc--;  // 조리 중인 햄버거 시간 감소
    }

    printf("Simulation Report! \n");
    printf(" - Cheese burger: %d \n", cheOrder);
    printf(" - Bulgogi burger: %d \n", bulOrder);
    printf(" - Double burger: %d \n", dubOrder);
    printf(" - Waiting room size: %d \n", QUEUE_LEN);

    return 0;
}

#include <string.h>
#include <ctype.h>
#include "ListBaseStack.h"

int EvalRPNExp(char exp[])
{
    Stack stack;
    int expLen = strlen(exp);
    int i;
    char tok, op1, op2;

    StackInit(&stack);

    for(i = 0; i < expLen; i++) // 수식을 구성하는 문자를 하나씩 차례대로 읽으면서 처리
    {
        tok = exp[i];   // 한 문자씩 tok에 저장

        if(isdigit(tok))  // 문자가 정수인지 확인
        {
            SPush(&stack, tok - '0');  // 정수인 경우 숫자로 변환하여 스택에 푸시
        }
        else  // 연산자인 경우
        {
            op2 = SPop(&stack);  // 두 번째 피연산자를 스택에서 꺼냄
            op1 = SPop(&stack);  // 첫 번째 피연산자를 스택에서 꺼냄

            switch(tok)  // 연산자에 따라 계산 수행
            {
                case '+':
                    SPush(&stack, op1 + op2);
                    break;
                case '-':
                    SPush(&stack, op1 - op2);
                    break;
                case '*':
                    SPush(&stack, op1 * op2);
                    break;
                case '/':
                    SPush(&stack, op1 / op2);
                    break;
            }
        }
    }

    return SPop(&stack);  // 최종 계산 결과를 반환
}
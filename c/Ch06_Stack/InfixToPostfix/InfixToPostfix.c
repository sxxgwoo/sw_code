#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include "ListBaseStack.h"

int GetOpPrec(char op)  // 연산자의 우선순위 반환
{
    switch(op)
    {
        case '*':
        case '/':
            return 5;   // 가장 높은 연산의 우선순위
        case '+':
        case '-':
            return 3;   // 두 번째로 높은 연산의 우선순위
        case '(':
            return 1;   // 가장 낮은 연산의 우선순위
    }

    return -1;  // 등록되지 않은 연산자 -1 반환
}

int WhoPrecOp(char op1, char op2)  // 연산자의 우선순위 비교
{
    int op1Prec = GetOpPrec(op1);
    int op2Prec = GetOpPrec(op2);

    if(op1Prec > op2Prec)
        return 1;  // op1의 우선순위가 더 높으면 1 반환
    else if(op1Prec < op2Prec)
        return -1;  // op2의 우선순위가 더 높으면 -1 반환
    else
        return 0;  // 우선순위가 같으면 0 반환
}

void ConvToRPNExp(char exp[])  // 중위 표기법을 후위 표기법으로 변환
{
    Stack stack;
    int expLen = strlen(exp);
    char * convExp = (char*)malloc(expLen + 1);  // 변환된 표기법을 저장할 문자열 공간 할당

    int i, idx = 0;
    char tok, popOp;

    memset(convExp, 0, sizeof(char) * expLen + 1);  // 변환된 표기법을 저장할 문자열 공간을 0으로 초기화

    StackInit(&stack);  // 스택 초기화

    for(i = 0; i < expLen; i++)
    {
        tok = exp[i];   // exp로 전달된 수식을 한 문자씩 tok에 저장

        if(isdigit(tok))  // tok에 저장된 문자가 숫자인지 확인
        {
            convExp[idx++] = tok;  // 숫자인 경우 변환된 표기법에 추가
        }
        else  // 숫자가 아닌 연산자인 경우
        {
            switch(tok)
            {
                case '(':
                    SPush(&stack, tok);  // 여는 괄호인 경우 스택에 추가
                    break;
                case ')':
                    while(1)  // 닫는 괄호인 경우 스택에서 여는 괄호가 나올 때까지 모든 연산자를 변환된 표기법에 추가
                    {
                        popOp = SPop(&stack);  // 스택에서 연산자를 꺼냄
                        if(popOp == '(')  // 여는 괄호가 나오면 반복문 종료
                            break;
                        convExp[idx++] = popOp;  // 연산자를 변환된 표기법에 추가
                    }
                    break;
                
                case '+':
                case '-':
                case '*':
                case '/':
                    while(!SIsEmpty(&stack) && WhoPrecOp(SPeek(&stack), tok) >= 0)  // 스택에 남아있는 연산자의 우선순위가 현재 연산자의 우선순위보다 높거나 같은 경우
                        convExp[idx++] = SPop(&stack);  // 스택에서 연산자를 꺼내 변환된 표기법에 추가
                    
                    SPush(&stack, tok);  // 현재 연산자를 스택에 추가
                    break;
            }
        }
    }

    while(!SIsEmpty(&stack))    // 스택에 남아있는 모든 연산자를,
        convExp[idx++] = SPop(&stack);  // 변환된 표기법에 추가

    strcpy(exp, convExp);  // 변환된 표기법을 exp로 복사
    free(convExp);  // 변환된 표기법을 저장할 문자열 공간 해제
}
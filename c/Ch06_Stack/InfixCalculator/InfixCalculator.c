#include <string.h>
#include <stdlib.h>
#include "InfixToPostfix.h"
#include "PostCalculator.h"

int EvalInfixExp(char exp[])
{
    int len = strlen(exp);
    int ret;
    char * expcpy = (char*)malloc(len + 1);     // 수식을 저장할 문자열 공간 할당

    strcpy(expcpy, exp);  // 수식을 복사
    ConvToRPNExp(expcpy);  // 중위 표기법을 후위 표기법으로 변환
    ret = EvalRPNExp(expcpy);  // 후위 표기법을 계산
    free(expcpy);  // 문자열 공간 해제

    return ret;  // 계산 결과 반환
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "ListBaseStack.h"
#include "BinaryTree2.h"

BTreeNode * MakeExpTree(char exp[])
{
	Stack stack;            // 트리 노드를 임시 저장할 스택
	BTreeNode * pnode;      // 새로 생성할 노드 포인터

	int expLen = strlen(exp);
	int i;

	StackInit(&stack);         // 스택 초기화

	for(i=0; i<expLen; i++)    // 수식을 한 문자씩 순회
	{
		pnode = MakeBTreeNode();  // 새 노드 생성

		if(isdigit(exp[i]))		// 피연산자인 경우
		{
			SetData(pnode, exp[i]-'0');   // 문자를 정수로 바꿔서 저장
		}
		else					// 연산자인 경우
		{
			MakeRightSubTree(pnode, SPop(&stack));
			MakeLeftSubTree(pnode, SPop(&stack));
			SetData(pnode, exp[i]);
		}

		SPush(&stack, pnode);   // 새로 만든 노드를 스택에 push
	}

	return SPop(&stack);     // 마지막에 남은 노드가 루트 노드 → 반환
}

int EvaluateExpTree(BTreeNode * bt)  // 수식 트리를 재귀적으로 순회하여 전체 수식을 계산하는 함수
{
	int op1, op2;

	if(GetLeftSubTree(bt)==NULL && GetRightSubTree(bt)==NULL)  // 리프 노드(숫자 노드)인 경우 → 해당 값 반환
		return GetData(bt);

	op1 = EvaluateExpTree(GetLeftSubTree(bt));   // 왼쪽 subtree를 재귀적으로 평가
	op2 = EvaluateExpTree(GetRightSubTree(bt));  // 오른쪽 subtree를 재귀적으로 평가

	switch(GetData(bt))
	{
	case '+':
		return op1+op2;
	case '-':
		return op1-op2;
	case '*':
		return op1*op2;
	case '/':
		return op1/op2;
	}

	return 0;
}

void ShowNodeData(int data)
{
	if(0<=data && data<=9)
		printf("%d ", data);    // 피연산자 출력
	else
		printf("%c ", data);    // 연산자 출력
}

void ShowPrefixTypeExp(BTreeNode * bt)    // 전위 표기법으로 수식 출력
{
	PreorderTraverse(bt, ShowNodeData);
}

void ShowInfixTypeExp(BTreeNode * bt)     // 중위 표기법으로 수식 출력
{
	if(bt == NULL)
		return;
	
	if(bt->left != NULL || bt->right != NULL)   // 숫자는 두 자식이 모두 NULL
		printf(" ( ");
		
	ShowInfixTypeExp(bt->left);    // 첫 번째 피연산자 출력
	ShowNodeData(bt->data);        // 연산자 출력
	ShowInfixTypeExp(bt->right);   // 두 번째 피연산자 출력

	if(bt->left != NULL || bt->right != NULL)
		printf(" ) ");
}

void ShowPostfixTypeExp(BTreeNode * bt)   // 후위 표기법으로 수식 출력
{
	PostorderTraverse(bt, ShowNodeData);
}
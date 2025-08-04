#ifndef __EXPRESSION_TREE_H__
#define __EXPRESSION_TREE_H__

#include "BinaryTree2.h"

BTreeNode * MakeExpTree(char exp[]);   // 수식 트리 구성 (후위 표기법 기반)
int EvaluateExpTree(BTreeNode * bt);   // 수식 트리 계산

void ShowPrefixTypeExp(BTreeNode * bt);  // 수식 트리의 수식을 전위 표기법 기반 출력
void ShowInfixTypeExp(BTreeNode * bt);   // 수식 트리의 수식을 중위 표기법 기반 출력
void ShowPostfixTypeExp(BTreeNode * bt); // 수식 트리의 수식을 후위 표기법 기반 출력

#endif
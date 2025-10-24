#include <stdio.h>

int main(void)
{
    // 상수
    const int age = 12;
    printf("%d\n", age);

    int input;
    printf("값을 입력하세요 : ");
    scanf_s("%d", &input);
    printf("%d\n", input);

    return 0;
}
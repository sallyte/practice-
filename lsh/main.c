// #include <stdio.h>
// int main()
// {
//     printf("hello world!!! \n");
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int num;
//     scanf("%d",&num);
//     switch(num) {
//     case 1:
//         printf("1을 입력\n");
//         break;
//     case 2:
//         printf("2을 입력\n");
//         break;
//     case 3:
//         printf("3을 입력\n");
//         break;
//     default:
//         printf("입력오류\n");
//         break;


//     }
//     return 0;
// }


// #include <stdio.h>
// int main() {
//     int i, j;
//     for (i =2; i <= 4; i++){
//         for (j = 5; j <= 7; j++) {
//         }
//     }
//     printf("%d x %d = %2d", j , i, i*j);
// }

#include <stdio.h>
main() {
    int a;
    printf("정수입력 : ");
    scanf("%d", &a);
    if a %3 == 0 && 
       a %7 == 0
        printf("3의배수이면서 7의 배수가 아님\n");
    else
        printf("3의배수이면서 7의 배수가 아님\n");
}
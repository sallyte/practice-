// #include <stdio.h>
// int main(){
//     int a[5] = {5,4,3,2,1};
//     int i = 4, sum =0;
//     do {
//         a[i] = a[i] % 3;
//         sum = sum + a[i];
//         i--;
//     } while(i > 0);
//    printf("%d" , sum);
// }

// #include <stdio.h>
// int main()
// {
//     int* pnum, Num1 =200, Num2 =300;
//     pnum = &Num1;
//     (*pnum) += 40;
//     pnum = &Num2;
//     (*pnum) -= 50;
//     printf("Num1=%d\nNum2=%d" , Num1, Num2);
// }


// #include <stdio.h>
// hrd(num) {
//     if (num <= 0)
//         return;
//     printf("%d ", num);
//     hrd(num -1);

// }
// int main() {
//     hrd(5);
//     return 0;
// }

// #include <stdio.h>
// int main(int argc, char* argv[]) {
//     int i;
//     char str[4];

//     str[0] = 'K';
//     str[1] = 'O';
//     str[2] = 'R';
//     str[3] = 'E';
//     str[4] = 'A';

//     for (i =0; i < 5; i++) {
//         printf("%c", str[i]);
//     }
//     return 0;
// }

// #include <stdio.h>
// int main() {
//     for (int i = 9; i > 0; i--) {
//         switch(i % 2){
//         case 1:
//             printf("%d", i);
//             break;
//         default:
//             printf("*");
//             break;
//         }
//     }
//     return 0;
// }

// #include <stdio.h>
// int main() {
//     int a, b = 10;
//     for (a =0; a < 5; ++a, b -= a);
//     printf("%d, %d" , a, b);
// }

// #include <stdio.h>
// int main() {
//     int numAry[] = {0,0,0,0,3};
//     int i, j;
//     for (j= 4; j >= 0; --j)
//         for (i = 4; i > j; --i)
//             numAry[j] += numAry[i];
//     for (j = 0; j < 5; ++j)
//     printf("%d " , numAry[j]);
// }

// #include <stdio.h>
// #include <string.h>
// #include <stdlib.h>

// int main()
// {
//     char a[] = "A B c  D e  F !";
//     delbl(a);
//     printf("%s", a);
//     return 0;

// }

// void delbl(char a[])
// {
//     int len = strlen(a);
//     char* str = (char*)malloc(sizeof(char) * len);
//     int i, k= 0;

//     for(i = 0; i < len; i++)
//     {
//         if(a[i] != ' ')
//             str[k++] = a[i];
//     }
//     str[k] = '\0';
//     strcpy(a, str);
//     free(str);
// }

// #include <stdio.h>

// int main() {
//     int i, a[5], cnt = 0;
//     for (i = 0; i< 5; i++)
//         scanf("%d", &a[i]);
//     for (i = 0; i < 5; i++){
//         if (a[i] % 2 != 0)
//             cnt = cnt + 1;
//     }
//     printf("홀수의 개수 : %d개", cnt);
// }


// #include <stdio.h>
// int isprime(int number)
// {
//     int i;
//     for(i = 2; i < number; i++)
//         if(number)
//             return 0;
//         return 1;
// }

// int main()
// {
//     int number = 99, cnt = 0, i;
//     for(i = 2; i <== number; i++)
//         cnt = cnt + isprime(i);
//     printf("%d를 넘지 않는 소수는  %d개입니다.\n", number, cnt);
//     return 0;
// }


// #include <stdio.h>
// int Fibonacci(int n){
//     if(n==0)
//      return 0;
//     else if(n==1)
//         return 1;
//     else
//     return Fibonacci(n-2) + Fibonacci(n-1);
// }

// int main(void) {
//     int i=0;
//     for(i=0; i<10; i++)
//         printf("%d", Fibonacci(i));
//     return 0;
// }


// #include <stdio.h>
// #define SIZE 4

// int main() {
//     int test[SIZE][SIZE] = {0, };
//     int i ,j;
//     for(i = 0; i< SIZE; i++) {
//        for(j = 0; j< SIZE; j++){
//         if(i >=j)
//             test[i][j] = i-j;
//         else
//             test[i][j] = j-i;
//     }
// }
// for(i = 0; i < SIZE; i++) {
//     for(j =0; j < SIZE; j++){
//         printf("%d", test[i][j]);
//     }
//     printf("\n");
// }
// return 0;
// }


// #include <stdio.h>

// int main() {
//     int a = sizeof(int) + sizeof(char);
//     printf("%d", a);
// }

// #include <stdio.h>
// #include <math.h>

// int main(){
//     int ans = pow(2, ceil(M_PI));
//     printf("%d", ans);
// }


// #include <stdio.h>
// #include <string.h>

// int main() {
//     char a[11] ="KOREA";
//      printf("%lu\n", strlen(a));
//      printf("%lu\n", sizeof(a));
//     char b[] ="12345";
//      printf("%lu\n", sizeof(b));

//     strcat(a,b);
//     puts(a);
//     // printf("%lu\n", sizeof(a));
   
//     // printf("배열a의 크기: %lu\n",sizeof(a));
//     printf("%s", b);
//     return 0;
// }

// #include <stdio.h>

// int main(){
//     int i, j, sum =0;
//     for (i =2; i <=5; i++)
//         for(j =1; j < i; j++)
//             sum =sum + j;
//     printf("%d", sum);
//     return 0;
// }

// #include <stdio.h>
// #define MAX 10

// int main(){
//     int cur = 1, prev =0, tmp , i;

//     for( i =0; i < MAX; i++)
//     {
//         printf("%d", cur);
//         tmp = prev;
//         prev = cur;
//         cur =cur + tmp;
//         if (i % 5 == 4)
//          printf("\n");
//         else
//         printf("-");
//     }
//     return 0;
// }

// #include <stdio.h>
// #include <stdbool.h>

// bool test(int a){
//     bool ans = a < 150 ? true :false;
//     return ans;
// }
// int fact(int i){
//     if (i < 2) return 1;
//     else return i*fact(i-1);
// }

// int main()
// {
//     int ans = 0;
//     for (int i =0; i < 10; i++)
//         if(test(fact(i)))
//             ans++;
//     printf("%d", ans);
//     return 0;
// }

// #include <stdio.h>

// void intswap(int *x, int *y)
// {
//     int t;

//     t = *x;
//     *x = *y;
//     *y = t;
// }

// void testfunc(int *a, int *b, int *c)
// {
//     if (*c %2 ==0)
//         intswap(a, b);
//     else
//         intswap(a,c);
// }

// int gcd(int a, int b)
// {
//     if (b == 0)
//         return 1;
//     else
//         return gcd(b, a % b);
// }
// int main()
// {
//     int a =5;
//     int b =4;
//     int test1 =15;
//     int test2 =12;
//     int test =gcd(test1,test2);

//     switch(test % 2)
//     {
//         case 1:
//             testfunc(&a, &b, &test2);
//         defalt:
//             testfunc(&a, &b, &test1);
//     }
//     printf("%d-%d", a, b);
//     return 0;
// }


// #include <stdio.h>

// int main()
// {
//     int x = 5, y = 10, z= 20, sum;
//     x += y;
//     y -= x;
//     z %= y;
//     sum = x +y + z;
//     printf("%d", sum);
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int ans= 0;
     
//     for(int i= 0; i< 5; i++)
//         for(int j =0; j < 5; j++)
//             if (i==j || i+j==4) ans++;

//     printf("%d", ans);
//     return 0;
// }

#include <stdio.h>
#include <stdbool.h>

bool test(int a)
{
    if (a % 2 == 1) return true;
    else return false;
}
int main()
{
    int res = 0;
    int tmp;
    for (int i =0; i < 6; i++)
        for (int j =0 ; j < 6; j++)
        {
            if (test(i+j)) tmp =i;
            else tmp =0;
            res += tmp
        }
    printf("%d", res);
    return 0;
}
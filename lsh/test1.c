// #include <stdio.h>
// int main() {
//     int a;
//     printf("정수입력 : ");
//     scanf("%d", &a);
//     if (a % 3 == 0 && a % 7 == 0)
//         printf("3의배수이면서 7의 배수임\n");
//     else
//         printf("3의배수이면서 7의 배수가 아님\n");
// }

// #include <stdio.h>
// int main()
// {
//     double num = 0.01;
//     double res = 0;
//     int cnt = 0;
//     while(cnt < 100)
//     {
//         res += num;
//         cnt++;
 
//     }
//     printf(res >= 1 ? "true" : "false");
//         return 0;
// }


// #include <stdio.h>
// int main() {
//     int num = 1;
//     for (int i = 1; ; i++) {
//         num =num * i;
//         if(i>5)
//         break;
//     }
//     printf("%d",num);
// }

// #include <stdio.h>
// #define N 100
// int main() {
//     int i = 1;
//     int cnt = 0;
    
//     while (i <= N) {
//         if ((i % 3) == 0 && (i % 7) == 0){
//             cnt++;
//             printf("%d*%d*", cnt, i);
//         }
//         i++;
//     }
// }


// #include <stdio.h>
// int main()
// {
//     int n1 = 172;
//     int n2 = 387;

//     while( n1 != n2)
//     {
//         if (n1 > n2) n1-=n2;
//         else n2-=n1;

//     }

//     printf("%d", n1);
    
//     return 0;

// }

// #include <stdio.h>
// int main()
// {
//     char a[] = {'1','B','C','D','E'};
//     char *p;
//     p = &a[2];
//     printf("%C%C", *p, *(p-2));
//     return 0;
// }


// #include <stdio.h>
// int main() {
//     int i, a[5], temp;
//     for (i = 0; i < 5; i++){
//         a[i] = i + 1;
//         printf("%d", a[i]);
//     }
//     printf("\n");
//     temp = a[0];
//     for (i = 0; i < 4; i++){
//         a[i] = a[i+1];

//       a[4] = temp;
//     for (i =0; i < 5; i++){
//         printf("%d", a[i]);
//     }
//     }
// }



// <p.194>
// #include <stdio.h>
// int main()
// {
//     int a[5] = {3,2,5,1,4};
//     int temp, i;
//     for (i = 0; i < 4; i++)
// {
//     temp =a[i];
//     a[i] = a[i+1];
//     a[i+1] =temp;
// }
// for (i =0; i < 5; i++)
// {
//     printf("%d", a[i]);
// }
// }

// #include <stdio.h>
// int main() {
//     int len = 0;
//     char str[50];
//     gets(str);
//     for (int i =0; str[i]; i++)
//         len += 1;
//     printf("%d", len);
// }

// #include <stdio.h>
// int main() {
//     int i = 0, sum = 0;
//     int a[10] = {47,104,30,65,46,80,51,106,61,62};
//     for (i =0; i < 10; i= i+2)
//         sum =sum +a[i];
//     printf("%d", sum);
// }


// #include <stdio.h>
// int main()
// {
//     int map[5][5] = {
//         1,5,6,7,8,
//         2,4,6,4,9,
//         1,5,7,4,2,
//         2,3,4,5,5,
//         5,2,4,1,1 };
//     int i = 0, j = 0;
//     int res = map[i][j];
//     while(1)
//     {
//         if (i == 4 && j == 4)break;
//         else if(i == 4) j++;
//         else if(i == 4) i++;
//         else if(map[i+1][j] >= map[i][j+1]) j++;
//         else
//             i++;
//             res += map[i][j];
//     }
//     printf("result : %d", res);
//     return 0;

//     }


// #include <stdio.h>
// main()
// {
//    int a[10] = {3, 7 , 9 , 4 , 5 , 1 , 8 ,2 , 6, 10};
//    int i;
//    for (i = 0; i < 10; i++)
//    {
//     if(i % 3 == 2)
//     {
//         printf("%d", a[i]);
//     }
//    } 
// }


// #include <stdio.h>
// #include <string.h>

// int main()
// {
//     int k, n;
//     char st[] = "I am Tom!";
//     char temp;
//     n = strlen(st);
//     n--;
//     for  (k = 0; k< n; k++)
//     {
//         temp = *(st + k);
//         *(st + k) = *(st +n);
//         *(st + n) = temp;
//         n--;
//     }  
//         printf("%s/n", st);
//         }

// p.206
// #include <stdio.h>
// int num;
// int grow();

// int main() {
    
//     printf("%d", num);
//     grow();
// }

// int grow() {
//     num = 16448000;
//     printf("%d", num);
// }

// #include <stdio.h>
// #include <stdbool.h>

// bool numTest(int n) {
//     int i =2;
//     if (n < 2) return false;
//     else if (n == 2) return true;

//     while(1)
//     {
//         if(n% i == 0) return false;
//         else if(i*i> n) break;
//         i++;
//     }
//     return true;
// }

// int main()
// {
//     int j = 0;
//     int res = 0;
//     for(j =1; j<=20; j++)
//     {
//         if(numTest(j)) res +=j;
//     }
//     printf("%d",res);

//     return 0;
// }

// #include <stdio.h>
// int hrdcopare(num1, num2);
// int main() {
//     printf("%d", hrdcopare(10,23)+ hrdcopare(35,19));
// }
// int hrdcopare(int num1, int num2){
//     if (num1> num2)
//         return num1;
//     else
//         return num2;

// }

// #include <stdio.h>
// int main() {
//     int a =12, b= 8, c =2, d=3;
//     a /= b++ - c * d;
//     printf("%d", a);
// }

// #include <stdio.h>
// #define func1 0
// #define func2 1
// int main(){
//     int num = 83;
//     if (num %2 == func1)
//         printf("HRD");
//     else if (num % 2== func2)
//         printf("KOREA");
//     else
//         printf("1644-8000");

// }

// #include <stdio.h>
// #define ArrSize 5

// void into(int arr[], int gn, int ao);
// void PrintArr(int arr[]);

// void into(int arr[], int gn, int ao){
//     arr[ao] = gn;
// }

// void PrintArr(int arr[]) {
//     int i;
//     for (i = 0; i< ArrSize; i++) {
//         printf("%d", arr[i]);
//     }
//     printf("\n");
// }
// int main(){
//     int arr[ArrSize];
//     int i, j;
//     for (i =1; i < 6; i++) {
//         for (j= 0; j < ArrSize; j++) {
//             into(arr, (j + 1) * i % 5, j);
//         }
//         PrintArr(arr);
//     }
//     return 0;
// }

#include <stdio.h>

int printBin(int a)
{
    if (a == 0| a == 1) printf("%d", a);
    else
    {
        printBin(a/2);
        printf("%d", a%2);
    }
}
int main()
{
    int x = 11;
    printBin(x);
    return 0;
}
// class ClassA {
//     int a= 10;
//     int funcAdd(int x, int y){
//         return x + y+ a;
//     }
// }
// public class Test{
//     public static void main(String[] args){
//         int x = 3,y =6, r;
//         ClassA cal =new ClassA();
//         r = cal.funcAdd(x, y);
//         System.out.print(r);
//     }
// }



// p.271
// class ClassA{
//         ClassA(){
//             System.out.print('A');
//             this.prn();
//         }
//         void prn(){
//             System.out.print('B');
//                 }
// }
// class ClassB extends ClassA {
//     ClassB(){
//         super();
//         System.out.print('D');
//         }
//         void prn(){
//         System.out.print('E');   
//         }
//         void prn(int x){
//             System.out.print(x);   
//             }
//         }
//     public class Test {
//         public static void main(String[] args){
//             int x =7;
//             ClassB cal =new ClassB();
//             cal.prn(x);
//         }
        
//     }
        
// public class Test {
//     public static void main(String[] args){
//         int arr1[] = {3,5,9,2,5,4};
//         atest at = new atest();
//         int arr2[] =at.rw(arr1);
//         at.pa(arr2);
//     }
// }
// class atest {
//     int[] rw(int[] a){
//         int len = a.length;
//         int b[] =new int[len];
//         for(int i = 0; i < len; i++)
//             b[i] = a[len -i -1];
//         return b;
//     }
//     void pa(int[] arr){
//         for(int i = 0; i < arr.length; i++){
//             System.out.print(arr[i]);
//         }
//     }
    
// }

// public class Test {
//     public static void main(String[] args) {
//         int i;
//         int num[] ={2,1,3,74,9};
//         int numb[] = new int[10];
//         for (i =0; i< num.length; i++)
//             numb[i] = num[i];
//         for
//     }
// }

// public class hrdkorea {
//     public static void main(String[] args){
//         int cnt =0;
//         int sum =0;
//         for (int i =0; i <= 7; i++)
//         {
//             if(i % 2 == 1)
//             {
//                 cnt = cnt +1;
//                 sum = sum +i;

//             }
//         }
//         System.out.printf(cnt + ", " + sum);
//     }
// }






// import java.lang.*;
// public class Main{
//     public static void main(String[] args){
//         switch ((int)Math.signum(0)) {
//             case -1:
//                 System.out.print("N");
//                 break;
//             case 0:
//                 System.out.print("P");
//                 // break;
//             case 1:
//                 System.out.print("E");
//                 // break;
            
//             default:
//                 System.out.print("Z");
//         }
//     }
// }



// class TestClass{
//     int a,b,c;
// }

// public class Main{
//     public static void  main(String[] args){
//         TestClass Myint = new TestClass();
//         Myint.a =8;
//         Myint.b =10;
//         hrd(Myint);
//         System.out.println("a = " + Myint.a);
//         System.out.println("b = " + Myint.b);
//         System.out.println("c = " + Myint.c);

//     }
//     static void hrd(TestClass Myint){
//         if(Myint.a++ >= Myint.b--)
//             Myint.c = Myint.a - Myint.b;
//         else
//             Myint.c = Myint.a + Myint.b;

//     }
// }


// class ClassA {
//     int a =1;
//     int b =1;    
// }
// class ClassB extends ClassA{
//     void testcase(){
//         System.out.println(this.a + this.b);
//     }
//     void testcase(int i){
//         System.out.println(this.a - this.b);
// }
//     void testcase(char i){
//         System.out.println(this.a * this.b);
// }
//     void testcase(float i){
//         System.out.println(this.a / this.b);
//  }
// }
// public class Main
// {
//     public static void main(String[] args){
//         int a = 10;
//         int b = 3;

//         ClassB c = new ClassB();
//         c.testcase(a/b);
//         c.testcase(c.a);
        
//         // c.testcase('4'); // char로 호출하여 testcase(char i)를 사용함
//         // c.testcase(4.0f); // float로 호출하여 testcase(float i)를 사용함
//     }
//     }
// }

// public class Main10
//  {
//     public static void main(String[] args){
//         int num1 =3, num2 =7;

//         if(++num1 < 5 || ++num2 > 5)
//         System.out.println(num1);
//     System.out.println(num2);
//     }
    
// }


// class q1{
//     private String ans;
    
//     q1(){
//         this.ans ="";
//     }
// void test(){
//         System.out.print(ans);
//     }
// <T> void test(T i){
//     this.ans += i.toString();
// }
// void test(int i){
//     this.ans += i*2;
// }
// }

// public class Main10 {
//     public static void main(String[] args){
//         q1 a = new q1();
//         a.test("abs");
//         a.test();
//         a.test(1.0);
//         a.test(2);
//     }
    
// }


// public class Main10 {

//     public static void main(String[] args)
//     {
//         int num[] ={2,1,3,7,4,9};
//         int numb[] =new int[10];
//         for (int i =0; i < num.length; i++)
//             numb[i] = num[i];
//         for (int i:numb)
//         System.out.print(i);
//     }
// }

// public class Main10 {

//     public static void main(String[] args)
//     {int ans =0;
//     for(int i= 1; i<100; i++)
// {if( i % 3 == 0)
// ans++;
// else if(i % 4 ==0)
// ans--;}
// System.out.println(ans);;
// }
// }

// import java.lang.Math;
// public class Main10 {

//     public static void main (String[] args)
//     {
//         int s, t, cnt =0;
//         int test[] = new int[5];
//         for(int i = 0; i<10; i++)
//     }
// }


public class main8{
    public static void main8(String[] args){
        String tesstr = "    LoremIpsum    ";
        int a = teststr.trim().length();
        System.out.print(a);
    }
}
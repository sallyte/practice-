// public class Example {
//     public static void main(String[] args){
//         int a[] = new int[5];
//         int i;
//         for(i = 0; i < 5; i++)
//             a[i] = i+10;
//         for (i = 0; i<5; i++)
//             System.out.printf("%4d\n", a[i]);

//     }
// }

// public class Example{
//     public static void main(String[] args){
//         int[] a = {90,100,80,70,60,50,30};
//         int hap =0;
//         float avg;
//         for (int i: a)
//             hap =hap +i;
//         avg = (float)hap /a.length;
//         System.out.printf("%4d, %4.2f" , hap ,avg);
//     }
// }

// public class Example{
//     public static void main (String[] args){
//     String str = "Infomation!";
//     int n = str.length();
//     char[]st = new char[n];
//     n--;
//     for (int k = n; k >= 0;  k--){
//         st[n-k] = str.charAt(k);
//     }
//     for (char k:st){
//         System.out.printf("%c", k);
//     }
// }
// }


// class ClassA{
//     int a= 10;
//     int funcAdd(int x, int y){
//         return x + y+ a;

// public calss Test{
//     public static void main(String[] args){
//         int x = 3,y =6, r;
//         ClassA cal =new ClassA();
//         r = cal,funcAdd(x, y);
//         System.out.print(r);
//     }
// }
//     }
// }

public class Example {

    static class AAclass {

      static int i;
      int j;       
    }
    public static void main(String[] args){
        AAclass myVal = new AAclass();
        AAclass.i = 10;
        myVal.j = 20;
        change(myVal);
        System.out.printf("i=%d, j=%d\n", AAclass.i, myVal.j);
    }
    // static void change(AAclass myVal){
    //     int temp;
    //     temp = AAclass.i;
    //     AAclass.i = myVal.j;
    //     myVal.j = temp;
    // }

    static AAclass change(AAclass myVal){
        int temp;
        temp = AAclass.i;
        AAclass.i = myVal.j;
        myVal.j = temp;
        return myVal;
    }
}
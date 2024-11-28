
// public class Test{
//     public static void main(String[] args){
//         String weeks[] = {"월요일","화요일","수요일","목요일","금요일","토요일","일요일"};

//     int cnt = 1;
//     for (int i =1; i < 7; i++){
//         if(i%3 == 0)
//           break;
//         cnt++;
//     }
//     System.out.print("오늘은 " + weeks[cnt]);
//     }
// }

// public class Test{
//     public static void main(String[] args){
//         int arr[] ={0,1,2,3};
//         for (int num:arr)
//             System.out.println(num);
//     }
// }


// public class Test{
//     public static void main(String[] args){
//         int arr1[] = {3,5,9,2,5,4};
//         atest at  = new atest();
//         int arr2[] = at.rw(arr1);
//         at.pa(arr2);
//     }
// }
// class atest{
//     int[] rw(int[] a){
//         int len =a.length;
//         int b[] = new int[len];
//         for(int i =0; i< len; i++)
//              b[i] =a[len -i -1];
//         return b;
//     }
// void pa(int[] arr){
//     for(int i =0; i< arr.length; i++){
//         System.out.print(arr[i]);
//     }
// }
// }

// public class Test {
//     static int cycle(int[] arr, int i){
//         if(i <= 0) return 0;
//         return arr[i] %3 + cycle(arr, i -1);
//     }
// public static void main(String[] args){
//     int[] arr = {5,4,3,2,1};
//     System.out.print(cycle(arr, 4));
    
// }
// }


// public class Test {
//   public static void main(String[] args) {
//     Otest ot = new Otest();
//     ot.cat();
//     ot.cat("4");
//   }
//   }
// class Otest{
//     void cat(){
//         System.out.print("1234");
//     }
//     void cat(int c){
//         System.out.print(++c);   
//     }
//     void cat(String c){
//         System.out.print("문자");   
//     }
// }


// public class Test {
//     public static void main(String[] args){
//         String str ="HRDK" + 40 + 23;
//         System.out.println(str);
//     }
// }
 
// public class Test {
//     public static void main(String[] args){
//         char num = 0x06;
//         System.out.printf("%05O", num << 2);
//     }
// }

// public class Test {
//     public static void main(String[] args){
//     StringBuffer sb = new StringBuffer();
//     sb.append( "KOREA");
//     sb.insert(3, "HRD");
//     //     System.out.print(sb.toString());    
// }}

// public class Test {
//     public static void main(String[] args) {
//         String str ="*ulsan*";
//         int n = str.length();
//         char[] st = new char[n];
//         n--;
//         for (int k =n; k >=0; k--)
//             st[n-k] = str.charAt(k);
//         for (char k:st)
//             System.out.printf("%c", k);
//     }
// }


// public class Test {
//     public static void main (String[] args){
//         String str1 = "HELloWorLD!";
//         String str2 = "heLLOwORld!";

//         if(str1.epuals(str2))
//             System.out.print(str1.toUpperCase());
//         else if(str1.epualsIgnoreCase(str2));
//             System.out.print(str2.toLorCase());

//     }

// }

// public class Test3 {
//     public static void main(String[] args){
//         String str = "1,2,3,4,,,5,6,7,,8,9";
//         String[] splittest = str.split(",");

//         for(int i =0; i<splittest.length; i++)
//         {
//             System.out.print(splittest[i]);
//             if((i+1) % 3 ==0)
//             System.out.println();
//         }
//     }
// }



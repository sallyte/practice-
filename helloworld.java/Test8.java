// public class Test8 {
//     public static void main(String[] args){
//         String str = "1,2,3,4,,,5,6,7,,8,9";
//         String[] splittest = str.split(",,");

//         for(int i =0; i<splittest.length; i++)
//         {
//             System.out.print(splittest[i]);
//             if((i+1) % 3 ==0)
//             System.out.println();
//         }
//     }
// }


// public class Test8 {
//     public static void main(String[] args){
//         String str = "HELLO!@#WORLD/-";
//         String res = str.replaceAll("[^ㄱ-하-ㅣ가-힣a-zA-Z0-9,.]","*");
//         System.out.print(res);
//     }
// }


// 

import java.math.*;

public class Test8 {
    public static void main(String[] args){
        BigInteger n = new BigInteger("12345");
        BigInteger m = new BigInteger("54321");
        System.out.print(n.compareTo(m));

    }
}
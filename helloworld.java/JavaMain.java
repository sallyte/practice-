interface Cals {
    public void set(int v);  
}

interface Coms {
    public void get(int v);  
}

class Test implements Cals,Coms {
    public void get(int v) {
        System.out.print(v*v);
            }
        
    public void set(int v) {
        System.out.print(v/v);
    }}
public class JavaMain {
    public static void main(String[] args){
        Test a = new Test();

        a.get(10);
        a.set(10);
    }
    }
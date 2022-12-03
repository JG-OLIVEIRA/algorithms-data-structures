import java.util.Scanner;

public class Fibonacci {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Please enter the number of month:");
        int number = sc.nextInt();

        for(int i = 1; i <= number; i++){
            System.out.println(i + " month: " + fibonacci(i));
        }
    }

    public static int fibonacci(int n){
        if(n == 1 || n == 2){
            return 1;
        } else {
            return fibonacci(n - 1) + fibonacci(n - 2);
        }
    }
}
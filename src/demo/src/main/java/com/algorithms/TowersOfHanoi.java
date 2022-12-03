package com.algorithms;

import java.util.Scanner;

public class TowersOfHanoi {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Please enter the number of discs: ");
        int n = sc.nextInt();
        hanoi(n, 'A', 'B', 'C');
    }

    public static void hanoi(int n, char A, char B, char C) {
        if(n == 1){
            System.out.println("Move " + n + " " + A + " to " + C);
        } else {
            hanoi(n - 1, A, C, B);
            System.out.println("Move " + n + " from " + A + " to " + C);
            hanoi(n - 1, B, A, C);
        }
    }
}

package exercises;

import java.util.Scanner;

import static java.lang.System.*;;

/*
 * Program to calculate sum and average for non-negative integers
 *
 * See:
 * - Loops (while only)
 * - LoopAndAHalf
 *
 */
public class Ex3SumAvg {

    public static void main(String[] args) {
        new Ex3SumAvg().program();
    }

    final Scanner sc = new Scanner(in);
    int sum;
    int times = 0;
    int input;


    void program() {
        // Write your code here

        // -- Input (and bookkeeping)
        while(input >-1)
        {
            sum = sum + input;
            times = times + 1;
            input = sc.nextInt();
        }

        // -- Process---
        float avg = sum / (times - 1);


        // -- Output ----
        System.out.println("sum: " + sum);
        System.out.println("avg: " + avg);

    }

}

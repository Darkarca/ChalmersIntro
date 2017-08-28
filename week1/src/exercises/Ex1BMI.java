package exercises;

import java.util.Scanner;
import java.lang.Math;

import static java.lang.System.in;
import static java.lang.System.out;

/*
 * (this is a multi row comment, no impact on program)
 *
 * Program to calculate a persons BMI
 * See https://en.wikipedia.org/wiki/Body_mass_index
 *
 * Formula is: bmi = weight / height²     (kg/m²)
 *
 * See:
 * - F2C
 * - PrimitiveVariables
 * - IO
 * - Arithmetic
 */
public class Ex1BMI {

    // Don't care about this, must be there, start coding at program
    public static void main(String[] args) {
        new Ex1BMI().program();
    }

    // This connects our program to the keyboard
    final Scanner sc = new Scanner(in);
    int weight;
    float height;

    void program() {
        // Write your code here


        // --- Input ---------
        System.out.println("Please, enter your weight (kg)");
        weight = sc.nextInt();
        System.out.println("Please, enter your height (m)");
        height = sc.nextFloat();
        // --- Process --------
        //lol no

        // --- Output ---------
        System.out.println("BMI = " + weight / (java.lang.Math.pow(height, 2)));
    }

}

package exercises;

import java.util.*;

import static java.lang.System.in;
import static java.lang.System.out;

/*
 * Applying "smallest step tactics" to Rock, paper, scissor game.
 * See https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors
 *
 * Rules:
 *
 *       -----------  Beats -------------
 *       |                              |
 *       V                              |
 *      Rock (1) --> Scissors (2) --> Paper (3)
 *
 * See:
 * - SmallestStepNim
 */
public class Ex7SmallestStepRPS {

    public static void main(String[] args) {
        new Ex7SmallestStepRPS().program();
    }

    final Random rand = new Random();
    final Scanner sc = new Scanner(in);

    void program() {

        int maxRounds = 5;
        int human;          // Outcome for player
        int computer;       // Outcome for computer
        int result;         // Result for this round
        int round = 0;      // Number of rounds
        int total = 0;      // Final result after all rounds
        String[] choice = new String[3];                                                                                // Array of strings to make result prints cleaner
            choice[0] = "Rock";
            choice[1] = "paper";
            choice[2] = "scissor";

        out.println("Welcome to Rock, Paper and Scissors");
        // Write code for game here
   out.print("1 for Rock, 2 for Paper or 3 for Scissor? (-1 to quit) > ");                                              // Defines input rules for player
        for(int i = 0; i<maxRounds; i++) {                                                                              // Restarts round until maxRounds have been played
            try {                                                                                                       // Try for errors
                human = sc.nextInt();
                sc.nextLine();                                                                                          // sc.nextInt doesn't remove the /n at the end so another sc.nextLine is needed to skip it

                computer = computerRoll();                                                                              // Calls the method for computer roll
                result = computer - human;                                                                              // Calculates the winner
                if (human == -1) {
                    break;
                }
                if (human > 3 || human < -1) {                                                                          // Checks if player choice is within rules
                    out.println("Please only choose numbers 1, 2 or 3!");
                    i--;                                                                                                // Restarts current round if player chose an illegal move
                }
                if (result % 2 == 0) {                                                                                  // Calculation needed to determine winner easier
                    result = result * (-1);                                                                             // Calculation needed to determine winner easier
                }
                if (result == 0) {                                                                                      // If both human and computer chose the same number then result = 0
                    out.println("Computer also chose " + choice[computer - 1] + " so it is a draw!");
                } else if (result > 0) {
                    out.println("Unfortunate! Computer chose " + choice[computer - 1] + " so the computer wins!");
                    total--;
                } else if (result < 0) {
                    out.println("Congratulations! Computer chose " + choice[computer - 1] + " so you win!");
                    total++;
                }
                if (i < maxRounds - 1) {                                                                                // Asks human to play again if there is atleast one more round to play
                    out.print("Go ahead and try again! > ");
                }
            } catch (Exception e) {                                                                                     // Catch error and ask for new inpout
                out.print("Please only enter numbers!");
                i--;
                sc.next();
            }
        }
        out.println("Game over! ");
        if ( total == 0 ) {
            out.println("Draw");
        } else if ( total > 0 ) {
            out.println("Human won.");
        } else {
            out.println("Computer won.");
        }


    }
    int computerRoll(){                                                                                                     // Rolls a die
        return rand.nextInt(3) + 1;                                                                                  // Returns a random number between 1 and 6
    }
}

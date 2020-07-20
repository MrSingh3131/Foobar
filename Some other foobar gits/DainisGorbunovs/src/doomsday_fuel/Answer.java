package doomsday_fuel;

import java.util.LinkedList;
import java.util.List;

/*
    Helpful information:
        https://en.wikipedia.org/wiki/Absorbing_Markov_chain
        https://github.com/ivanseed/google-foobar-help/blob/master/challenges/doomsday_fuel/doomsday_fuel.md

    Reusing functions of other people as in real world this challenge is solved using libraries.
    Also no need to reinvent the wheel.
 */
public class Answer {
    /**
     * Adapted from Jeffrey Hantin's code
     * http://stackoverflow.com/questions/4201860/how-to-find-gcd-lcm-on-a-set-of-numbers
     * @param a First number
     * @param b Second number
     * @return Least Common Multiple between two numbers
     */
    private static int leastCommonMultiple(int a, int b)
    {
        return a * (b / greatestCommonDivisor(a, b));
    }

    /**
     * Adapted from Jeffrey Hantin's code
     * http://stackoverflow.com/questions/4201860/how-to-find-gcd-lcm-on-a-set-of-numbers
     * @param input Numbers
     * @return Least Common Multiple between all numbers
     */
    static int leastCommonMultiple(int[] input)
    {
        int result = input[0];
        for (int i = 1; i < input.length; i++)
            result = leastCommonMultiple(result, input[i]);
        return result;
    }

    /**
     * Finds greatest common divisor between numbers
     * @param a First number
     * @param b Second number
     * @return Greatest Common Divisor of these numbers
     */
    private static int greatestCommonDivisor(int a, int b) {
        if (b==0)
            return a;

        return greatestCommonDivisor(b, a%b);
    }

    /**
     * @param decimals Decimal numbers
     * @return an int array of fraction denominators
     */
    static int[] getFractionDenominators(double[] decimals) {
        int[] denominators = new int[decimals.length];

        for (int index = 0; index < decimals.length; ++index) {
            denominators[index] = getFractionDenominator(decimals[index]);
        }

        return denominators;
    }

    /**
     * Max limit for denominator is 1'000'000
     * @param decimal Decimal number
     * @return Denominator
     */
    static int getFractionDenominator(double decimal) {
        return getFractionDenominator(decimal, 1000000);
    }

    /**
     * Adapted from Peter Lawrey's, Christopher Guray's code
     * http://stackoverflow.com/questions/5968636/converting-a-float-into-a-string-fraction-representation
     * @param d Decimal number
     * @param factor Maximum denominator
     * @return Denominator
     */
    private static int getFractionDenominator(double d, int factor) {
        if (d < 0) {
            d = -d;
        }
        long l = (long) d;
        d -= l;
        double error = Math.abs(d);
        int bestDenominator = 1;
        for(int i=2;i<=factor;i++) {
            double error2 = Math.abs(d - (double) Math.round(d * i) / i);
            if (error2 < error) {
                error = error2;
                bestDenominator = i;
                if (error2 == 0) break;
            }
        }
        return bestDenominator;
    }

    /**
     * Code by Manish Bhojasia
     * http://www.sanfoundry.com/java-program-find-inverse-matrix/
     * @param a Array (matrix) of double values
     * @return Inverse of the array (matrix)
     */
    static double[][] invert(double a[][])
    {
        int n = a.length;
        double x[][] = new double[n][n];
        double b[][] = new double[n][n];
        int index[] = new int[n];
        for (int i=0; i<n; ++i)
            b[i][i] = 1;

        // Transform the matrix into an upper triangle
        gaussian(a, index);

        // Update the matrix b[i][j] with the ratios stored
        for (int i=0; i<n-1; ++i)
            for (int j=i+1; j<n; ++j)
                for (int k=0; k<n; ++k)
                    b[index[j]][k]
                            -= a[index[j]][i]*b[index[i]][k];

        // Perform backward substitutions
        for (int i=0; i<n; ++i)
        {
            x[n-1][i] = b[index[n-1]][i]/a[index[n-1]][n-1];
            for (int j=n-2; j>=0; --j)
            {
                x[j][i] = b[index[j]][i];
                for (int k=j+1; k<n; ++k)
                {
                    x[j][i] -= a[index[j]][k]*x[k][i];
                }
                x[j][i] /= a[index[j]][j];
            }
        }
        return x;
    }

    /**
     * Code by Manish Bhojasia
     * http://www.sanfoundry.com/java-program-find-inverse-matrix/
     *
     * Method to carry out the partial-pivoting Gaussian
     * elimination.  Here index[] stores pivoting order.
     * @param a Array (matrix) of double values
     * @param index Pivoting order
     */
    private static void gaussian(double a[][], int index[])
    {
        int n = index.length;
        double c[] = new double[n];

        // Initialize the index
        for (int i=0; i<n; ++i)
            index[i] = i;

        // Find the rescaling factors, one from each row
        for (int i=0; i<n; ++i)
        {
            double c1 = 0;
            for (int j=0; j<n; ++j)
            {
                double c0 = Math.abs(a[i][j]);
                if (c0 > c1) c1 = c0;
            }
            c[i] = c1;
        }

        // Search the pivoting element from each column
        int k = 0;
        for (int j=0; j<n-1; ++j)
        {
            double pi1 = 0;
            for (int i=j; i<n; ++i)
            {
                double pi0 = Math.abs(a[index[i]][j]);
                pi0 /= c[index[i]];
                if (pi0 > pi1)
                {
                    pi1 = pi0;
                    k = i;
                }
            }

            // Interchange rows according to the pivoting order
            int itmp = index[j];
            index[j] = index[k];
            index[k] = itmp;
            for (int i=j+1; i<n; ++i)
            {
                double pj = a[index[i]][j]/a[index[j]][j];

                // Record pivoting ratios below the diagonal
                a[index[i]][j] = pj;

                // Modify other elements accordingly
                for (int l=j+1; l<n; ++l)
                    a[index[i]][l] -= pj*a[index[j]][l];
            }
        }
    }

    /**
     * Find transition and terminal nodes in matrix
     * @param matrix Matrix array
     * @return In TERMINAL_NODE - terminal nodes, in TRANSITION_NODE - transition nodes
     */
    static final int TERMINAL_NODE = 0;
    static final int TRANSITION_NODE = 1;
    static int[][] separateTransitionTerminalNodes(int[][] matrix) {
        List<Integer> terminalNodesList = new LinkedList<>();
        List<Integer> transitionNodesList = new LinkedList<>();

        int i = 0;
        for (int[] row : matrix) {
            boolean terminal = true;
            for (int column : row) {
                if (column != 0) {
                    terminal = false;
                    break;
                }
            }
            if (terminal) {
                terminalNodesList.add(i);
            } else {
                transitionNodesList.add(i);
            }
            i++;
        }

        int[][] separated = new int[2][];
        separated[TERMINAL_NODE] = new int[terminalNodesList.size()];
        separated[TRANSITION_NODE] = new int[transitionNodesList.size()];

        i = 0;
        for (int value : terminalNodesList)
            separated[TERMINAL_NODE][i++] = value;

        i = 0;
        for (int value : transitionNodesList)
            separated[TRANSITION_NODE][i++] = value;

        return separated;
    }

    /**
     * Finds the probability of reaching a node via a certain node
     * @param m Matrix
     * @param fromNode Transitioning from node
     * @param toNode Transitioning to node
     * @return Probability of reaching the node
     */
    static double getTransitionProbability(int[][] m, int fromNode, int toNode) {
        int count = 0;
        for (int times : m[fromNode]) {
            count += times;
        }
        return (double) m[fromNode][toNode] / count;
    }

    /**
     * Returns Q matrix (probabilities of transitioning from transient state to another)
     * @param matrix Matrix array
     * @param nodes Transition nodes
     * @return Q matrix
     */
    static double[][] getTransitionProbabilities(int[][] matrix, int[] nodes) {
        double[][] probabilities = new double[nodes.length][nodes.length];

        int nodeIndex = 0;
        for (int node : nodes) {
            int toIndex = 0;
            for (int toNode : nodes) {
                probabilities[nodeIndex][toIndex] = getTransitionProbability(matrix, node, toNode);
                ++toIndex;
            }
            ++nodeIndex;
        }

        return probabilities;
    }

    /**
     * Get reaching probabilities
     * @param F Transitioning probabilities
     * @return F matrix
     */
    static double[][] getReachingProbabilities(double[][] F) {
        double[][] identitySubtractF = new double[F.length][F.length];

        for (int row = 0; row < F.length; ++row) {
            for (int column = 0; column < F.length; ++column) {
                identitySubtractF[row][column] = -F[row][column];

                // Add identity matrix
                if (row == column) {
                    ++identitySubtractF[row][column];
                }
            }
        }

        return invert(identitySubtractF);
//        return identitySubtractF;
    }

    /**
     * Get absorbing probabilities
     * @param matrix Matrix array
     * @param transitionNodes Nodes which transition
     * @param terminalNodes Nodes which terminate
     * @return R matrix
     */
    static double[][] getAbsorbingProbabilities(int[][] matrix, int[] transitionNodes,
                                                int[] terminalNodes) {
        double[][] probabilities = new double[transitionNodes.length][terminalNodes.length];
        int nodeIndex = 0;
        for (int transitionNode : transitionNodes) {
            int toIndex = 0;
            for (int terminalNode : terminalNodes) {
                probabilities[nodeIndex][toIndex] = getTransitionProbability(matrix, transitionNode, terminalNode);
                ++toIndex;
            }
            ++nodeIndex;
        }
        return probabilities;
    }

    /**
     * Multiplies a matrix with another matrix
     * @param first Matrix with double values
     * @param second Matrix with double values
     * @return Product of both matrices
     */
    static double[][] multiplyMatrix(double[][] first, double[][] second) {
        double[][] result = new double[first.length][second[0].length];

        for (int i = 0; i < first.length; ++i) {
            for (int j = 0; j < second[0].length; ++j) {
                for (int k = 0; k < first[0].length; ++k) {
                    result[i][j] += first[i][k] * second[k][j];
                }
            }
        }

        return result;
    }

    /**
     * Finds the probabilities of reaching terminal states.
     * Probabilities are in fractions, e.g. 1/7 probability.
     *
     * @param m Input matrix of ore form states
     * @return Fractional probabilities of reaching terminal states
     */
    public static int[] answer(int[][] m) {
        // If matrix is 1x1, then probability is 100%
        if (m.length == 1) {
            return new int[]{1, 1};
        }

        // Find transitional and terminal nodes
        int[][] nodeTypes = separateTransitionTerminalNodes(m);

        // Q: probability of transitioning from some transient state to another
        double[][] Q = getTransitionProbabilities(m, nodeTypes[TRANSITION_NODE]);
        // R: probability of transitioning from some transient state to some absorbing state.
        double[][] R = getAbsorbingProbabilities(m, nodeTypes[TRANSITION_NODE], nodeTypes[TERMINAL_NODE]);

        // F = (I-Q)^-1, the expected probabilities reaching transient states from transient states
        double[][] F = getReachingProbabilities(Q);

        // FR = (I-Q)^-1 * R, probabilities of reaching the terminal states
        double[][] FR = multiplyMatrix(F, R);

        // Create the answer
        int[] answer = new int[FR[0].length + 1];

        // Last number is the least common denominator
        int leastCommonDenominator = Answer.leastCommonMultiple(Answer.getFractionDenominators(FR[0]));
        answer[FR[0].length] = leastCommonDenominator;

        // Other numbers must be multiplied by it and rounded to the nearest integer
        for (int index = 0; index < FR[0].length; ++index) {
            answer[index] = (int) Math.round(FR[0][index]*leastCommonDenominator);
        }

        return answer;
    }
}
/*
    Minion's bored game
    ===================

    There you have it. Yet another pointless "bored" game created by the bored minions of Professor Boolean.

    The game is a single player game, played on a board with n squares in a horizontal row. The minion places a token
    on the left-most square and rolls a special three-sided die.

    If the die rolls a "Left", the minion moves the token to a square one space to the left of where it is currently.
    If there is no square to the left, the game is invalid, and you start again.

    If the die rolls a "Stay", the token stays where it is.

    If the die rolls a "Right", the minion moves the token to a square, one space to the right of where it is currently.
    If there is no square to the right, the game is invalid and you start again.

    The aim is to roll the dice exactly t times, and be at the rightmost square on the last roll. If you land on the
    rightmost square before t rolls are done then the only valid dice roll is to roll a "Stay". If you roll anything
    else, the game is invalid (i.e., you cannot move left or right from the rightmost square).

    To make it more interesting, the minions have leaderboards (one for each n,t pair) where each minion submits the
    game he just played: the sequence of dice rolls. If some minion has already submitted the exact same sequence,
    they cannot submit a new entry, so the entries in the leader-board correspond to unique games playable.

    Since the minions refresh the leaderboards frequently on their mobile devices, as an infiltrating hacker,
    you are interested in knowing the maximum possible size a leaderboard can have.

    Write a function answer(t, n), which given the number of dice rolls t, and the number of squares in the board n,
    returns the possible number of unique games modulo 123454321. i.e. if the total number is S, then return the
    remainder upon dividing S by 123454321, the remainder should be an integer between 0 and 123454320 (inclusive).

    n and t will be positive integers, no more than 1000. n will be at least 2.
 */
package minions_bored_game;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Answer {
    // Memoize counts
    static Map<List<Integer>, Integer> countMemo = new HashMap<List<Integer>, Integer>();

    // Returns max leaderboard size
    public static int count(int t, int n, int position) {
        // If at the last square, can only stay
        if (position == n-1) {
            return 1;
        }
        // Cannot go behind leftest or rightest squares
        // t == n-1 is min
        if (position < 0 || position >= n || t < n-position-1) {
            return 0;
        }

        // If memoized, return the cached value
        List<Integer> key = Arrays.asList(t, n, position);
        if (countMemo.containsKey(key))
            return countMemo.get(key);

        // Else, start counting
        int count = 0;
        count += count(t-1, n, position-1); // go left
        count += count(t-1, n, position);   // stay
        count += count(t-1, n, position+1); // go right
        count %= 123454321;

        // Memoize the count
        countMemo.put(key, count);
        return count;
    }

    public static int answer(int t, int n) {
        return count(t, n, 0);
    }

    public static void main(String[] args) {
        System.out.println("1 ?= " + answer(1,2)+"\n");
        System.out.println("2 ?= " + answer(2,2));
        System.out.println("3 ?= " + answer(3,2)+"\n");
        System.out.println("7 ?= " + answer(4,3)+"\n");
        System.out.println("862 ?= " + answer(10,6)+"\n");
    }
}
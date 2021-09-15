/**
 *
 */

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.stream.IntStream;

public class Recursion {

  /**
   * Recursive function that finds the index of s2 in s1.
   *
   * @param s1
   * @param s2
   * @return Returns the index of the first time that
   * 			s2 appears in s1 or -1 if s2 is not contained
   * 			in s1.
   */
  public static int indexOf(String s1, String s2) {
    // DEV:
    // String cur = s2.length() <= s1.length() ? s1.substring(0, s2.length()) : "";
    // System.out.println(cur);
    return s2.length() > s1.length()
      ? -1
      : s1.substring(0, s2.length()).equals(s2)
        ? 0
        : indexOf(s1.substring(1), s2) == -1
          ? -1
          : 1 + indexOf(s1.substring(1), s2);
  }
	
  // @Test
	// public void testIndexOf_test1() {
  //       int result1 = Recursion.indexOf("Hello", "World");
  //       System.out.println("indexOf(Hello, World), got " + result1);
  //       assertEquals(-1, result1);
	// }

  /**
   * Write a recursive function that removes the first k even numbers
   * from the stack. If there are less than k even elements in the stack,
   * just remove all even elements. Do not use any loops or data structures
   * other than the stack passed in as a parameter.
   * @param stack
   * @param k
   * @return Returns the number of elements removed from the stack.
   */
  public static int removeEvenNumbers(Stack<Integer> stack, int k) {
    // DEV:
    // System.out.println(k);
    // System.out.println(stack);

    if (k == 0) {
      return 0;
    }

    if (stack.get(removeEvenNumbers(stack, k - 1)) % 2 == 0) {
      stack.remove(removeEvenNumbers(stack, k - 1));
    }
    return 1 + removeEvenNumbers(stack, k - 1);
  }

  /**
   * Write a recursive function that accepts an integer and
   * returns a new number containing only the even digits, in the same
   * order. If there are no even digits, return 0. Your function should
   * work for positive or negative numbers. You are NOT allowed
   * to use any data structures. You are not allowed to use Strings to
   * solve this problem either.
   * @param n
   * @return The input with only the even digits remaining in the same
   * order.
   */
  public static int evenDigits(int n) {
    if (n == 0) {
      return n;
    }

    int dig = n % 10;
    int carry = evenDigits(Integer.valueOf(n / 10));

    if (dig % 2 == 0) {
      carry *= 10;
      carry += dig;
    }

    return carry;
  }

  /**
   * Write a recursive function that evaluates a Queue<Character> as a mathematical
   * expression. This queue can have any of the following characters:
   * { '(', ')', '+', '*'} or any single digit number. Evaluate this expression and
   * return the result. For example, for the expression:
   * "(((1+2)*(3+1))+(1*(2+2)))", each of these characters would be in the
   * q. As you recursively evaluate characters from the expression, you will
   * remove the characters from the q. After evaluating the above expression,
   * you should return 16. You are guaranteed that there are NO two digit numbers,
   * and that the expression is well formed (parenthesis match, etc...). Do not use any
   * loops. Do not use any data structures besides the q passed in as a parameter.
   * @param q
   * @return The result of the mathematical expression.
   */
  public static int evaluate(Queue<Character> q) {
    int first;
    if (q.peek() == '(') {
      q.poll();
      first = evaluate(q);
      q.poll();
    } else {
      first = Character.getNumericValue(q.poll());
    }
    Character operator = q.poll();

    if (q.isEmpty()) {
      return first;
    }

    System.out.println("first");
    System.out.println(first);

    int second;
    if (q.peek() == '(') {
      q.poll();
      second = evaluate(q);
      q.poll();
    } else {
      second = Character.getNumericValue(q.poll());
    }
    System.out.println("second");
    System.out.println(second);
    if (q.isEmpty()) {
      return first;
    }

    return operator == '+' ? first + second : first * second;
  }

  /**
   * Write a recursive function that accepts a stack of integers and
   * replaces each int with two copies of that integer. For example,
   * calling repeatStack and passing in a stack of { 1, 2, 3} would change
   * the stack to hold { 1, 1, 2, 2, 3, 3}. Do not use any loops. Do not use
   * any data structures other than the stack passed in as a parameter.
   * @param stack
   */
  public static void repeatStack(Stack<Integer> stack) {

    if ( !stack.empty()) {
      
      int first = stack.pop();
      
      repeatStack(stack);
      
      stack.push(first);
      stack.push(first);
    }

  }

  /**
   * Write a recursive function that accepts a Queue<Integer>. It
   * should change every int in this queue to be double its original
   * value. You may NOT use loops or any other data structures besides
   * the queue passed in as a parameter. You may use a helper function.
   * @param q
   */
  public static void doubleElements(Queue<Integer> q) {
    dblQueue(q, 2);
    dblQueue(q, 1);
  }
  
  public static void dblQueue(Queue<Integer> q, int modifier) {
    if ( !q.isEmpty()) {
      int cur = q.poll();
      dblQueue(q, modifier);
      q.add(cur * modifier);
    }

  }


  public static void main(String[] args) {
    // 1 - test
    // System.out.println(indexOf(args[0], args[1]));
    // 2- test
    // Stack<Integer> te = new Stack<Integer>();
    // IntStream.range(4, 20).forEachOrdered(n -> te.push(n));
    // System.out.println(removeEvenNumbers(te, 5));
    // 3 - test
    // System.out.println(evenDigits(Integer.parseInt(args[0])));
    // 4 - test
    // String mathExpression = "(((1+2)*(3+1))+(1*(2+2)))";
    // // String mathExpression = "(1+2)+3";

    // Queue<Character> test = new LinkedList<Character>();

    // for (int i = 0; i < mathExpression.length(); i++) {
    //   test.add(mathExpression.charAt(i));
    // }
    // System.out.println(evaluate(test));

    // 5 - test

    // Stack<Integer> test = new Stack<Integer>();
    // for ( int i = 0; i < 10; i++ ) {
    //   test.push(i);
    // }
    // repeatStack(test);
    // System.out.println(test);
    
    // 6 - test

    Queue<Integer> test = new LinkedList<Integer>();
    for ( int i = 0; i < 10; i++ ) {
      test.add(i);
    }
    doubleElements(test);
    System.out.println(test);
  }
}

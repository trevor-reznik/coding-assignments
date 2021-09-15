/**
 * Wordsearch Program
 * PA1 | CSC210 | Fall 21
 * <p>
 * Parse text and dictionary files from stdin path params.
 * Search for matches going up/dowm back/forward. Print all
 * matches in sorted order to stdout.
 * <p>
 * Usage:
 *  <code>java WordSearch.java dictionary puzzle</code>
 * <p>
 * Example:
 *  <code>java WordSearch.java myDict.txt myPuzzle.txt</code>
 * <p>
 * <b>Dictionary File</b> should be a text file of words delimited by newline
 * characters.
 * <b>Puzzle File</b> should be a text file containing rows
 * delimited by newline characters.
 *
 * @author Christian P. Byrne
 *
 *
 */

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.TreeMap;
import java.util.stream.Collectors;

public class WordSearch {

  /**
   * Read and parse file. Remove whitespaces, lowercase all letters,
   * and filter based on character length. Array because primarily
   * doing lookups on data.
   *
   * @param path          Path to file.
   * @param minLength     Exclude lines with fewer letters than this.
   * @return              Array of parsed and filtered lines.
   * @throws              java.io.IOException
   */
  public static String[] parseFile(String path, Integer minLength)
    throws java.io.IOException {
    return Files
      .readAllLines(Paths.get(path))
      .stream()
      .filter(word -> word.length() >= minLength)
      .map(word -> word.replace(" ", "").toLowerCase())
      .collect(Collectors.toList())
      .toArray(new String[0]);
  }

  /**
   * Return a rotated (90-degree counter clockwise) version of puzzle to
   * allow for vertical searches with contains() method.
   *
   * @param puzzle      Puzzle (array of strings which represent rows).
   * @param dimensions  {character width, chracter height} of puzzle grid.
   * @return            Rotated 2D puzzle grid.
   */
  public static String[] rotatePuzzle(String[] puzzle, Integer[] dimensions) {
    List<String> ret = new LinkedList<String>();
    for (int column = 0; column < dimensions[0]; column++) {
      // Create linked list for each column (because only appending).
      List<Character> columnChars = new LinkedList<Character>();
      for (int row = 0; row < dimensions[1]; row++) {
        columnChars.add(puzzle[row].charAt(column));
      }
      // Reduce column to string and append to rotated puzzle (it's now a row).
      ret.add(
        columnChars.stream().map(String::valueOf).collect(Collectors.joining())
      );
    }
    return ret.toArray(new String[0]);
  }

  /**
   * Search puzzle for word and append any matches to treemap accumulator
   * with key representing index of starting letter.
   *
   * @param puzzle    Puzzle (array of strings which represent rows).
   * @param word      Target word to search for.
   * @param hits      Accumulation of matches so far.
   * @param reversed  Whether searching backwards or not.
   */
  public static void search(
    String[] puzzle,
    String word,
    TreeMap<Integer, ArrayList<String>> hits,
    Boolean reversed
  ) {
    Integer width = puzzle[0].length();
    for (int i = 0; i < puzzle.length; i++) {
      String curRow = puzzle[i];
      if (curRow.contains(word)) {
        // Create key that indicates row AND column position of 1st letter.
        Integer startPos = curRow.indexOf(word) + (i * width);
        if (reversed) {
          startPos =
            (width - curRow.indexOf(word) - word.length() + i * width);
          word = new StringBuilder(word).reverse().toString();
        }
        // If multiple matches start at same letter (nested matches).
        if (hits.keySet().contains(startPos)) {
          hits.get(startPos).add(word);
        } else {
          hits.put(startPos, new ArrayList<>(Arrays.asList(word)));
        }
      }
    }
  }

  /**
   * Print matches. Words that start at same index (nested matches) are 
   * sorted based on character length before printing. Matches are in
   * 4 array lists representing L>R, R>L
   *
   * @param hits   Matches/hits accumulator.
   */
  public static void printPuzzle(
    List<TreeMap<Integer, ArrayList<String>>> hits
  ) {
    hits.forEach(
      hitType ->
        hitType
          .values()
          .forEach(
            startIndex -> {
              startIndex.sort((Comparator.comparing(String::length)));
              startIndex.forEach(hit -> System.out.println(hit));
            }
          )
    );
  }

  public static void main(String[] args) throws java.io.IOException {
    String[] dictionary = parseFile(args[0], 3);
    String[] puzzle = parseFile(args[1], 1);
    Integer[] dimensions = {
      Integer.parseInt(puzzle[1]),
      Integer.parseInt(puzzle[0]),
    };
    puzzle = Arrays.copyOfRange(puzzle, 2, puzzle.length);
    String[] rotatedPuzzle = rotatePuzzle(puzzle, dimensions);

    // Find then print matches.
    List<TreeMap<Integer, ArrayList<String>>> ret = new ArrayList<>(4);
    for (int i = 0; i < 4; i++) {
      ret.add(new TreeMap<Integer, ArrayList<String>>());
    }
    for (String word : dictionary) {
      String reversed = new StringBuilder(word).reverse().toString();
      search(puzzle, word, ret.get(0), false);
      search(puzzle, reversed, ret.get(1), true);
      search(rotatedPuzzle, word, ret.get(2), false);
      search(rotatedPuzzle, reversed, ret.get(3), true);
    }
    printPuzzle(ret);
  }
}

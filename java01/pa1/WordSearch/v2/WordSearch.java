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
   * and filter based on character length.
   *
   * @param path          Path to file.
   * @param minLength     Exclude lines with fewer letters than this.
   * @return              List of parsed and filtered lines.
   * @throws              java.io.IOException
   */
  public static List<String> parseFile(String path, Integer minLength)
    throws java.io.IOException {
    return Files
      .readAllLines(Paths.get(path))
      .stream()
      .filter(word -> word.length() >= minLength)
      .map(word -> word.replace(" ", "").toLowerCase())
      .collect(Collectors.toList());
  }

  /**
   * Return a rotated (90-degree counter clockwise) version of puzzle to allow 
   * for vertical searches with contains() methhod. Convert to fastest data 
   * type depending on operation.
   *
   * @param puzzle      2D Puzzle grid.
   * @param dimensions  {character width, chracter height} of puzzle grid.
   * @return            Rotated 2D puzzle grid.
   */
  public static List<String> rotatePuzzle(
    List<String> puzzle,
    Integer[] dimensions
  ) {
    // Convert original puzzle to array (because only doing lookups).
    String[] arrPuzzle = puzzle.toArray(new String[0]);
    List<String> ret = new LinkedList<String>();
    for (int column = 0; column < dimensions[0]; column++) {
      // Create linked list for each column (because only appending).
      List<Character> columnChars = new LinkedList<Character>();
      for (int row = 0; row < dimensions[1]; row++) {
        columnChars.add(arrPuzzle[row].charAt(column));
      }
      // Reduce column to string and append to rotated puzzle (it's now a row).
      ret.add(
        columnChars.stream().map(String::valueOf).collect(Collectors.joining())
      );
    }
    return ret;
  }

  /**
   * Search provided puzzle grid for word and append any matches to hit tree map.
   *
   * @param puzzle    2D Puzzle grid.
   * @param word      Target word.
   * @param hits      Collection of matches so far.
   * @param width     Character width of puzzle grid.
   * @param reversed  Whether searching backwards or not.
   *
   */
  public static void search(
    List<String> puzzle,
    String word,
    TreeMap<Integer, ArrayList<String>> hits,
    Boolean reversed
  ) {
    Integer width = puzzle.get(0).length();
    for (int i = 0; i < puzzle.size(); i++) {
      String candidate = puzzle.get(i);
      if (candidate.contains(word)) {
        Integer priority = candidate.indexOf(word) + (i * width);
        if (reversed) {
          priority =
            (width - candidate.indexOf(word) - word.length() + i * width);
          word = new StringBuilder(word).reverse().toString();
        }
        if (hits.keySet().contains(priority)) {
          hits.get(priority).add(word);
        } else {
          hits.put(priority, new ArrayList<>(Arrays.asList(word)));
        }
        return;
      }
    }
  }

  /**
   * Print matches. Words that start at same index (substring word
   * inside another) are sorted based on length before printing.
   *
   * @param ret   Matches/hits accumulator.
   */
  public static void printPuzzle(
    List<TreeMap<Integer, ArrayList<String>>> ret
  ) {
    ret.forEach(
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
    // Read and parse txt files.
    List<String> dictionary = parseFile(args[0], 3);
    List<String> puzzleFile = parseFile(args[1], 1);
    Integer[] dimensions = {
      Integer.parseInt(puzzleFile.get(1)),
      Integer.parseInt(puzzleFile.get(0)),
    };
    puzzleFile.subList(0, 2).clear();
    List<String> rotated = rotatePuzzle(puzzleFile, dimensions);

    // Find then print matches.
    List<TreeMap<Integer, ArrayList<String>>> ret = new ArrayList<>(4);
    for (int i = 0; i < 4; i++) {
      ret.add(new TreeMap<Integer, ArrayList<String>>());
    }
    for (String word : dictionary) {
      String reversed = new StringBuilder(word).reverse().toString();
      search(puzzleFile, word, ret.get(0), false);
      search(puzzleFile, reversed, ret.get(1), true);
      search(rotated, word, ret.get(2), false);
      search(rotated, reversed, ret.get(3), true);
    }
    printPuzzle(ret);
  }
}

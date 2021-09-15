/**
 * <h1>Wordsearch Program</h1>
 * <h5>PA1 - CSC210 - Fall 21</h5>
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
 * characters. <b> Puzzle File</b> should be a text file containing rows
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
import java.util.List;
import java.util.TreeMap;
import java.util.stream.Collectors;

public class WordSearch {

  /**
   * Read and parse file. Remove whitespaces, lowercase all letters,
   * and filter based on length.
   *
   * @param path          Path to file.
   * @param minLength     Exclude lines with fewer letters than this.
   * @return              List of parsed and filtered lines.
   * @throws              java.io.IOException
   *
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
   * Return a rotated (90 degree) version of puzzle to allow for
   * vertical searches.
   *
   * @param puzzle    2D Puzzle grid.
   * @param width     Character width of puzzle grid.
   * @param height    Character height of puzzle grid.
   * @return          Rotated 2D puzzle grid.
   *
   */
  public static ArrayList<String> flip(
    List<String> puzzle,
    Integer[] dimensions
  ) {
    ArrayList<String> flipped = new ArrayList<String>();
    String rowString;
    for (int column = 0; column < dimensions[0]; column++) {
      rowString = "";
      for (int row = 0; row < dimensions[1]; row++) {
        rowString += puzzle.get(row).charAt(column);
      }
      flipped.add(column, rowString);
    }
    return flipped;
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
   * Print matches. Keep track of already printed words and skip
   * duplicates. Words that start at same index (substring word
   * inside another) sorted based on length.
   *
   * @param ret
   *
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
    // Read input files.
    List<String> dictionary = parseFile(
      args.length > 0 ? args[0] : "dictionary.txt",
      3
    );
    List<String> puzzleFile = parseFile(
      args.length > 1 ? args[1] : "specExample.txt",
      1
    );

    // Map puzzle grid.
    Integer[] dimensions = {
      Integer.parseInt(puzzleFile.get(1)),
      Integer.parseInt(puzzleFile.get(0)),
    };
    puzzleFile.subList(0, 2).clear();

    // Create rotated grid.
    ArrayList<String> flipped = flip(puzzleFile, dimensions);

    // Find then print matches.
    List<TreeMap<Integer, ArrayList<String>>> ret = new ArrayList<>(4);
    for (int i = 0; i < 4; i++) {
      ret.add(new TreeMap<Integer, ArrayList<String>>());
    }
    for (String word : dictionary) {
      String reversed = new StringBuilder(word).reverse().toString();
      search(puzzleFile, word, ret.get(0), false);
      search(puzzleFile, reversed, ret.get(1), true);
      search(flipped, word, ret.get(2), false);
      search(flipped, reversed, ret.get(3), true);
    }
    printPuzzle(ret);
  }
}

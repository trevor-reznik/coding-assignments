package p1a;  // this is just the package I created in my project, prob different for you

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.io.File;

public class Main 
{
	public static void main(String[] args) throws java.io.IOException 
	{   
/*
		//---- some I/O examples
        System.out.println("Type a letter: ");
        char letter = (char) System.in.read();
        System.out.println("You typed the letter " + letter);

        System.out.println("Type a letter: ");
		Scanner sin = new Scanner(System.in);
        char answer = sin.next().charAt(0);
        System.out.println("You typed the letter " + answer);
        
        System.out.println("Enter your age: ");
		int age = sin.nextInt();
        System.out.println("You are " + age);

        sin.nextLine(); // to consume the /n
        System.out.println("Enter your name: ");
		String name = sin.nextLine();
        System.out.println("You are " + name);
  */
        //---- file reading examples
        Scanner tfile = new Scanner(new File("testfile.txt"));
    	String s = tfile.nextLine();
        System.out.println(s);
        
        /*while (tfile.hasNext()) 
        {
        	s = tfile.nextLine();
            System.out.println(s);
        }*/
        
        List<String> dict_words = new ArrayList<String>();
        
        while (tfile.hasNext())
        {
        	s = tfile.nextLine(); //.trim().toLowerCase();
        	dict_words.add(s);
        }
        
        System.out.println(dict_words);        

        tfile.close();
        
        
        Scanner gfile = new Scanner(new File(args[0]));
        
        int grid_rows = Integer.valueOf(gfile.nextLine());
        int grid_cols = Integer.valueOf(gfile.nextLine());    

        char[][] grid = new char[grid_rows][grid_cols];
    	
        for (int r = 0; r < grid_rows; r++) 
        {
        	String line = gfile.nextLine(); //.trim().toLowerCase();
        	String[] parts = line.split(" ");
        	
            for (int c = 0; c < grid_cols; c++)
                grid[r][c] = parts[c].charAt(0);
        }

        for (int r = 0; r < grid_rows; r++)
        {
            for (int c = 0; c < grid_cols; c++)
                System.out.print(grid[r][c]);        
            System.out.println();	
        }
        
        // pass grid to a function
        PrintGrid(grid);
	}
	
	private static void PrintGrid(char[][] grid)
	{
		System.out.println("inside PrintGrid");
        for (int r = 0; r < grid.length; r++)
        {
            for (int c = 0; c < grid[0].length; c++)
                System.out.print(grid[r][c]);        
            System.out.println();	
        }		
	}

}


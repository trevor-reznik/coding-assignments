package P1b;   // this is just the package I created in my project, prob different for you

public class Main 
{
	public static void main(String[] args) 
	{
		System.out.println("Hello World!");
		
		int a = 55;
		int b = 121;
		int c = a + b;
		System.out.println("the sum of " + a + " and " + b + " is " + c);
		
		int gcd;
		gcd = GCD(a, b);
		
		System.out.println("the GCD of " + a + " and " + b + " is " + gcd);
	}

	private static int GCD( int a, int b )
	{
		System.out.println("inside GCD");
		
		while (a != b)
		{
			if (a > b)
				a = a - b;
			else
				b = b - a;
		}
		return b;
	}
}

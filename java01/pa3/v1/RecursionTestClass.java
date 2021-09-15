// import static org.junit.Assert.assertEquals;

// import org.junit.Test;

public class RecursionTestClass 
{
	//---- testIndexOf_test1 tests if s2 is not a substring of s1, should return -1.
	@Test
	public void testIndexOf_test1() {
        int result1 = Recursion.indexOf("Hello", "World");
        System.out.println("indexOf(Hello, World), got " + result1);
        assertEquals(-1, result1);
	}
	
	//---- testIndexOf_test2 should return 1.
	@Test
	public void testIndexOf_test2() {       
        int result2 = Recursion.indexOf("boring", "ing");
        System.out.println("indexOf(boring, ing), got " + result2);
        assertEquals(3, result2);	
    }

	//---- more tests...
	
}

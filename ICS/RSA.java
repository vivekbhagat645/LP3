import java.util.*;
import java.math.*;
class RSA 
{
	public static void main(String args[])
	{
		int p,q,n,z,i,e,d=0;
		double C,P;
		BigInteger msgback;
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter the number to be encrypted and decrypted:");
		P = sc.nextInt();
		
		System.out.println("Enter first prime number p:");
		p = sc.nextInt();
		
		System.out.println("Enter second prime number q:");
		q = sc.nextInt();
		
		n = p*q;
		
		z = (p-1)*(q-1);  //(fi of n)
		System.out.println("Value of z is:"+z);
		
		//e is for public key exponent
		for(e=2;e<z;e++)
		{
			if(gcd(e,z)==1)
			{
				break;
			}
		}
		System.out.println("Value of e is:"+e);
		
		//d is for private key exponent
		for(i=0;i<=9;i++)
		{
			int x = 1+(i*z);
			if(x%e==0)
			{
				d=x/e;
				break;
			}
		}
		System.out.println("Value of d is:"+d);
		
		C = (Math.pow(P,e))%n;
		System.out.println("Encrypted message is:"+(int)C);
		
		//P = 0;
		P = (Math.pow(C,d))%n;
		System.out.println("Decrypted message is:"+(int)P);
		
		//BigInteger N = BigInteger.valueOf(n);
		
		//BigInteger c = BigDecimal.valueOf(C).toBigInteger();
		//msgback = (c.pow(d)).mod(N);
		//System.out.println("Decrypted message is:"+msgback);
	}
	
	static int gcd(int e,int z)
	{
		if(e==0)
		{
			return z;
		}
		else
		{
			return gcd(z%e,e);
		}
	}
}
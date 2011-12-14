/*
 ============================================================================
 Name        : find_primes.c
 Author      : pfl
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void brute(int nMax)
{
	int i,j;

		for( i = 3; i<=nMax; i++)
		{
			for( j=3; j<=i; j++)
			{
				if ( i%j == 0 )
					break;
			}
			if( i == j)
				printf( "%i\n",i);
		}
}

void optimised_1(int nMax)
{
	int i,j;
	char thisIsAPrime;

			for( i = 3; i<nMax; i=i+2)
			{
				thisIsAPrime = 1;
				for( j=3; j<=sqrt(i); j++)
				{
					if ( i%j == 0 )
					{
						thisIsAPrime = 0;
						break;
					}

				}
				if( thisIsAPrime )
					printf( "%i\n",i);
			}
}

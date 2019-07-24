#include <cstdio>

int main() {
	
	int v1 = 100; 
	
	int *p1 = &v1; 
	
	int **pp1 = &p1; 
	
	int ***ppp1 = &pp1; 
	
	// printf("value:: v1=%d\np1=%d\n", v1, *p1); // 100, 100 
	
	printf("point:: v1=%p p1=%p\n", &v1, p1);
	// point:: v1=000000000022FE44 p1=000000000022FE44
	
	printf("point:: p1=%p pp1=%p\n", &p1, pp1);
	// point:: p1=000000000022FE38 pp1=000000000022FE38
	
	printf("point:: pp1=%p ppp1=%p\n", pp1, ppp1);

	printf("value:: *p1=%d  **pp1=%d ***ppp1=%d\n", *p1, **pp1, ***ppp1);	
	
	/*
		point:: v1=000000000022FE44 p1=000000000022FE44
		point:: p1=000000000022FE38 pp1=000000000022FE38
		point:: pp1=000000000022FE38 ppp1=000000000022FE30
		value:: *p1=100  **pp1=100 ***ppp1=100
	*/
	
	return 0; 
}

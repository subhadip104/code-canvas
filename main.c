#include<stdio.h>
int main () {
int n;
printf("enter the value of n: ");
scanf("%d",&n);
int sum = 0;

for (int i = 1; i <= n; ++i) {
    sum += i;
    }
    
    printf("Sum of numbers from 1 to %d is %d\n", n, sum);

return 0;
}
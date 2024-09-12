//program to increament a stack using array  in C DSA

#include <stdio.h>

#define MAX_SIZE 100

struct Stack {
    int items[MAX_SIZE];
    int top;
};

void initialize(struct Stack* stack) {
    stack->top = -1;
}

void push(struct Stack* stack, int item) {
    if (stack->top < MAX_SIZE - 1)
        stack->items[++stack->top] = item;
    else
        printf("Stack overflow!\n");
}

void increment_top(struct Stack* stack, int k) {
    if (stack->top >= 0)
        stack->items[stack->top] += k;
    else
        printf("Stack is empty!\n");
}

int main() {
    struct Stack my_stack;
    initialize(&my_stack);

    push(&my_stack, 10);
    push(&my_stack, 20);
    push(&my_stack, 30);

    printf("Original stack: %d %d %d\n", my_stack.items[0], my_stack.items[1], my_stack.items[2]);
    increment_top(&my_stack, 5);
    printf("Stack after incrementing top by 5: %d %d %d\n", my_stack.items[0], my_stack.items[1], my_stack.items[2]);

    return 0;
}



////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////
// factrioal of a number in C  DSA


#include <stdio.h>

unsigned long long fac(int n) {
    if (n == 0 || n == 1)
        return 1; 
    else
        return n * fac(n - 1); 
}

int main() {
    int num;
    printf("Enter a pnumber: ");
    scanf("%d", &num);

    if (num < 0)
        printf("Factorial is not defined\n");
    else
        printf("Factorial of %d = %llu\n", num, fac(num));

    return 0;
}

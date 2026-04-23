#include <stdio.h>
int main(){

    char operator;
    
    printf("enter the operator ['+', '-', '*', '/']: ");
    scanf("%c", &operator);

    double number1, number2;
    printf("choose first number: ");
    scanf("%lf", &number1);

    printf("choose second number: ");
    scanf("%lf", &number2);

    int result;
    switch(operator){
     case '+':
     result = number1 + number2;
     break;

     case '-':
     result = number1 - number2;
     break;

     case '*':
     result = number1 * number2;
     break;

     case '/':
     result = number1 / number2;
     break;
    }
    printf("result: %d", result);

return 0;
}

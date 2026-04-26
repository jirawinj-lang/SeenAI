#include <stdio.h>

int main(){
 
    char operator;
    printf("Enter the operator ['+', '-', '*', '/']: ");
    scanf("%c", &operator);

    double number1, number2;
    printf("Enter first number: ");
    scanf("%lf", &number1);

    printf("Enter second number: ");
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
    printf("result %d\n", result);


   int number;
   printf("Enter your birth day 1 to 7: ");
   scanf("%d", &number);

   switch(number){

    case 1:
    printf("monday");
    break;

    case 2:
    printf("tuesday");
    break;

    case 3:
    printf("wednesday");

    case 4:
    printf("tursday");
    break;

    case 5:
    printf("friday");
    break;

    case 6:
    printf("saturday");
    break;

    case 7:
    printf("sunday");
    break;

    defualt:
    printf("error value");
   }

   int number;
   printf("Enter the number: ")
   scanf("%d", &number)

   int count = 1;
   while(count < 5){
    int product = number * count;
    product("%d*%d = %d", number, count,product);
    count = count + 1;
   }





    return 0;
}
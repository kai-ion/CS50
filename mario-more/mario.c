#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int num = get_int("Enter a height between 1 - 8\n");
    //printf("Height: %d\n", num);
    while ( num < 1 || num > 8) {
        printf("Invalid Input\n");
        num = get_int("Enter a height between 1 - 8\n");
        //printf("Height: %d\n", num);
    }


    for (int i = 0; i < num; i++) {

        for (int k = num - i - 1; k > 0; k--) {
            printf(" ");
        }

        for (int j = i + 1; j > 0; j--) {
            printf("#");
        }

        printf("  ");

        for (int j = i + 1; j > 0; j--) {
            printf("#");
        }

        printf("\n");
    }

}
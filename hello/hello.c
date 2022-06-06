#include <stdio.h>
#include <cs50.h>

int main(void) {
    string userName = get_string("what is your name?\n");
    printf("hello, %s\n", userName);
}
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>


bool valid_key(string str) {
    for (int i = 0; i < strlen(str); i++)
    {
        if (!isalpha(str[i]))
        {
            return false;
        }
    }
    return true;
}

int main(int argc, string argv[])
{
    bool isValid = valid_key(argv[0]);

    printf("argv[0] = %s\n", argv[1]);
    printf("sizeof = %d\n", argc);

    if (argc != 1)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else if (argc == 1 && argv[0] == (null))
    {
        printf("Usage: ./substitution key\n");

    }
    else if (strlen(argv[0]) != 26 || !isValid)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
}
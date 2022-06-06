#include <cs50.h>
#include <stdio.h>
#include <string.h>


bool valid_key(string str) {
    
}

int main(int argc, string argv[])
{
    if (strlen(argv[0]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    else if (argc != 1)
    {
        printf("Usage: ./substitution key\n");
    }
}
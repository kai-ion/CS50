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

        for (int j = i + 1; j < strlen(str); j++)
        {
            if (tolower(str[i]) == tolower(str[j]))
            {
                return false;
            }
        }
    }
    return true;
}

string cipher_text(string str, string key) {
    
}

int main(int argc, string argv[])
{
    bool isValid = valid_key(argv[1]);

    printf("argv[1] = %s\n", argv[1]);

    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else if (strlen(argv[1]) != 26 || !isValid)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    string text = get_string("plaintext: ");

    string cipher = text;

    printf("ciphertext: %s", cipher);

    printf("\n");
    return 0;
}
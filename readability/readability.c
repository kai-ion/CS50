#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int count_letters(string text)
{
    int sum = 0;

    for (int i = 0; i < strlen(text); i++) {
        if (isalpha(text[i]) != 0)
        {
            sum++;
        }
    }

    return sum;
}

int count_words(string text)
{
    int sum = 0;

    for (int i = 0; i < strlen(text); i++) {
        if (isspace(text[i]) != 0)
        {
            sum++;
        }
    }


    return ++sum;
}

int count_sentences(string text)
{
    int sum = 0;

    for (int i = 0; i < strlen(text); i++) {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sum++;
        }
    }

    return sum;
}

int main(void)
{
    string text = get_string("Enter text\n");

    int letter;
    int word;
    int sentence;

    letter = count_letters(text);
    word = count_words(text);
    sentence = count_sentences(text);

    printf("letters: %d\n", letter);
    printf("words: %d\n", word);
    printf("sentences: %d\n", sentence);

    double L = letter / word * 100;
    double S = sentence / word * 100;

    double index = 0.0588 * L - 0.296 * S - 15.8;
    printf("Index: %f\n", index);

    if ( index < 1) {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade: %f\n", index);
    }

}


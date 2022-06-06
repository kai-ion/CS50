#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

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

    double letter = count_letters(text);
    double word = count_words(text);
    double sentence = count_sentences(text);

    //printf("letters: %f\n", letter);
    //printf("words: %f\n", word);
    //printf("sentences: %f\n", sentence);

    double L = letter / word * 100;
    double S = sentence / word * 100;

    //printf("L: %f\n", L);
    //printf("S: %f\n", S);

    double index = 0.0588 * L - 0.296 * S - 15.8;
    //printf("Index: %f\n", index);

    if ( index < 1) {
        printf("Before Grade 1\n");
    }
    else if (index > 16) {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %.0f\n", round(index));
    }

}


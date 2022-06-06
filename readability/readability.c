#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string text = get_string("Enter text\n");

    int letter;
    int word;
    int sentence;
    
    letter = count_letters(text);
    word = count_words(text);
    sentence = count_sentences(text);

    int l = letter / word * 100;
    int s = sentece / word * 100;

    int index = 0.0588 * L - 0.296 * S - 15.8;

    printf("Grade: %d/n", index);
}

int count_letters(string text) {
    int sum = 0

    return sum;
}

int count_words(string text) {
    int sum = 0

    return sum;
}

int count_sentences(string text) {
    int sum = 0

    return sum;
}
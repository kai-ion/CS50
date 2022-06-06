#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int text = get_string("Enter text\n");

    int l = count_letters(text);
    int w = count_words(text);
    int s = count_sentences(text);

    int index = 0.0588 * L - 0.296 * S - 15.8;

    printf("Grade: %d/n", index);
}

int count_letters(string text) {

}

int count_words(string text) {

}

int count_sentences(string text) {

}
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    bool isValid = false;
    bool isVisa = false;
    bool isMaster = false;
    bool isAmex = false;
    int len = 0;
    int sum = 0;
    int ft = 0; //first two

    long cardNum = get_long("Enter a credit card number. (numbers only)\n");

    while (cardNum != 0) {
        if (cardNum < 100 && cardNum > 10) {
            ft += cardNum;
        }

        if (len % 2 != 0) {
            int n = (cardNum % 10) * 2;
            while (n != 0) {
                sum += n % 10;
                n /= 10;
            }
//            printf("Card Check: %d\n", n);
        }
        else {
            int n = (cardNum % 10);
            sum += (cardNum % 10);
            //printf("Card Check: %d\n", n);
        }
        cardNum /= 10;
        //printf("cardNum: %ld\n", cardNum);
        len++;
    }

//    printf("ft: %d\n", ft);

    if ((len == 13 || len == 15 || len == 16) && sum % 10 == 0) {
        isValid = true;
        if (len == 15 && (ft == 34 || ft == 37)) {
            isAmex = true;
        }
        else if (len == 16 && (ft >= 51 && ft <= 55)) {
            isMaster = true;
        }
        else if (len == 16 || len == 13) {
            ft /= 10;
            if (ft == 4) {
                isVisa = true;

            }
            //printf("ft: %d\n", ft);
        }

//        printf("isValid: %d\n", isValid);

    }
    else {
        isValid = false;
    }


    printf("Card Length: %d\n", len);
    printf("Card Check: %d\n", sum);

    if (isValid) {
        if (isVisa) {
            printf("VISA\n");

        }
        else if (isMaster) {
            printf("MASTERCARD\n");
        }
        else if (isAmex) {
            printf("AMEX\n");
        }
        else {
            printf("INVALID\n");
        }
    }
    else {
        printf("INVALID\n");
    }
}

/**
 *
 * American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers
 *
All American Express numbers start with 34 or 37; most MasterCard numbers start with 51, 52, 53, 54, or 55
(they also have some other potential starting numbers which we won’t concern ourselves with for this problem); and all Visa numbers start with 4.
So that we can automate some tests of your code, we ask that your program’s last line of output be AMEX\n or MASTERCARD\n or VISA\n or INVALID\n, nothing more, nothing less.
*/

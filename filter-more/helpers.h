#include "bmp.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width]);

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i <  height; i++) {
        for (int j = 0; j < width/2; j++)
        {
            RGBTRIPLE temp = image[height][j];
        }
    }
};

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width]);

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width]);


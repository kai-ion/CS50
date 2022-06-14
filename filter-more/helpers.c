#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i <  height; i++) {
        for (int j = 0; j < width; j++)
        {
            BYTE avg = round((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen)/3.0);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i <  height; i++) {
        for (int j = 0; j < width/2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //temp array to keep original pixel
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }


    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float redSum = 0;
            float blueSum = 0;
            float greenSum = 0;
            float n = 0;
            //loop through surround pixels
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    //check if row or column in range
                    if ((i + k) < 0 || (i + k) >= height || (j + l) < 0 || (j + l) >= width)
                    {
                        continue;
                    }
                    redSum += temp[i+k][j+l].rgbtRed;
                    blueSum += temp[i+k][j+l].rgbtBlue;
                    greenSum += temp[i+k][j+l].rgbtGreen;
                    n++;
                }
            }
            image[i][j].rgbtRed = round(redSum / n);
            image[i][j].rgbtBlue = round(blueSum / n);
            image[i][j].rgbtGreen = round(greenSum / n);
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    //duplicate image to keep original value for calculation
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    //set sobel coefficient
    int Gx[3][3] = {-1, 0, 1} {-2,0,2}{-1,0,1};

    //loop through each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {

        }
    }

    return;
}

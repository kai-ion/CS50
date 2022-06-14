#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i <  height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            BYTE avg = round((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3.0);
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
    for (int i = 0; i <  height; i++)
    {
        for (int j = 0; j < width / 2; j++)
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
                    redSum += temp[i + k][j + l].rgbtRed;
                    blueSum += temp[i + k][j + l].rgbtBlue;
                    greenSum += temp[i + k][j + l].rgbtGreen;
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
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    //loop through each pixel rows by column
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float n = 0; //counter
            float gxRedSum = 0;
            float gxBlueSum = 0;
            float gxGreenSum = 0;
            float gyRedSum = 0;
            float gyBlueSum = 0;
            float gyGreenSum = 0;

            //loop through surround pixel
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    //if its an edge pixel, set it to black(value 0);
                    if ((i + k) < 0 || (i + k) >= height || (j + l) < 0 || (j + l) >= width)
                    {
                        continue;
                    }
                    gxRedSum += (temp[i + k][j + l].rgbtRed) * (Gx[k + 1][l + 1]);
                    gxBlueSum += (temp[i + k][j + l].rgbtBlue) * (Gx[k + 1][l + 1]);
                    gxGreenSum += (temp[i + k][j + l].rgbtGreen) * (Gx[k + 1][l + 1]);
                    gyRedSum += (temp[i + k][j + l].rgbtRed) * (Gy[k + 1][l + 1]);
                    gyBlueSum += (temp[i + k][j + l].rgbtBlue) * (Gy[k + 1][l + 1]);
                    gyGreenSum += (temp[i + k][j + l].rgbtGreen) * (Gy[k + 1][l + 1]);
                    n++;
                }
            }

            int red = round((sqrt(gxRedSum * gxRedSum + gyRedSum * gyRedSum)));
            int blue = round((sqrt(gxBlueSum * gxBlueSum + gyBlueSum * gyBlueSum)));
            int green = round((sqrt(gxGreenSum * gxGreenSum + gyGreenSum * gyGreenSum)));

            if (red > 255)
            {
                red = 255;
            }
            if (blue > 255)
            {
                blue = 255;
            }
            if (green > 255)
            {
                green = 255;
            }

            image[i][j].rgbtRed = red;
            image[i][j].rgbtBlue = blue;
            image[i][j].rgbtGreen = green;
        }
    }

    return;
}

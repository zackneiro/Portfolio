#include "helpers.h"
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

// I had a task to write the code to apply filters for the images in BMP format

// Function to return the smaller of two integers.
int min(int a, int b)
{
    return (a < b) ? a : b;
}

// Function to convert an image to grayscale by averaging the RGB values of each pixel.
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE *pixel = &image[i][j];
            int average = round((pixel->rgbtRed + pixel->rgbtGreen + pixel->rgbtBlue) / 3.0);
            pixel->rgbtRed = pixel->rgbtGreen = pixel->rgbtBlue = average;
        }
    }
}

// Function to reflect an image horizontally.
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Swap the pixels on horizontally opposite sides.
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
}

// Function to blur an image using a box blur algorithm.
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumRed = 0, sumGreen = 0, sumBlue = 0, count = 0;
            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di, nj = j + dj;
                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        sumRed += image[ni][nj].rgbtRed;
                        sumGreen += image[ni][nj].rgbtGreen;
                        sumBlue += image[ni][nj].rgbtBlue;
                        count++;
                    }
                }
            }
            temp[i][j].rgbtRed = round(sumRed / (float) count);
            temp[i][j].rgbtGreen = round(sumGreen / (float) count);
            temp[i][j].rgbtBlue = round(sumBlue / (float) count);
        }
    }

    // Copy the blurred image back to the original image array.
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
}

// Function to detect edges in an image using the Sobel operator.
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float sumXRed = 0, sumXGreen = 0, sumXBlue = 0;
            float sumYRed = 0, sumYGreen = 0, sumYBlue = 0;

            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int newI = i + di;
                    int newJ = j + dj;
                    if (newI >= 0 && newI < height && newJ >= 0 && newJ < width)
                    {
                        RGBTRIPLE pixel = image[newI][newJ];
                        int weightX = Gx[di + 1][dj + 1];
                        int weightY = Gy[di + 1][dj + 1];

                        sumXRed += pixel.rgbtRed * weightX;
                        sumXGreen += pixel.rgbtGreen * weightX;
                        sumXBlue += pixel.rgbtBlue * weightX;
                        sumYRed += pixel.rgbtRed * weightY;
                        sumYGreen += pixel.rgbtGreen * weightY;
                        sumYBlue += pixel.rgbtBlue * weightY;
                    }
                }
            }

            temp[i][j].rgbtRed = fmin(round(sqrt(sumXRed * sumXRed + sumYRed * sumYRed)), 255);
            temp[i][j].rgbtGreen = fmin(round(sqrt(sumXGreen * sumXGreen + sumYGreen * sumYGreen)), 255);
            temp[i][j].rgbtBlue = fmin(round(sqrt(sumXBlue * sumXBlue + sumYBlue * sumYBlue)), 255);
        }
    }

    // Apply the edge detection result to the original image.
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
}
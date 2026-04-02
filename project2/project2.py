import numpy as np
import cv2
import time

def logTransform(image):
    return

def powerTransform(image):
    return


def part1(image):
    cv2.imshow('default', image)
    cv2.waitkey(0)
    return

def part2(image):
    return

def part3(image):
    return

def part4(image):
    return

def part5(image):
    return

def main():
    fourier = cv2.imread('fourierspectrum.pgm')
    noisy = cv2.imread('noisy_atrium.png')
    sat = cv2.imread('sat_map.png')
    university = cv2.imread('university.png')
    part1(fourier)
    part2(university)
    part3(sat)
    part4(noisy)
    part5(noisy)

if __name__ == "__main__":
    main()
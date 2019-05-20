from PIL import Image, ImageOps
import math
from time import time


class Merge:
    def __init__(self, image_1_path, image_2_path):
        self.image_1 = self.get_image(image_1_path)
        self.image_2 = self.get_image(image_2_path)
        self.image_merged_width, self.image_merged_height = self.get_resolution_of_merged_image()
        self.image_merged = None

    class Decorators:
        @classmethod
        def save_image(self, func):
            def show(*args, **kwargs):
                image = func(*args, **kwargs)
                image.save("merged_image.bmp")
                return image

            return show

    def get_image(self, image_path):
        image = Image.open(image_path)
        return image
    
    def get_resolution_of_merged_image(self):
        image_1_width, image_1_height = self.image_1.size 
        image_2_width, image_2_height = self.image_2.size 
        image_merged_width = min(image_1_width, image_2_width)
        image_merged_height = min(image_1_height, image_2_height)
        return image_merged_width, image_merged_height
    
    @Decorators.save_image
    def merge_1_median(self):
        merged_image = Image.new("RGB", (self.image_merged_width, self.image_merged_height), "white")
        for x in range(self.image_merged_width):
            for y in range(self.image_merged_height):
                # get_first_image_pixel rgb values
                red1, green1, blue1 = self.image_1.getpixel((x, y))
                # get_second_image_pixel rgb values
                red2, green2, blue2 = self.image_2.getpixel((x, y))
                # calculate pixels median, using int to get integer values
                red = int((red1 + red2) / 2)
                green = int((green1 + green2) / 2)
                blue = int((blue1 + blue2) / 2)
                # put pixel into merged image
                merged_image.putpixel((x, y), (red, green, blue))
        self.image_merged = merged_image
        return self.image_merged

    @Decorators.save_image
    def merge_2_concat(self):
        merged_image = Image.new("RGB", (self.image_merged_width, self.image_merged_height), "white")
        for x in range(self.image_merged_width):
            for y in range(self.image_merged_height):
                # get_first_image_pixel rgb values
                red1, green1, blue1 = self.image_1.getpixel((x, y))
                # get_second_image_pixel rgb values
                red2, green2, blue2 = self.image_2.getpixel((x, y))
                # pixels sum, using int to get integer values
                red = int((red1 + red2))
                green = int((green1 + green2))
                blue = int((blue1 + blue2))
                # put pixel into merged image
                merged_image.putpixel((x, y), (red, green, blue))
        self.image_merged = merged_image
        return self.image_merged

    @Decorators.save_image
    def merge_3_blend(self):
        merged_image = Image.new("RGB", (self.image_merged_width, self.image_merged_height), "white")
        for x in range(self.image_merged_width):
            for y in range(self.image_merged_height):
                # get_first_image_pixel rgb values
                red1, green1, blue1 = self.image_1.getpixel((x, y))
                # get_second_image_pixel rgb values
                red2, green2, blue2 = self.image_2.getpixel((x, y))
                # pixels sum, using second image as background
                red = int((red1 + red2*0.5))
                green = int((green1 + green2*0.5))
                blue = int((blue1 + blue2*0.5))
                # put pixel into merged image
                merged_image.putpixel((x, y), (red, green, blue))
        self.image_merged = merged_image
        return self.image_merged
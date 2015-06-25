#########
#Similar.py
#Returns an integer value indicating how different two pictures are.
#Oct 4 2010
#########

import media
import Image

def red_average(pic):
    ''' Return an average red value of all the pixels in the Picture pic as an 
        integer. Truncate the result if the average calculation yields a
        non-integer value.'''
    
    sum_red = 0
    total_pix = 0
    
    for pixel in pic:
        sum_red += media.get_red(pixel)
        total_pix += 1
    
    average_red = (sum_red/total_pix)
    return average_red

def green_average(pic):
    ''' Return an average green value of all the pixels in the Picture pic as an 
        integer. Truncate the result if the average calculation yields
        a non-integer value.'''
    
    sum_green = 0
    total_pix = 0
    
    for pixel in pic:
        
        sum_green += media.get_green(pixel)
        total_pix += 1
    
    average_green = (sum_green/total_pix)
    return average_green

def blue_average(pic):
    ''' Return an average blue value of all the pixels in the Picture pic as an 
        integer. Truncate the result if the average calculation yields a
        non-integer value.'''
    
    sum_blue = 0
    total_pix = 0
    
    for pixel in pic:
        sum_blue += media.get_blue(pixel)
        total_pix += 1
    
    average_blue = sum_blue/total_pix
    return average_blue    

def scale_red(pic, new_red_average):
    ''' Take the Picture pic and set the average value of all red pixels in    
        the picture to the Integer new_average. Return scaled picture.
        Assume that the picture will have some colour component in it'''  
    
    old_average = float(red_average(pic))
    
    for pixel in pic:        
        new_red = (new_red_average / old_average) * media.get_red(pixel)
        if new_red > 255:
            new_red = 255
        media.set_red(pixel, int(new_red))
    
    return pic

def scale_green(pic, new_green_average):
    ''' Take the Picture pic and set the average value of all green pixels in    
        the picture to the Integer new_green_average. Return scaled picture
        Assume that the picture will have some colour component in it'''
   
    old_average = float(green_average(pic))
    
    for pixel in pic:        
        new_green = (new_green_average * media.get_green(pixel)) / old_average
        if new_green > 255:
            new_green = 255
        media.set_green(pixel, int(new_green))
    
    return pic

def scale_blue(pic, new_blue_average):
    ''' Take the Picture pic and set the average value of all blue pixels in    
        the picture to the Integer new_blue_average. Return scaled Picture 
        Assume that the picture will have some colour component in it'''
    
    old_average = float(blue_average(pic))
    
    for pixel in pic:        
        new_blue = (new_blue_average * media.get_blue(pixel)) / old_average 
        if new_blue > 255:
            new_blue = 255
        media.set_blue(pixel, int(new_blue))
    
    return pic


def expand_height(pic, expanding_factor):
    ''' Take Picture pic and return a duplicate of it that is vertically 
        stretched by an Integer expanding_factor'''
    
    new_width = pic.get_width()
    new_height = pic.get_height() * expanding_factor
    
    #create a new pic with new width, height and color black
    newpic = media.create_picture(new_width, new_height, media.black)
    
    #in new pic, align the x/y coordinate to that of old pic, get pixel and
    #use that pixel to get its color and set it as the new color for new pic
    for pixel in newpic:
        x_coordinate = media.get_x(pixel)
        y_coordinate = media.get_y(pixel) / expanding_factor
        newpixel = media.get_pixel(pic, x_coordinate, y_coordinate)
        new_color = media.get_color(newpixel)
        media.set_color(pixel, new_color)  
    return newpic

def expand_width(pic, expanding_factor):
    ''' Take Picture pic and return a duplicate of it that is horizontally 
        stretched by an Integer expanding_factor'''  
    
    new_width = (pic.get_width()) * expanding_factor
    new_height = pic.get_height()
    newpic = media.create_picture(new_width, new_height, media.black)
    
    for pixel in newpic:
        x_coordinate = media.get_x(pixel) / expanding_factor
        y_coordinate = media.get_y(pixel)
        newpixel = media.get_pixel(pic, x_coordinate, y_coordinate)
        
        new_color = media.get_color(newpixel)
        media.set_color(pixel, new_color)
    return newpic

def reduce_height(pic, reducing_factor):
    ''' Take Picture pic and return a duplicate of it that is vertically 
        compressed by an Integer reducing_factor''' 
      
    # Create a new Picture with the appropriate new height and old width, and
    # initialize the colour to black (all colour components are zero).
    new_width = pic.get_width()
    new_height = (pic.get_height() - 1) / reducing_factor + 1
    newpic = media.create_picture(new_width, new_height, media.black)
    
    # Iterate through all the Pixels in the large image, and copy
    # a portion of that Pixel's colour components into the correct 
    # Pixel position in the smaller image.
    for pixel in pic:
        # Find the corresponding Pixel in the new Picture.
        x_coordinate = media.get_x(pixel);
        y_coordinate = media.get_y(pixel) / reducing_factor;
        newpixel = media.get_pixel(newpic, x_coordinate, y_coordinate)
        
        # Add the appropriate fraction of this Pixel's colour components
        # to the components of the corresponding Pixel in the new Picture.
        new_red = newpixel.get_red() + pixel.get_red()/reducing_factor
        new_blue = newpixel.get_blue() + pixel.get_blue()/reducing_factor
        new_green = newpixel.get_green() + pixel.get_green()/reducing_factor
        
        media.set_red(newpixel, int(new_red))
        media.set_blue(newpixel, int(new_blue))
        media.set_green(newpixel, int(new_green))
        
    return newpic

def reduce_width(pic, reducing_factor):
    ''' Take Picture pic and return a duplicate of it that is horizontally 
        compressed by an Integer reducing_factor''' 
      
    # Create a new Picture with the appropriate old height and new width, and
    # initialize the colour to black (all colour components are zero).
    new_width = (pic.get_width() - 1) / reducing_factor + 1
    new_height = pic.get_height()
    newpic = media.create_picture(new_width, new_height, media.black)
    
    # Iterate through all the Pixels in the large image, and copy
    # a portion of that Pixel's colour components into the correct 
    # Pixel position in the smaller image.
    for pixel in pic:
        # Find the corresponding Pixel in the new Picture.
        x_coordinate = media.get_x(pixel)/reducing_factor;
        y_coordinate = media.get_y(pixel);
        newpixel = media.get_pixel(newpic, x_coordinate, y_coordinate)
        
        # Add the appropriate fraction of this Pixel's colour components
        # to the components of the corresponding Pixel in the new Picture.
        new_red = newpixel.get_red() + pixel.get_red()/reducing_factor
        new_blue = newpixel.get_blue() + pixel.get_blue()/reducing_factor
        new_green = newpixel.get_green() + pixel.get_green()/reducing_factor
        media.set_red(newpixel, int(new_red))
        media.set_blue(newpixel, int(new_blue))
        media.set_green(newpixel, int(new_green))
        
    return newpic

def distance(Pixel_1, Pixel_2):
    ''' Return an integer value indicating the difference between the two 
        pixels Pixel_1 and Pixel_2)'''
    
    #find the difference b/w values of pixel 2 and pixel 1 and sum the 
    #difference of R, G and B, then return the total diff.
    distance_red = abs(media.get_red(Pixel_1) - media.get_red(Pixel_2))
    distance_green = abs(media.get_green(Pixel_1) - media.get_green(Pixel_2))
    distance_blue = abs(media.get_blue(Pixel_1) - media.get_blue(Pixel_2))
     
    distance_total = distance_red + distance_green + distance_blue
    return distance_total

def simple_difference(pic_1, pic_2):
    ''' Return an integer value indicating the difference between two Pictures,
        pic_1 and pic_2, with the same dimensions'''
    
    sum_diff = 0
    
    #sum up all the distances for the corresponding pixels in the two pictures.
    #(add up all RGB value differences between pixels in the two pics)
    for pixel in pic_1:
        x_coordinate = media.get_x(pixel) 
        y_coordinate = media.get_y(pixel)
        sum_diff += distance(media.get_pixel(pic_1, x_coordinate, y_coordinate),
                             media.get_pixel(pic_2, x_coordinate, y_coordinate))
    
    return sum_diff


def smart_difference(pic_1, pic_2):
    ''' Return an integer value indicating the difference between two Pictures,
        pic_1 and pic_2, with different dimensions and colors. Assume that 
        the heights and widths of the two pictures are integer multiples
        of each other.'''
    
    #if the height of one pic is larger than the other, we create a new pic 
    #that is the same as the first one but with reduced height. Otherwise, we 
    #make a pic that is the same as pic_1, but this time, stretched.

    
    height_pic_1 = media.get_height(pic_1)
    width_pic_1 = media.get_width(pic_1)
    
    height_pic_2 = media.get_height(pic_2)
    width_pic_2 = media.get_width(pic_2)
    
    if height_pic_1 > height_pic_2:
        height_factor = float(height_pic_1 / height_pic_2)
        shorter_pic = reduce_height(pic_1, height_factor)
    else:
        height_factor = height_pic_2 / height_pic_1
        shorter_pic = expand_height(pic_1, height_factor)
    width_shorter_pic = media.get_width(shorter_pic)
    
    if width_shorter_pic > width_pic_2:
        width_factor = width_shorter_pic / width_pic_2
        adjusted_pic = reduce_width(shorter_pic, width_factor)
    else:
        width_factor = width_pic_2 / width_shorter_pic
        adjusted_pic = expand_width(shorter_pic, width_factor)
    
    #scale the new pic we have based on the average colours of pic_2
    scale_red_to = red_average(pic_2)
    scale_green_to = green_average(pic_2)
    scale_blue_to = blue_average(pic_2)
    
    adjusted_pic = scale_red(adjusted_pic, scale_red_to)
    adjusted_pic = scale_green(adjusted_pic, scale_green_to)
    adjusted_pic = scale_blue(adjusted_pic, scale_blue_to)
    
    scale_red_to = red_average(adjusted_pic)
    scale_green_to = green_average(adjusted_pic)
    scale_blue_to = blue_average(adjusted_pic)
    
    #run simple_difference function between new pic and pic_2
    true_difference = simple_difference(adjusted_pic, pic_2)
    
    return true_difference

if __name__ == "__main__":
    a=media.load_picture("original.jpg")
    b=media.load_picture("mosaic.jpg")
    print smart_difference(a,b)
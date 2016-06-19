import os
import Image
import media
import time
import mosaic

class EnhancedMosaic(mosaic.Mosaic):
    ''' Enhance the performance of the mosaics and/or increase efficiency '''
    
    def __init__(self, path):
        ''' Creata a picture database that stores all images from directory 
        path to the Mosaic object. '''
        
        self.database = os.listdir(path)
        self.pic_database = {}
        self.pic_size_database = {} 
        for img in self.database:
            im = Image.open(os.path.join(path, img))
            self.pic_database[im] = _avg_color(im)
            self.pic_size_database[im] = (im.size[0], im.size[1])
            
        self.picture = None
        #created a dictionary with images from path as keys and their average 
        #color objects as values - a process that will aid in saving time   
        #created 2nd dictionary with images from path as keys and their sizes 
        #a tuple of (width, height) as values. 
        
    def create_mosaic(self, filename, min_size, threshold):
        ''' Create a Mosaic that performs more efficiently than Fractal Mosaic
        and/or has a better quality '''
        
        picture = Image.open(filename)        
        
        def _helper_fractal(self, image, min_size, threshold):
            ''' Help parent function create a fractal photomosaic version of a
            single pict by applying the algorithm on portions of the original
            pic '''
            
            width = image.size[0]
            height = image.size[1]         
            
            match = _match(image, threshold, self.pic_database, width, height)
            
            if (width >= min_size or height >= min_size) and not match:
                quad_a = image.crop((0, 0, int(width / 2), int(height / 2)))
                quad_b = image.crop((int(width / 2), 0, int(width), \
                                     int(height / 2)))
                quad_c = image.crop((0, int(height / 2), int(width / 2), \
                                     int(height)))
                quad_d = image.crop((int(width / 2), int(height / 2), \
                                     int(width), int(height)))
                #divided the picture into four equal parts
                
                result_a = _helper_fractal(self, quad_a, min_size, threshold) 
                result_b = _helper_fractal(self, quad_b, min_size, threshold) 
                result_c = _helper_fractal(self, quad_c, min_size, threshold) 
                result_d = _helper_fractal(self, quad_d, min_size, threshold)
                #keep dividing into more parts until its size is < min_size
                #then, find best entry and paste it onto the part and return it
                
                image.paste(result_a, (0, 0))
                image.paste(result_b, (int(width / 2), 0))
                image.paste(result_c, (0, int(height / 2)))
                image.paste(result_d, (int(width / 2), int(height / 2)))
                
            elif match:
                image.paste(match)
            
            elif (width < min_size or height < min_size):
                
                d = {} 
                img_avg_color = _avg_color(image)
                for img in self.pic_database:
                    d[_distance(img_avg_color, self.pic_database[img])] = img
                # created a new dictionary with distance as key, image as value
                
                closest_img = d[min(d.keys())]
                if closest_img.size is not image.size: 
                    closest_img = closest_img.resize((width, height))
                image.paste(closest_img)
                #base case needs to return modified part
            return image       
        
        self.picture = _helper_fractal(self, picture, min_size, threshold)  
        
    def save_as(self, filename):
        ''' Save the final Mosaic as an jpeg image with the Filename filename.
        If the Mosaic was not created, do not save. '''
        
        if self.picture:
            filename = str(filename) + '.jpeg'
            self.picture.save(filename)
                
def _avg_color(image):
    ''' Return the average color object of the Image image '''
    
    h = image.histogram()        
    red_count = h[0:256]
    green_count = h[256:512]
    blue_count = h[512:768]
    sum_of_red_values = sum_of_green_values = sum_of_blue_values = 0
    total_pixels = image.size[0] * image.size[1]
    
    for i in range(256):
        if red_count:
            sum_of_red_values += red_count[i] * i
        if green_count:
            sum_of_green_values += green_count[i] * i
        if blue_count:
            sum_of_blue_values += blue_count[i] * i
    if total_pixels: # <-- if total_pixels is not 0: 
        #can't divide by 0 on Earth - apparently the limit approaches infinity.
        average_red = sum_of_red_values / total_pixels
        average_green = sum_of_green_values / total_pixels
        average_blue = sum_of_blue_values / total_pixels
    else:
        average_red = average_green = average_blue = 0
    
    return (average_red, average_green, average_blue)

def _distance(col1, col2):
    ''' Return the Eucleadean distance between the two pixels '''
    
    red1, green1, blue1 = col1[0], col1[1], col1[2]
    red2, green2, blue2 = col2[0], col2[1], col2[2]
    return ((((red1 - red2) ** 2) + ((blue1 - blue2) ** 2) + \
             ((green1 - green2) ** 2)) ** 0.5)

def _match(image, threshold, pic_database, width, height):
    ''' Go thru the dictionary and return matching pic or None.'''
     
    pixels = image.getdata() 
    for pic in pic_database:
        total = 0
        if pic.size is not image.size:         
            pic = pic.resize((width, height))
        picdata = pic.getdata()
        length = len(pixels)
        for i in range(length):            
            distance = _distance(pixels[i], picdata[i])
            total += distance   
        if (total / length) < threshold:
            return pic
    return None   

if __name__ == '__main__':
    x = time.time()
    m = EnhancedMosaic('images')
    m.create_mosaic('original.jpg',100, 85)
    m.save_as('mosaic_enhanced')
    print time.time() - x
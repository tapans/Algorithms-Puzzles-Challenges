import os
import media
import Image
import mosaic
import time

class FractalMosaic(mosaic.Mosaic):
    ''' #Build a basic photomosaic. i.e. a single picture represented as a grid 
    of smaller component pictures. '''
    
    def __init__(self, path):
        ''' Creata a picture database that stores all images from directory 
        path to the Mosaic object. '''
        
        self.database = os.listdir(path)
        self.pic_database = {}
        for img in self.database:
            im = Image.open(os.path.join(path, img))
            self.pic_database[os.path.join(path, img)] = _avg_color(im)
        self.picture = None
        #created a dictionary with images from path as keys and their average 
        #color objects as values - a process that will aid in saving time   
        
    def create_mosaic(self, filename, min_size, threshold):
        ''' Create and store a photomosaic version of the single picture
        specified by file filename. '''
              
        picture = Image.open(filename)
        
        def _helper_fractal(self, image, min_size, threshold):
            ''' Help parent function create a fractal photomosaic version of a
            single pict by applying the algorithm on portions of the original
            pic '''
            
            width = image.size[0]
            height = image.size[1]                    
            
            match = _match(image, threshold, self.pic_database)
            
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
                closest = [image, 99999999999] #arbitrary starting point
                img_avg_color = _avg_color(image) #call helper function 
                for pic in self.pic_database:
                    avg_color = self.pic_database[pic]
                    distance1 = media.distance(avg_color, img_avg_color)
                    if distance1 < closest[1]:
                        closest = [pic, distance1]
                closest_img = Image.open(closest[0])
                closest_img = closest_img.resize((width, height))
                #closest entry from the database is resized to match image size
                
                image.paste(closest_img)
                #base case needs to return modified part
            return image 
                
        self.picture = _helper_fractal(self, picture, min_size, threshold)   
                             
    def save_as(self, filename):
        ''' Save the picture that stores the photomosaic resulting from 
        create_mosaic in a file called filename If the photomosaic hasn't been 
        created yet, don't save anything.'''
            
        if self.picture != None:
            filename = str(filename)
            filename = filename + '.jpg'
            self.picture.save(filename)        
            
def _match(image, threshold, pic_database):
    ''' Go thru the dictionary and return matching pic or None.'''
    
    width = image.size[0]
    height = image.size[1]   
    pixels = image.getdata()
      
    for pic in pic_database:
        total = 0
        pic = Image.open(pic)
        pic = pic.resize((width, height))
        picdata = pic.getdata()
        for i in range(len((picdata))):            
            distance = help_distance(pixels[i], picdata[i])
            total += distance            
        if int(total / len(picdata)) < threshold:
            return pic
    return None
        
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

def help_distance(col1, col2):
    ''' Return the Eucleadean distance between the two colors '''
    
    red1, green1, blue1 = col1[0], col1[1], col1[2]
    red2, green2, blue2 = col2[0], col2[1], col2[2]
    return int((((red1 - red2) ** 2) + ((blue1 - blue2) ** 2) + \
                ((green1 - green2) ** 2)) ** 0.5)  

if __name__ == '__main__':
    x = time.time()
    m = FractalMosaic('images')
    m.create_mosaic('original.jpg', 20,75)
    m.save_as('mosaic_fractal')
    print time.time() - x

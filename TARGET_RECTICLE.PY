import cv2 as cv
import numpy as np

class TARGET_RECTICLE:
    
    def __init__(self,x0,y0,x1,y1,B0,G0,R0,PATH):
        self.x0     =   x0
        self.y0     =   y0
        self.x1     =   x1
        self.y1     =   y1
        self.B0     =   B0
        self.G0     =   G0
        self.R0     =   R0
        #self.frame  =   frame
        #self.mtrx   =   mtrx
        #self.width  =   width
        #self.height =   height
        self.PATH   =   PATH
        
        
    def load_img(self, PATH):
        return cv.imread(PATH)

    def rescale_img(self, frame, scale=0.5):
        width = int(frame.shape[1] * scale)
        height = int(frame.shape[0] * scale)
        dimensions = (width, height)
        return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
  
    def show_reduced_img(self,PATH):
        img = cv.imread(PATH)
        resized_img = self.rescale_img(self.load_img(PATH))
        cv.imshow('REDUCED_SIZE_IMG_SAMPLE', resized_img) 
        cv.waitKey(0)

    def change_res(self, width, height, PATH):
        #* LIVE VIDEO ONLY
        capture = cv.VideoCapture(PATH)
        capture.set(3,width)
        capture.set(4,height)
    
        while True:
            isTrue, frame = capture.read()
            cv.imshow('VIDEO', frame)
        
            if cv.waitKey(20) & 0xFF==ord('q'):
                break 
            
        capture.relaes()
        cv.destroyAllWindows()       
            
    def create_blank_matrix(self):
        self.mtrx = np.zeros((500,500,3), dtype='uint8')
        self.mtrx[:] = 255,255,255
        return self.mtrx

    def show_blank_matrix(self):
        cv.imshow('BLANK_MATRIX_SAMPLE', self.create_blank_matrix())
        cv.waitKey(0)

    def show_color_matrix_range(self,x0,y0,x1,y1,B0,G0,R0):
        self.mtrx = self.create_blank_matrix()
        self.mtrx[x0:y0, x1:y1] = R0,G0,B0
        cv.imshow('SHOW_COLOR_MATRIX_RANGE', self.mtrx)
        cv.waitKey(0)
    
    def draw_target_recticle(self,mtrx,x0,y0,x1,y1, B0,G0,R0):
        return cv.rectangle(self,mtrx,(x0,y0),(x1,y1), (B0,G0,R0),thickness=1)    

    def show_target_recticle(self,mtrx,x0,y0,x1,y1, B0,G0,R0):
        self.draw_target_recticle(self,mtrx,x0,y0,x1,y1,B0,G0,R0)
        cv.imshow('SHOW_TARGET_RECTICLE', mtrx)
        cv.waitKey(0)
    
x0 = 0 
y0 = 0
x1 = 100
y1 = 100

B0 = 0
G0 = 0
R0 = 255

PATH = r'C:\Users\Administrator\OneDrive - SUNY Polytechnic Institute\DSP\DEV\PROJECTS\PYTHON\COMPUTER_VISION\img\Warno-feature-2000x1270-1.jpg'    

t = TARGET_RECTICLE(x0,y0,x1,y1,B0,G0,R0,PATH)
t.load_img(PATH)
 
import cv2
import numpy as q
import settings
from pose.estimator import TfPoseEstimator
from pose.networks import get_graph_path


img1=cv2.imread("neck1-removebg-preview.png")
cv2.imshow("necklace",img1)
ty="jewellery"
#cv.imshow('necklace',img1)
def fit_object1(img2,x1,y1,x2,y2,x3,y3):
    print("hi")

    try:
        
#        print("s")
        
        dim = (x2-x1,y3-y1)
        img1_rs = cv2.resize(img1,dim,interpolation = cv2.INTER_CUBIC)
        img1_gray = cv2.cvtColor(img1_rs,cv2.COLOR_BGR2GRAY)
#        print("s")
        rows,cols = img1_rs.shape[:2]
        if ty=="full":
            roi = (img2[y1-int(yded):y3+int(yded1),x1-int(xded):x2+int(xded1)])
        elif ty=="jewellery":
           roi = (img2[y3-50:y3+30,x1:x2+10])
# print("s")
        #cv2.imshow("roi",roi)
#        print("s")
#        print(roi.shape)
#        print("s")
        if ty=="full":
            ret,mask = cv2.threshold(img1_gray,10,255,cv2.THRESH_BINARY)
        elif ty=="jewellery":
            ret,mask = cv2.threshold(img1_gray,30,255,cv2.THRESH_BINARY)
        
        j=roi.shape[0]
        t=roi.shape[1]
    
        mask_inv = cv2.bitwise_not(mask)
#        cv2.imshow("mask",mask)
#        cv2.imwrite("mask.jpg",mask)
#        kernel = np.ones((5,5),np.uint8)
#        dilation = cv2.dilate(mask,kernel,iterations = 1)
#        cv2.imshow("dilation",dilation)
#        cv2.imshow("mask1",mask)
        j=roi.shape[0]
        t=roi.shape[1]
        mask_inv = cv2.bitwise_not(mask)
        mask_inv = cv2.resize(mask_inv,(t,j),interpolation = cv2.INTER_CUBIC)
        
        mask=cv2.resize(mask,(img1_rs.shape[1],img1_rs.shape[0]),interpolation = cv2.INTER_CUBIC)            
        #cv2.imshow("maskinv",mask_inv)
        img1_bo = cv2.bitwise_and(roi,roi,mask=mask_inv)
        #cv2.imshow("bg",img1_bo)
        
        img2_fg = cv2.bitwise_and(img1_rs,img1_rs,mask=mask)
        
        img2_fg=cv2.resize(img2_fg,(t,j),interpolation = cv2.INTER_CUBIC)
        
        final = cv2.add(img1_bo,img2_fg)
#        cv2.imshow("final1",final)
#        final = cv2.blur(final,(2,3))
        
#        cv2.imshow("blur",final)
        if ty=="full":
            
            img2[y1-int(yded):y3+int(yded1),x1-int(xded):x2+int(xded1)] = final
        elif ty=="jewellery":
            img2[y3-50:y3+30,x1:x2+10]= final
#        cv2.imshow('final',img2)
#        cv2.imwrite(str(name),img2)
        print("sucess")
        return img2
    except:
        print("hi")

ix,iy = 0,0
r=300
c=295
poseEstimator = None

poseEstimator = TfPoseEstimator(get_graph_path('mobilenet_thin'), target_size=(432, 368))
def maskf(image):
    
    mask = np.zeros(image.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    rect = (1,0,image.shape[1],image.shape[0])
    
    mask, bgModel, fgModel=cv2.grabCut(image,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    outputMask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD),0, 1)

# scale the mask from the range [0, 1] to [0, 255]
    outputMask = (outputMask * 255).astype("uint8")
    return outputMask
#cap=cv2.VideoCapture('rtsp://admin:rashmi2018@192.168.51.162/PSIA/streaming/channels/102')    
       
def fit_object(img2,x1,y1,x2,y2,x3,y3):
    
    
    try:
#    cap = cv2.VideoCapture(0)
        
#        img2=model
        
        
        
        dim = (x2-x1,y3-y1)
        img1_rs = cv2.resize(img1,dim,interpolation = cv2.INTER_CUBIC)
        
        rows,cols = img1_rs.shape[:2]
        roi = (img2[y3:y3+100,x1:x2+10])
        mask=maskf(img1_rs)
        
        j=roi.shape[0]
        t=roi.shape[1]
        mask_inv = cv2.bitwise_not(mask)
        mask_inv = cv2.resize(mask_inv,(t,j),interpolation = cv2.INTER_CUBIC)
        
        mask=cv2.resize(mask,(img1_rs.shape[1],img1_rs.shape[0]),interpolation = cv2.INTER_CUBIC)            
        cv2.imshow("maskinv",mask_inv)
        img1_bo = cv2.bitwise_and(roi,roi,mask=mask_inv)
        cv2.imshow("bg",img1_bo)
        
        img2_fg = cv2.bitwise_and(img1_rs,img1_rs,mask=mask)
        
        img2_fg=cv2.resize(img2_fg,(t,j),interpolation = cv2.INTER_CUBIC)
        
        final = cv2.add(img1_bo,img2_fg)
        cv2.imshow("final1",final)
        img2[y3:y3+10,x1:x2+10] = final
    
        cv2.imshow('final',img2)
        cv2.imwrite("fit_jewel.jpg",img2)
        return img2
    except:
        return img1


cap=cv2.VideoCapture(0)
'''
these are the keypoint values stored in the 2D list Values
Nose = 0
Neck = 1
RShoulder = 2
RElbow = 3
RWrist = 4
LShoulder = 5
LElbow = 6
LWrist = 7
RHip = 8
RKnee = 9
RAnkle = 10
LHip = 11
LKnee = 12
LAnkle = 13
REye = 14
LEye = 15
REar = 16
LEar = 17
Background = 18
'''

while True:
    
    ret,frame=cap.read()
    Values=[]
    img3=[]
    
    if ret :
        print(ret)
        show = cv2.resize(frame, (settings.winWidth, settings.winHeight))
        
        humans = poseEstimator.inference(show)
                   
        show,Values = TfPoseEstimator.draw_humans(show, humans, imgcopy=False)
        cv2.imwrite("personpoints.jpg",show)
        flag1=0
        flag2=0
        flag3=0
        for val in Values:
            if val[0]==2:
                hal="hi"
                
            if val[0]==5:
                x2=val[1]
                y2=val[2]
                
            if val[0]==1:
                flag3=1
                print("Neck")
                print(val[1])
                print(val[2])
                x3=val[1]
                y3=val[2]
            if val[0]==16:
                print("Rear")
                x1=val[1]
                y1=val[2]
                flag1=1
                print(val[1])
                print(val[2])
            if val[0]==17:
                print("Lear")
                x2=val[1]
                y2=val[2]
                flag2=9
                print(val[1])
                print(val[2])
    if flag1 and flag2 and flag3:
        print(x1,y1,x2,y2,x3,y3)
        print("True")
       
        img3=fit_object1(frame,x1,y1,x2,y2,x3,y3)
#        cv2.imshow("model",img3)
    if flag1 and flag2 and flag3:
         cv2.imshow("frame",img3)
    else:
        cv2.imshow("frame",show)
      
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
        

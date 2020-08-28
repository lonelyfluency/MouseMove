from PIL import ImageGrab
import cv2
import aircv as ac
import pyautogui
import time

def catch_screen():
    im = ImageGrab.grab()
    im.save("screen.png")

def get_obj_pos():
    screen_img = ac.imread('screen.png')
    im_obj_hor = ac.imread('hor.png')
    tar_pos_hor = ac.find_template(screen_img,im_obj_hor)
    tar_p_hor = tar_pos_hor['result']
    return tar_p_hor

def move_xy(th,x,y,v,t):
    center_xy = (th[0]-294,th[1]-239)
    pyautogui.moveTo(center_xy)
    tx = x/((x**2+y**2)**(1/2))
    ty = y/((x**2+y**2)**(1/2))
    
    pyautogui.moveRel(-v*tx,v*ty)
    pyautogui.mouseDown()
    time.sleep(t)
    pyautogui.mouseUp()

    

def move_z(th,z,v,t):
    center_z = (th[0]-85,th[1]-239)
    
    pyautogui.moveTo(center_z)
    pyautogui.moveRel(0,-v*z)
    pyautogui.mouseDown()
    time.sleep(t)
    pyautogui.mouseUp()


if __name__ == "__main__":
    catch_screen()
    th = get_obj_pos()
    move_xy(th,10,20,70,1)
    move_z(th,1,70,1)



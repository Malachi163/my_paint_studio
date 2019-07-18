def setup():
    global myFill 
    myFill = "red"
    size(512,512)
    background(255)
    rectangleWidth = width/4
    
    fill(255,0,0)
    rect(0,0,rectangleWidth,30) #red box
    
    fill(0,0,255)
    rect(128,0,rectangleWidth,30) #blue box
    
    fill(255,255,0)
    rect(256,0,rectangleWidth,30) # yellow box
    
    fill(255,255,255)
    rect(384,0,rectangleWidth,30) #white box

def draw():
    global myFill
    
    # if(keyPressed and key == 'c' ):
    #     fill(255,255,255)
    #     ellipse(mouseX,mouseY,20,20)
    # line(0, 0, width, height) #line going across the screen
    
    # if(keyPressed and key == 'c' ):
    #     if displayHeight >= 30:
            
    #         fill(255,255,255)
    # #     ellipse(mouseX,mouseY,20,20)
    
        
    if mouseButton and mouseY < 30:
        if mouseX < 128:
            myFill = "red"
        elif mouseX > 128 and mouseX <= 256:
            myFill = "blue"
            
        elif mouseX > 256 and mouseX <= 384: 
            myFill = "yellow"
            
        elif mouseX > 384:
            myFill = "white"
    
    elif mouseButton and mouseY > 30:
        if myFill == "red":
            fill(255,0,0)
        elif (myFill == "blue"):
            fill(0,0,255)
            
        elif (myFill == "white"):
            fill(255,255,255)
            
            ellipse(mouseX,mouseY,70,70)
            
        else:
            fill(255,255,0)
        noStroke()
        ellipse(mouseX, mouseY, 10,10)

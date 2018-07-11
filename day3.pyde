def setup():
    size (600, 600)
    background(255)
    rect(20, 500, 200, 80) 
    fill(253, 237, 236)
    rect(20, 500, 40, 40) #
    fill(170, 183, 184)
    rect(20, 540, 40, 40) #
    fill(39, 55, 70)
    rect(60, 500, 40, 40)
    fill(39, 174, 96)
    rect(60, 540, 40, 40)
    fill(241, 148, 138)
    rect(100, 500, 40, 40)
    fill(255, 87, 51)
    rect(100, 540, 40, 40)
    fill(255, 195, 0)
    rect(140, 500, 40, 40)
    fill(218, 247, 166)
    rect(140, 540, 40, 40)
    fill(142, 68, 173)
    rect(180, 500, 40, 40)
    fill(52, 152, 219)
    rect(180, 540, 40, 40)


    
def draw():
    leftBoundary= 250
    bottomBoundary = 20
    if mousePressed and mouseX>= leftBoundary:
        line(pmouseX, pmouseY, mouseX, mouseY)
    if mousePressed and mouseY <= bottomBoundary:
        line(pmouseX, pmouseY, mouseX, mouseY)
def mouseClicked():
    if mouseX >= 20 and mouseX >= 60:
        stroke(253, 237, 236)
    elif mouseY > 500 and mouseY < 540:
        stroke
    


    
    

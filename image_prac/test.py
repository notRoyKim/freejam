from PIL import Image
from PIL import ImageDraw
from PIL import ImageChops
from PIL import ImageStat
import sys
import time

source = Image.open("source.jpg")
sx,sy = source.size
target = Image.open("target2.jpg")
tx,ty = target.size
tolerance = 30;
step = 2;

print("source size : ", source.size)
print("Target size : ", target.size)

trial = 0

def Search(cx, cy, tolerance):
    compare = source.crop((cx,cy,cx+tx,cy+ty))
    print("compare size: ",compare.size)

    diff = ImageChops.difference(compare, target)
    stat = ImageStat.Stat(diff)
    global trial
    if max(max(stat.extrema[0]), max(stat.extrema[1]), max(stat.extrema[2])) <= tolerance :
        print("target found : ", stat.extrema)
        return True
    else:
        trial += 1
        return False
draw = ImageDraw.Draw(source)
start = time.time()

for y in range(sy - ty):
    for x in range(0,sx-tx,step):
        compare = source.crop((x,y,x+10,y+10))
        partial_target = target.crop((0,0,10,10))
        diff = ImageChops.difference(compare,partial_target)
        stat = ImageStat.Stat(diff)

        if max(max(stat.extrema[0]), max(stat.extrema[1]), max(stat.extrema[2])) < tolerance:
            if Search(x,y,tolerance) == True:
                print("Top left point: (%d, %d)" %(x,y))
                print("Center of target point : (%d, %d)" %(x+target.width/2,y+target.height/2))
                print("try", trial)
                draw.rectangle((x,y,x+target.width, y + target.height), outline = (255,0,0))
                end = time.time()
                print("time",end - start)
                source.show()
                sys.exit()
            else:
                print("not found (%d, %d):" %(x,y))
                print("wrong detection", trial)
end = time.time()
print("image search failed")

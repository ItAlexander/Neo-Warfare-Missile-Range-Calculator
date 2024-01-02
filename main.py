import math

def maybeMakeNumber(s):  
    if not s:
        return s
    try:
        f = float(s)
        i = int(f)
        return i if f == i else f
    except ValueError:
      return s

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

def calcRange(burn, mAcc, mSpeed, ySpeed,eSpeed,dirAng):
    ykmps = ySpeed * 1.852 / 3600
    mAkmps = (mAcc * 1.852) / 3600
    mVkmps = (mSpeed * 1.852) / 3600
    ekmps = (eSpeed * 1.852) / 3600
    accTime = (mVkmps-ykmps) / mAkmps
    if accTime < burn:
        conTime = burn - accTime
    else:
        conTime = 0
        accTime = burn
    mDisAc = ykmps*accTime + (mAkmps * accTime * accTime) / 2
    mDisCon = mVkmps * conTime
    mDis = mDisAc + mDisCon
    eDis = ekmps * burn
    if dirAng == 180 or dirAng == 0:
        if dirAng == 180:
            dis = mDis - eDis
        if dirAng == 0:
            dis = mDis + eDis
    else:
        mAng = math.degrees(math.asin((eDis * math.sin(math.radians(dirAng)) / mDis)))
        cAng = 180 - mAng - dirAng
        dis = (mDis * math.sin(math.radians(cAng))) / math.sin(
            math.radians(dirAng))
    return dis

def makeCalc(burn, mAcc, mSpeed):
    eSpeed = (int)(input("What's the enemy's speed: "))
    while True:
        dirAng = (int)(input("What's target ditection relatively to you(angle from 0(towards you) to 180 (from you): "))
        if dirAng>=0 and dirAng<=180:
            break
        print("Not valid direction angle.")
    ySpeed = (int)(input("What is your speed?: "))
    print("----------------------------------------------------")
    print("Max effective range: "+ str(calcRange(burn, mAcc, mSpeed, ySpeed,eSpeed,dirAng)))

print("Welcome To sashabronya's optimal firing range for missiles calculator. Original idea of realmadridmydestiny1.")
print("version 1.2 All rights reserved. 2023")
with open("presets.txt", "r") as f:
        mls =list(map(str,f.readlines()[0].split(" ")))
while True:
    print("----------------------------------------------------")
    mode = "c"
    mode = input("What mode to use(ru or us-preset,c-custom,q-quit): ")
    if mode in mls:
      print("----------------------------------------------------")
      idc = 0
      with open("missiles_" + mode + ".txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            idc+=1
            print(line)
      print("----------------------------------------------------")
      while True:
        id=(int)(input("Missile id: "))
        if id>0 and id<idc:
            break
        print("Not valid ID.")
      ar=list(map(str,lines[id].split(" ")))
      statArray = list(map(int,filter(is_integer_num,list(map(maybeMakeNumber, ar)))))
      burn, mAcc, mSpeed = statArray[1], statArray[2], statArray[3]
      makeCalc(burn, mAcc, mSpeed)
    elif mode == "c":
        burn = (int)(input("What is the missile's burn time?: "))
        mAcc = (int)(input("What is the missile's acceleration?: "))
        mSpeed = (int)(input("What is the missile's maximum speed?: "))
        makeCalc(burn, mAcc, mSpeed)
    elif mode == "q":
        print("Shutting down.")
        quit();
    else:
        print("Unknown mode. Try again.")
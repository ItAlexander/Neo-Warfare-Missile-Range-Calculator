import math

def maybeMakeNumber(s):  
    # handle None, "", 0
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

print("Welcome To sashabronya's optimal firing range for missiles calculator. Original idea of realmadridmydestiny1.")
print("version 1.0 All rights reserved. 2022")
print("----------------------------------------------------")
mode = "c"
mode = input("What mode to use(p-preset,c-custom)")
if mode == "p":
  print("----------------------------------------------------")
  with open("missiles.txt", "r") as f:
    i=0
    lines = f.readlines()
    for line in lines:
        print(line)
  print("----------------------------------------------------")
  id=(int)(input("Missile id: "))
  ar=list(map(str,lines[id].split(" ")))
  statArray = list(map(int,filter(is_integer_num,list(map(maybeMakeNumber, ar)))))
  burn, mAcc, mSpeed = statArray[1], statArray[2], statArray[3]
elif mode == "c":
    burn = (int)(input("What is the missile's burn time?: "))
    mAcc = (int)(input("What is the missile's acceleration?: "))
    mSpeed = (int)(input("What is the missile's maximum speed?: "))
else:
  print("Unknown mode")
  quit()
eSpeed = (int)(input("What's the enemy's speed: "))
dirAng = (int)(input("What's target ditection relatively to you(angle from 0(towards you) to 180 (from you): "))
ySpeed = (int)(input("What is your speed?: "))
print("----------------------------------------------------")
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
print("Missile distance: " + str(mDis))
eDis = ekmps * burn
print("Enemy distance: " + str(eDis))
if dirAng == 180 or dirAng == 0:
    if dirAng == 180:
        dis = mDis - eDis
    if dirAng == 0:
        dis = mDis + eDis
else:
    mAng = math.degrees(
        math.asin((eDis * math.sin(math.radians(dirAng)) / mDis)))
    cAng = 180 - mAng - dirAng
    dis = (mDis * math.sin(math.radians(cAng))) / math.sin(
        math.radians(dirAng))
print(dis)
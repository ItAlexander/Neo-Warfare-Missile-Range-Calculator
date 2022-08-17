import math

print("Welcome To sashabronya's optimal firing range for missiles calculator. Original idea of realmadridmydestiny1.")
print("version 0.2. All rights reserved. 2022")
print("----------------------------------------------------")
mode = "c"
#mode = input("What mode to use(p-preset,c-custom)")
if mode == "p":
    print("WIP")
    quit()
if mode == "c":
    burn = (int)(input("What is the missile's burn time?: "))
    mAcc = (int)(input("What is the missile's acceleration?: "))
    mSpeed = (int)(input("What is the missile's maximum speed?: "))
eSpeed = (int)(input("What's the enemy's speed: "))
dirAng = (int)(input(
    "What's target ditection relatively to you(angle from 0(towards you) to 180 (from you): "
))
ySpeed = (int)(input("What is your speed?: "))
print("----------------------------------------------------")
ykmps = ySpeed * 1.852 / 3600
mAkmps = (mAcc * 1.852) / 3600
mVkmps = (mSpeed * 1.852) / 3600
ekmps = (eSpeed * 1.852) / 3600
accTime = mVkmps / mAkmps
if accTime < burn:
    conTime = burn - accTime
else:
    conTime = 0
    accTime = burn
mDisAc = ykmps * accTime + (mAkmps * accTime * accTime) / 2
mDisCon = mVkmps * conTime
mDis = mDisAc + mDisCon
eDis = ekmps * burn
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
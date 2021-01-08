import pyautogui
import time

breachX = open("breachX.txt", "r")
breachY = open("breachY.txt", "r")
brimstoneX = open("brimstoneX.txt", "r")
brimstoneY = open("brimstoneY.txt", "r")
cypherX = open("cypherX.txt", "r")
cypherY = open("cypherY.txt", "r")
jettX = open("jettX.txt", "r")
jettY = open("jettY.txt", "r")
killjoyX = open("killjoyX.txt", "r")
killjoyY = open("killjoyY.txt", "r")
omenX = open("omenX.txt", "r")
omenY = open("omenY.txt", "r")
phoenixX = open("phoenixX.txt", "r")
phoenixY = open("phoenixY.txt", "r")
razeX = open("razeX.txt", "r")
razeY = open("razeY.txt", "r")
reynaX = open("reynaX.txt", "r")
reynaY = open("reynaY.txt", "r")
sageX = open("sageX.txt", "r")
sageY = open("sageY.txt", "r")
skyeX = open("skyeX.txt", "r")
skyeY = open("skyeY.txt", "r")
sovaX = open("sovaX.txt", "r")
sovaY = open("sovaY.txt", "r")
viperX = open("viperX.txt", "r")
viperY = open("viperY.txt", "r")
lockX = open("lockX.txt", "r")
lockY = open("lockY.txt", "r")

#Breach
breachMouseX = breachX.readline()
breachMouseY = breachY.readline()

#Brimstone
brimstoneMouseX = brimstoneX.readline()
brimstoneMouseY = brimstoneY.readline()

#Cypher
cypherMouseX = cypherX.readline()
cypherMouseY = cypherY.readline()

#Jett
jettMouseX = jettX.readline()
jettMouseY = jettY.readline()

#Killjoy
killjoyMouseX = killjoyX.readline()
killjoyMouseY = killjoyY.readline()

#Omen
omenMouseX = omenX.readline()
omenMouseY = omenY.readline()

#Phoenix
phoenixMouseX = phoenixX.readline()
phoenixMouseY = phoenixY.readline()

#Raze
razeMouseX = razeX.readline()
razeMouseY = razeY.readline()

#Reyna
reynaMouseX = reynaX.readline()
reynaMouseY = reynaY.readline()

#Sage
sageMouseX = sageX.readline()
sageMouseY = sageY.readline()

#Skye
skyeMouseX = skyeX.readline()
skyeMouseY = skyeY.readline()

#Sova
sovaMouseX = sovaX.readline()
sovaMouseY = sovaY.readline()

#Viper
viperMouseX = viperX.readline()
viperMouseY = viperY.readline()

#LockIn
lockMouseX = lockX.readline()
lockMouseY = lockY.readline()


# print(breachMouseX,breachMouseY,brimstoneMouseX,brimstoneMouseY,cypherMouseX,
# cypherMouseY,jettMouseX,jettMouseY,killjoyMouseX,killjoyMouseY,omenMouseX,omenMouseY,
# phoenixMouseX,phoenixMouseY,razeMouseX,razeMouseY,reynaMouseX,reynaMouseY,sageMouseX,sageMouseY,
# skyeMouseX,skyeMouseY,sovaMouseX,sovaMouseY,viperMouseX,viperMouseY, lockMouseX, lockMouseY)

print("Which agent do you want?")
print("1 -->  Breach")
print("2 -->  Brimstone")
print("3 -->  Cypher")
print("4 -->  Jett")
print("5 -->  Killjoy")
print("6 -->  Omen")
print("7 -->  Phoenix")
print("8 -->  Raze")
print("9 -->  Reyna")
print("10 --> Sage")
print("11 --> Skye")
print("12 --> Sova")
print("13 --> Viper")

inputStr = input()
input = int(inputStr)
counter = 0

time.sleep(1)

#Breach
if input == 1:
    print("You chose Breach.")
    while counter <= 50:
        pyautogui.moveTo(int(breachMouseX), int(breachMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1

    


#Brimstone
elif input == 2:
    print("You chose Brimstone.")
    while counter <= 50:
        pyautogui.moveTo(int(brimstoneMouseX), int(brimstoneMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Cypher
elif input == 3:
    print("You chose Cypher.")
    while counter <= 50:
        pyautogui.moveTo(int(cypherMouseX), int(cypherMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Jett
elif input == 4:
    print("You chose Jett.")
    while counter <= 50:
        pyautogui.moveTo(int(jettMouseX), int(jettMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Killjoy
elif input == 5:
    print("You chose Killjoy.")
    while counter <= 50:
        pyautogui.moveTo(int(killjoyMouseX), int(killjoyMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Omen
elif input == 6:
    print("You chose Omen.")
    while counter <= 50:
        pyautogui.moveTo(int(omenMouseX), int(omenMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Phoenix
elif input == 7:
    print("You chose Phoenix.")
    while counter <= 50:
        pyautogui.moveTo(int(phoenixMouseX), int(phoenixMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Raze
elif input == 8:
    print("You chose Raze.")
    while counter <= 50:
        pyautogui.moveTo(int(razeMouseX), int(razeMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Reyna
elif input == 9:
    print("You chose Reyna.")
    while counter <= 50:
        pyautogui.moveTo(int(reynaMouseX), int(reynaMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Sage
elif input == 10:
    print("You chose Sage.")
    while counter <= 50:
        pyautogui.moveTo(int(sageMouseX), int(sageMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Skye
elif input == 11:
    
    print("You chose Skye.")
    while counter <= 50:
        pyautogui.moveTo(int(skyeMouseX), int(skyeMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Sova
elif input == 12:
    print("You chose Sova.")
    while counter <= 50:
        pyautogui.moveTo(int(sovaMouseX), int(sovaMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#Viper
elif input == 13:
    print("You chose Viper.")
    while counter <= 50:
        pyautogui.moveTo(int(viperMouseX), int(viperMouseY))
        pyautogui.click()
        pyautogui.moveTo(int(lockMouseX), int(lockMouseY))
        pyautogui.click()
        counter = counter + 1


#InvalidAgent
else:
    print("This isnt a valid agent.")




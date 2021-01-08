import pyautogui
import time

#Explanation    
print("This programm saves the location of all the agents and the lock in button.")
print("The locations get saved in a .txt file in the same folder as this python file is.")
print("To use it copy the location.txt file into the same folder as the ValorantAgentPicker.py is located in.")


#Breach
print("Please hover your cursor over Breach and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(5)
breachMouseX, breachMouseY = pyautogui.position()
pyautogui.alert("Done.(Breach)")


#Brimstone
print("Please hover your cursor over Brimstone and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
brimstoneMouseX, brimstoneMouseY = pyautogui.position()
pyautogui.alert("Done.(Brimstone)")


#Cypher
print("Please hover your cursor over Cypher and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
cypherMouseX, cypherMouseY = pyautogui.position()
pyautogui.alert("Done.(Cypher)")


#Jett
print("Please hover your cursor over Jett and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
jettMouseX, jettMouseY = pyautogui.position()
pyautogui.alert("Done.(Jett)")


#Killjoy
print("Please hover your cursor over Killjoy and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
killjoyMouseX, killjoyMouseY = pyautogui.position()
pyautogui.alert("Done.(Killjoy)")


#Omen
print("Please hover your cursor over Omen and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
omenMouseX, omenMouseY = pyautogui.position()
pyautogui.alert("Done.(Omen)")


#Phoenix
print("Please hover your cursor over Phoenix and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
phoenixMouseX, phoenixMouseY = pyautogui.position()
pyautogui.alert("Done.(Phoenix)")


#Raze
print("Please hover your cursor over Raze and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
razeMouseX, razeMouseY = pyautogui.position()
pyautogui.alert("Done.(Raze)")


#Reyna
print("Please hover your cursor over Reyna and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
reynaMouseX, reynaMouseY = pyautogui.position()
pyautogui.alert("Done.(Reyna)")


#Sage
print("Please hover your cursor over Sage and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
sageMouseX, sageMouseY = pyautogui.position()
pyautogui.alert("Done.(Sage)")


#Skye
print("Please hover your cursor over Skye and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
skyeMouseX, skyeMouseY = pyautogui.position()
pyautogui.alert("Done.(Skye)")


#Sova
print("Please hover your cursor over Sova and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
sovaMouseX, sovaMouseY = pyautogui.position()
pyautogui.alert("Done.(Sova)")


#Viper
print("Please hover your cursor over Viper and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
viperMouseX, viperMouseY = pyautogui.position()
pyautogui.alert("Done.(Viper)")

#LockIn
print("Please hover your cursor over the lock in Button and wait until you get a message box that sais, that it has been saved. You have 5 seconds.")
time.sleep(3)
lockMouseX, lockMouseY = pyautogui.position()
pyautogui.alert("Done.(LockIn)")



breachX = open("breachX.txt", "w")
breachY = open("breachY.txt", "w")
brimstoneX = open("brimstoneX.txt", "w")
brimstoneY = open("brimstoneY.txt", "w")
cypherX = open("cypherX.txt", "w")
cypherY = open("cypherY.txt", "w")
jettX = open("jettX.txt", "w")
jettY = open("jettY.txt", "w")
killjoyX = open("killjoyX.txt", "w")
killjoyY = open("killjoyY.txt", "w")
omenX = open("omenX.txt", "w")
omenY = open("omenY.txt", "w")
phoenixX = open("phoenixX.txt", "w")
phoenixY = open("phoenixY.txt", "w")
razeX = open("razeX.txt", "w")
razeY = open("razeY.txt", "w")
reynaX = open("reynaX.txt", "w")
reynaY = open("reynaY.txt", "w")
sageX = open("sageX.txt", "w")
sageY = open("sageY.txt", "w")
skyeX = open("skyeX.txt", "w")
skyeY = open("skyeY.txt", "w")
sovaX = open("sovaX.txt", "w")
sovaY = open("sovaY.txt", "w")
viperX = open("viperX.txt", "w")
viperY = open("viperY.txt", "w")
lockX = open("lockX.txt", "w")
lockY = open("lockY.txt", "w")




#Breach
breachX.write(str(breachMouseX))
breachY.write(str(breachMouseY))

#Brimstone
brimstoneX.write(str(brimstoneMouseX))
brimstoneY.write(str(brimstoneMouseY))


#Cypher
cypherX.write(str(cypherMouseX))
cypherY.write(str(cypherMouseY))


#Jett
jettX.write(str(jettMouseX))
jettY.write(str(jettMouseY))


#Killjoy
killjoyX.write(str(killjoyMouseX))
killjoyY.write(str(killjoyMouseY))


#Omen
omenX.write(str(omenMouseX))
omenY.write(str(omenMouseY))


#Phoenix
phoenixX.write(str(phoenixMouseX))
phoenixY.write(str(phoenixMouseY))


#Raze
razeX.write(str(razeMouseX))
razeY.write(str(razeMouseY))


#Reyna
reynaX.write(str(reynaMouseX))
reynaY.write(str(reynaMouseY))


#Sage
sageX.write(str(sageMouseX))
sageY.write(str(sageMouseY))



#Skye
skyeX.write(str(skyeMouseX))
skyeY.write(str(skyeMouseY))



#Sova
sovaX.write(str(sovaMouseX))
sovaY.write(str(sovaMouseY))



#Viper
viperX.write(str(viperMouseX))
viperY.write(str(viperMouseX))


#LockIn
lockX.write(str(lockMouseX))
lockY.write(str(lockMouseY))



#Simulacija Month Hall problema
import random

#Za simulaciju s vise mogucih izbora [samo jedan je tocan]
noOfDoors = 3;

def generateSelection():
	allChoices = [0] * noOfDoors;
	k = random.randint(0, noOfDoors-1);
	allChoices[k] = 1;
	return allChoices;
	
def hostOpensDoors(possibilites, userChoice):
	while True:
		hostChoice = random.randint(0, noOfDoors-1);
		if (hostChoice != userChoice and possibilites[hostChoice] != 1):
			return hostChoice;
		
def newUserChoice(oldChoice, hostChoice):
	while True:
		newChoice = random.randint(0, noOfDoors-1);
		if newChoice != oldChoice and newChoice != hostChoice:
			return newChoice;
		

def main():
	noCorrect = 0;
	noWrong = 0;
	loopCount = 100000;
	alwaysChangeDoors = True;
	useRandomChanging = False; #for fun
	
	for i in range(loopCount):
		selection = generateSelection();
		
		choice = random.randint(0, noOfDoors-1);
		#print 'Igrac otvara vrata ' + str(choice) + ' sto mu daje ' + str(selection[choice])
		
		hostChoice = hostOpensDoors(selection, choice);		
		#print 'Host otvara druga vrata: ' + str(hostChoice) + ' sto mu daje ' + str(selection[hostChoice])
		
		#Promjena izbora - random ili uvijek izmjeni ili ostani na pocetnom izboru	
		if useRandomChanging:
			coinToss = random.randint(0, 2);
			if coinToss == 1:
				choice = newUserChoice(choice, hostChoice);	
		elif alwaysChangeDoors:
			choice = newUserChoice(choice, hostChoice);		
		
		#Statistic countr
		if (selection[choice] == 1):
			noCorrect += 1;
		else:
			noWrong += 1;
			
	print 'Uvijek mijenjam vrata - ' + str(alwaysChangeDoors);
	print 'Konacni izracun:';
	print '  TOCNO:'+ str(noCorrect);
	print '  KRIVO:'+ str(noWrong);
	print 'Preciznost: ' + str(noCorrect * 100 / loopCount) + '%';



if __name__ == '__main__':
	main()
#Izracun PI preko monte carlo metode
import random;

circleCircumfence = 1000;
loopCount = 1000000;
epsilon = 0.00001;

def throwDart():
	a = random.uniform(-circleCircumfence, circleCircumfence+epsilon);
	b = random.uniform(-circleCircumfence, circleCircumfence+epsilon);	
	return (a,b);
	
def isInCircle(position):
	x = position[0];
	y = position[1];
	result = x**2 + y**2;
	
	return result <= circleCircumfence**2;

def main():
	hitsInsideCircle = 0;	
	
	for i in range(loopCount):	
		position = throwDart();
		#print position;
		
		if isInCircle(position):
			#print 'HIT'
			hitsInsideCircle += 1;
		
	print 'Result for ' + str(loopCount) + ' throws';
	print 'Darts inside circle: ' + str(hitsInsideCircle);	
	
	#hitsInsideCircle / loopCount ~= areaCircle / areaSquare
	#	= circleCircumfence**2 * PI / (2*circleCircumfence)**2	
	#hitsInsideCircle / loopCount == 4 / PI
	#PI hitsInsideCircle / loopCount = 4
	#PI = 4 * hitsInsideCircle / loopCount
	
	myPiValue = 4.0 * float(hitsInsideCircle) / loopCount;
	print 'My PI values is ' + str(myPiValue);	

if __name__ == '__main__':
	main();
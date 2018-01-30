'''
def loop1_10(a, b, c):
	print a, b, c;
	for i in range(1, 11):
		time.sleep(0.5)
		print(i)
		
def abcd():
	abcd = ['A', 'B', 'C', 'D']
	for i in range(len(abcd)):
		print(abcd[i])
		time.sleep(1)
	print('ABCD is done');
	
arguments = (1, 2, 3)
thread1 = threading.Thread(target=loop1_10, name='Counter', args=arguments);
thread1.start();
thread2 = threading.Thread(target=abcd, name='Abcd');
thread2.start();

thread2.join()
print('Thread 2 done');

#print(thread1.name);
#while (thread2.isAlive()):
#	time.sleep(1);
'''
import threading;
import time;
import Producers;

class Consumer():	
	def __init__(self, product, production_interval, max_capacity, grainProvider, milkProvider, PRINT_INFO):
		self.product = product
		self.items = 0;
		self.grainProvider = grainProvider;
		self.milkProvider = milkProvider;
		self.production_interval = production_interval;
		self.max_capacity = max_capacity;	
		self.totalProduction = 0
		self.print_info = PRINT_INFO;
	
	def produce(self):
		self.items += 1;	
		self.totalProduction += 1;
		
	def consume(self):
		self.items -= 1;
	
	def startProduction(self, grain_thread, milk_thread):
		while (self.items < self.max_capacity):
			if (self.grainProvider.items > 1 and self.milkProvider.items > 0):
				self.grainProvider.consume();
				self.grainProvider.consume();
				self.milkProvider.consume();
				self.produce();
				if(self.print_info):
					print(str(self.product) + ' created product! Current total: ' + str(self.items));
				
			if (not(grain_thread.isAlive() or milk_thread.isAlive())):
				print(str(self.product) + ' - Other production has stopped, going bankrupt...');
				break;
		if (self.print_info):
			print (str(self.product) + ' max capacity reached - production stopped!');
		print (str(self.product) + ' created ' + str(self.totalProduction) + ' entries in my lifetime');

		
PRINT_INFO = True;
	
grainProdvider = Producers.Producer('Grain', 3, 15, PRINT_INFO);
milkProdvider = Producers.Producer('Milk', 2, 15, PRINT_INFO);

grain_thread = threading.Thread(target=grainProdvider.startProduction, name='Grain_thread');
milk_thread = threading.Thread(target=milkProdvider.startProduction, name='Milk_thread');
bakeryConsumer = Consumer('Cake', 6, 80, grainProdvider, milkProdvider, PRINT_INFO);

#Start capitalism
grain_thread.start();
milk_thread.start();
bakeryConsumer.startProduction(grain_thread, milk_thread);




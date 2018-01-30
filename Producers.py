import time;

class Producer():	
	

	def __init__(self, product, production_interval, max_capacity, PRINT_INFO):
		self.product = product;
		self.items = 0;
		self.production_interval = production_interval;
		self.max_capacity = max_capacity;
		self.totalProduction = 0;
		self.max_totalProduction = 100;
		self.print_info = PRINT_INFO;
	
	def produce(self):
		self.items += 1;
		self.totalProduction += 1;
		
	def consume(self):
		if (self.items > 0):
			self.items -= 1;
		else:
			raise ValueError('Cant consume');
	
	def startProduction(self):
		time.sleep(2 * self.production_interval); #first production is slowest
		while (self.items < self.max_capacity):
			if (self.totalProduction >= self.max_totalProduction):	#dont over produce, 'cause its bad for the environment
				break;
			self.produce();
			if (self.print_info):
				print(str(self.product) + ' created product! Current total: ' + str(self.items));
			time.sleep(self.production_interval);

		
		if (self.print_info):
			print (str(self.product) + ' max capacity reached - production stopped!');
		print (str(self.product) + ' created ' + str(self.totalProduction) + ' entries in my lifetime');
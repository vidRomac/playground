#Deprecated

import urllib2
import re

def main():	
	a = 1
	main_url = 'http://eu.battle.net/sc2/en/'
	
	print "Otvaram web stranicu " + main_url
	stranica = urllib2.urlopen(main_url)
	linije = stranica.readlines()
	nadeno = False
	for red in linije:
		if re.search(r'have them compete(.)<\/p>', red):
			nadeno = True
			break
			
	if not nadeno:
		print 'Stranica nije nadena!'
		return
		
	#print red
	#print linije.index(red)
	#print linije[linije.index(red) + 2]
	
	match = re.search(r'href=\"(blog\/\w+#blog)\"', linije[linije.index(red) + 2])

	#print match.group(1)
	
	url = main_url + match.group(1)
	
	print "Nadena lista ..."
	
	while (1):
		print '\n'
		stranica= urllib2.urlopen(url)
		linije= stranica.readlines()
	
		terran = 0
		protoss = 0
		zerg = 0
		random = 0
		
		pozicija = 1
		
		prvi_igrac = 0
		najbolji_random = 0
		prva_rasa = 0

		for line in linije:
		
			datum = re.search(r'span> (\d+)\-(\w+)\-(\d+)', line)
			
			if datum:
				print "Datum: " + datum.group(1) + "." + datum.group(2) + "." + datum.group(3)
		
		
			match = re.search(r'class=\"race\-(\w+)\"', line)
			sljedeca = re.search(r'200 players in Europe \(<a href=\"http:\/\/eu.battle.net\/sc2\/en\/blog\/(\d+)', line)			
			
			if sljedeca:
				if sljedeca.group(1) == '554903':				#zadnja 'standardna stranica'
					print 'Daljnje pretrazivanje nije moguce!'
					a = 0
				else:
					url = main_url + 'blog/' + sljedeca.group(1)
					#print url

			if match:
				

				if not prvi_igrac:
					prvi_igrac = re.search(r'>(\w+)<\/a>', line)
					#print prvi_igrac.group(1)			
				if match.group(1) == 'terran':
					terran += 1
				elif match.group(1) == 'zerg':
					zerg += 1
				elif match.group(1) == 'protoss':
					protoss += 1
				else:
					random += 1
					if not najbolji_random:
						najbolji_random = pozicija
				pozicija += 1
				if not prva_rasa:
					prva_rasa = match.group(1)
		
		print "Na prvom mjestu se nalazi igrac " + prvi_igrac.group(1) + " sa rasom " + prva_rasa.upper() + "."
		print "Od ukupno " + str(terran + zerg + protoss + random) + " igraca, u listi se nalazi:"
		print '	-' + str(terran) + " Terrana"
		print '	-' + str(protoss) + " Protossa"
		print '	-' + str(zerg) + " Zerga"
		print '	-' + str(random) + " Randoma (najbolja pozicija je " + str(najbolji_random) + ')'
		
		a = raw_input ("\nPogledati tjedan ranije? (prazno za kraj) ")
		if not a:
			break
	
if __name__=='__main__':
  main()
#skripta za brzo potrazivanje tweetova odredene osobe ili skupine osoba zapisanih u datoteci popis.txt

import twitter #instal into py libs
import re
import time

destinacija = 'C:\Vid\programiranje\Radno\popis.txt'		#lokacija datoteke popis.txt


def main():
	#destinacija = 'C:\Vid\programiranje\Radno\popis.txt'
	file = open(destinacija, 'r+')
	print "Skripta za ucitavanje tweetova"
	while(1):
		print "\n----------------------------------------------"
		print "Opcije: "
		print "1. Ucitaj tweetove neke osobe"				#TODO
		print "2. Ispisi listu osoba koji se trenutno prate"
		print "3. Izaberi osobu iz liste pracenja"			#maknut
		print "4. Dodaj osobu u listu pracenja"
		print "5. Makni osobu iz liste pracenja"
		print "6. Ocitaj zadnje tweetove svih iz liste"		#TODO
		print "7. Izlaz"
		print "\n----------------------------------------------"
		odluka = int(raw_input('Navedite koju opciju zelite... '))
		
		if odluka == 1:
			ime = raw_input("Navesti ID osobe cije tweetove zelite: ")
			get_tweets(ime)
			
		elif odluka == 2:
			procitaj_listu(file)		#samo ispis

		elif odluka == 3:				
			pogledaj_listu(file)		#pogled s izborom
			
		elif odluka == 4:
			ime = raw_input("Navesti ID osobe koju zelite pratiti: ")
			dodaj_u_listu(ime, file)
			
		elif odluka == 5:
			procitaj_listu(file)
			ime = raw_input("Navesti ime koje zelite izbaciti iz liste: ")			
			potvrda = raw_input("jeste sigurni da zelite maknuti " + ime +" iz liste? (y/n): ")
			print '--------------------------------------------'
			if potvrda == 'y':
				makni_iz_liste(ime, file)
			elif potvrda == 'n':
				continue	
			else:
				print "Error!"
				continue
		
		elif odluka == 6:
			nizaj_tweetove(file)

		elif odluka == 7:
			file.close()
			return 0
		else:
			print "Error! Invalid number entered"
			
def nizaj_tweetove(file):
	file.seek(0)
	for line in file:
		if line[-1] == '\n':
			line = line[:-1]
		print line
		tekst = get_tweet(line)
		print '------------------------------------------'
	print 'KRAJ'
	raw_input('Pristinite enter za povratak u glavni meni...')
	return

def get_tweet(name):
	link = twitter.Api()
	statusi = link.GetUserTimeline(name)
	print '\t' + statusi[0].text
	del link
	return statusi[0]
	
def get_tweets(name):
	if name == 'RealTimeWWII':
		reverse_tweets(name)
		return
	link = twitter.Api()
	statusi = link.GetUserTimeline(name)
	print 'Tweets from ' + name + ':'
	print '\t--' + statusi[0].text + '\n'
	print '\t--' + statusi[1].text + '\n'
	odgovor = 'da'
	i = 2
	while (odgovor == 'da'):
		print '\t--' + statusi[i].text
		odgovor = raw_input('jos? (da/ne): ')
		i += 1
		if i == 20:
			print 'Limit dostignut!'
			break
	del link
	return

def reverse_tweets(name):
	link = twitter.Api()
	statusi = link.GetUserTimeline(name)
	for i in range(len(statusi)):
		print '\t--' + statusi[-(i+1)].text
		time.sleep(4)
	del link
	return
		
	
def pogledaj_listu(file):			#pogled s izborom
	procitaj_listu(file)
	izbor = int(raw_input('Navesti redni broj osobe cije tweetove zelite pogledati ili 0 za kraj: '))
	
	if izbor == 0: 				#ili neki terminator
		return
	ime = uzmi_ime(izbor, file)
	print ime,
	if ime[-1] == '\n':
		ime = ime[0:-1]
	get_tweets(ime)
	pogledaj_listu(file)
	return
	
def uzmi_ime(redni_broj, file):
	file.seek(0)
	lista_imena = file.readlines()
	return lista_imena[redni_broj - 1]
		
def procitaj_listu(file):			#samo ispis
	file.seek(0)
	lista = file.readlines()
	print "Sadrzaj datoteke:"
	for num in range(len(lista)):
		if lista[num] != '\n' or lista[num] != '\0':
			print "  " + str(num + 1) + ". " + lista[num],
	print "\n --Kraj datoteke"
	return
		
def dodaj_u_listu(ime, file):		#TODO popraviti polozaje pokazivaca kod umetanja
	file.seek(0, 2)
	file.write(ime + '\n')
	procitaj_listu(file)
	return

def makni_iz_liste(ime, file):
	file.seek(0)
	lista = file.read()				#original lista
	lokacija = lista.find(ime)
	if lokacija != -1:
		file = open(destinacija, 'w')					#brise sadrzaj originalne datoteke popis.txt
		file.write(lista[0:lokacija])					#pise sadrzaj iz orig. sve do maknutog clana
		file.write(lista[lokacija + len(ime) + 1:])		#pise ostatak sadrzaja
		file.close()
		file = open(destinacija, 'r+')					#otvara sa citanjem i pisanjem
		print 'Osoba s ID-om ' + ime + ' uspjesno je maknuta iz liste!'
	else:
		print 'Osoba s ID-om ' + ime + ' nije u listi pracenja!'
		
	procitaj_listu(file)
	return
	
if __name__ == '__main__':
	main()
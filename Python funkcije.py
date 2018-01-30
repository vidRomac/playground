import sys 			#za input sa terminala
import re  			#za 'trazilicu' (regex)
import datetime		#vrijeme
import time 		#za sleep
import calendar		#kalendar
import urllib		#internet 1.
import urllib2		#internet 2.
import zipfile		#zip
import pickle		#pickle, kodiranje (?)
import os			#dodatne komande za rad s OS-om
import subprocess	#podprocesi
import shutil		#za kopiranje datoteke
import winsound		#za sviranje zvukova, vezanih uz windows
import Image		#manipuliranje slikama, vise na http://www.pythonware.com/library/pil/handbook/image.htm
import ImageDraw	#crtanje po slici
import bz2			#kompresija/dekompresija
import xmlrpclib	#komunikacija sa serverom
import twitter 		#twitter API za python (TODO)
import base64		#jednostavno kodiranje
from msvcrt import getch	#za 'press any key'
import threading	#thread opcije

import neki program #za uzimanje funkcija iz drugih programa; poziv tih funkcija: program.funkcija (mora biti na istoj lokaciji kao i program koji ga poziva)

#Strings
str='Test'
     0123
	-4321
s[a:b]							#elementi liste/strina [a, b)
s[1:3]==es
s[:3]==Tes
s[-2:]==st
s[:-3]==T
s[a:b:c]						#od a, do b (ne uklj), sa skokovima od c


string = 'tekst'
string1 + string2					#konkatenacija (cat)
s.lower()
s.upper()			  				
string.find(string) 				#podskup trazi
sring.replace(staro, novo)
string.split(delimiter)				#razbi string u listu, odvojeni za delimiter (default je razmak)
									#'hello there world' postaje [hello, there, world]; uzima i punktuaciju
#lists
list = []
list.append(element koji dodajemo)
list.sort()
list.reverse()
list.insert(index, element)			#ubaci element na to mjesto, a sve ostale pomakne udesno
list.remove(elem)					#izbaci odredeni element, azurira polozaje ostalih
list1.extend(list2)					#listi 1 nadodaje sve elemente iz liste 2
list.index(elem)					#trazi element u listi i vraca njegov index

[num] * n							#stvara listu sa n elemenata i to svi num
[funkcija, elementi, uvijet]
[len(s) for s in list if s[0]!='d']	#vraca listu sa duljinom elemenata liste koji ne pocinju sa slovom 'd'; moguce ugnjeziditi jednu u drugu

#Files
f = open(filename, 'r')				#r, w, a, r+, wU, bw ... (r cita, w pise (brise sve napisano pri otvaranju), a dodaje na kraju)
for line in f  						#uzima red po red
list = f.readlines() 				#sve, vraca listu redova
string = f.read() 					#sve, stavlja u jedan veliki string
f.write(tekst {+ '\n'})
f.seek(n, m)						#pozicionira kazalo na mjesto za n pomaknuto u odnosu na m [m=0 za pocetak (default), 1 za trenutnu poziciju, 2 za kraj (n<0)]
f.tell()							#trenutna pozicija kazala u datoteci (int)
f.close()

#zip
zip = zipfile.ZipFile(open(ime, 'w/r/a'))
raw = zip.read('koji clan zipa')
zip.getinfo('file in zip').date_time/comments/file_size_compress_size)

#input/scanf
a = input('nesto usput ispise')			#uzima input, uzima int ili 'string' [potrebni '']
a = raw_input('za ispisat')				#sto god primi, sprema u string [ne treba stavljati '']
sys.argv[num]							#argumenti uzeti s terminala pri pozivu programa, 0 je sam program

#internet
file = urllib.urlopen(url)				#dalje kao file: read(), readlines()...
urllib2.urlopen('http://www.blabla.com')
urllib.urlretrive(url, dest)			#skida objekt sa url (jpg, gif, txt...) i sprema na dest

#server
server=xmlrpclib.ServerProxy(url)			#spaja se na server
print server.system.listMethods()			#ispisuje metode, tj. naredbe koje podrzava
print server.system.methodHelp(metoda)		#objasnjenje naredbe
print server.system.methodSignature(metoda)	#daje tip ulaza/izlaza

#dictionary
dict = {}							#inicijalizacija
dict['a'] = 'alpha'
dict.keys()							#vraca sve kljuceve rijecnika ['a']
dict.values()						#vraca sve asocirane vrijednosti rijecnika ['alpha']
dict.items()						#vraca tupleove povezanih [('a', 'alpha')]


#class
class Child (Parrent):				#stvara klasu Child, koja nasljeduje Parrent (sve metode i atribute)
 atribute = 'foo'					#mozemo listati atribute
 __hidden = 3						#skriveni atributi, ne mozemo im pristupiti izvana s self.__hidden; koristiti metode 
 def method(self, arg1, arg2 ...):	#stvara metodu, self obavezno prvi argument, dalje sukladno potrebi
 def __init__(self, arg1):			#prva metoda koja se poziva pri stvaranju objekta, konstruktor
 def __del__(self)					#destruktor
 def __cmp__(self, x)				#usporedba
 self.atribute						#pristup objektnoj varijabli
 Child.atribute						#pristup klasnoj varijabli, informacija koju svi imaju
 
Object = Child (arg)			#stvaranje novog objekta klase Child, inicijaliziran s arg (konstruktor se poziva)
Object.foo						#pristup atributu foo Objekta
Object.bar()					#poziv metode bar Objekta
hasattr(obj, name)				#ima li objekt ovakav atribut
getattr(obj, name)				#pribavlja vrijednost atibuta name
setattr(obj, name, value)		#postavlja
delattr(obj, name)				#brise
issubclass(sub, sup)			#je li A podklasa od B
isinstance(obj, class)			#je li obj instanca klase 



#trazilica
re.search(pattern, string)									#vraca 'pokazivac' na nadeni dio
match = re.search(r'(\w\d+\s)$@P(....\d\w\w)', D2345 $@Pg3ht5re)   #\w slovo-broj | \d broj | \s razmak | . bilo sto | ^ pocetak | $ kraj |
															#ako je . u [ ] onda je obicna tocka
															#sa () odjelimo u skupine
															#+ daje jednu ili vise, * daje 0 ili vise (?)
match.group() == D2345 $@Pg3ht5re
match.group(2) == g3ht5re									#ako je vise ( ), dati ce tuple-ove
	#primjer
nadeno = re.search(r'GET\s((.+).jpg)\s', line)				#od GET pa razmak do razmaka
daje -> GET /edu/languages/.../p-baab-bbaf.jpg

re.findall(r'sto trazimo', gdje trazimo) 	#da listu nalazaka
niz.split('po cemu')

#vrijeme
vrijeme=datetime.datetime.now()
vrijeme.ctime()							#vraca dan_u_tjednu mj dan hh:mm:ss yyyy'
vrijeme.strftime('%Y %d %b')			#yyyy dd m
time.sleep(vrijeme)						#stopiranje/pauziranje [u sec]

time()									#vraca vrijeme (float); za mjerenjetrajanja djela koda
(from time import time)				

#kalendar
calendar.isleap(year)					#vraca je li year prijestupna godina
calendar.leapdays(y1, y2)				#vraca broj prijestupnih dana/godina u intervalu [y1, y2]
calendar.weekday(year, month, day)		#vraca broj, koji dan u tjednu je bio navedenog datuma (0=pon, 6=ned)

#os
os.getpid()								#PID trenutnog procesa
os.kill(pid, sig)						#ubi proces
os.listdir(source)						#ispisuje sadrzaj datoteke
os.path.exists(dir)						#postoji li direktoriji, vraca True/False
os.path.join(dir, filename)				#spaja ime datoteke sa njenom lokacijom da bi se dobio path
os.mkdir(dest)							#stvori direktoriji naveden u dest, i.e novo u c:\\vid\tmp\novo
os.makedirs(path)						#rekurzivno radi sve potrebne direktorije da bi postigao path hijearhiju
os.rmdir(path)							#brise direktoriji, mora biti prazan
os.remove(path)							#brise datoteku
os.rename(old, new)
shutil.copy(source, dest)				#kopira datoteku, potreban import
os.system('naredba')					#pokrene naredbu na OS, tj windowsu (DIR, CD, CLS...)
										#naredbi dodati ako treba start/taskkill (!)
os.startfile(path)						#otvara kao u exploreru

#sys
sys.argv[]								#pozivanje argumenata danih pri pozivu funkcije sa konzole
sys.stdout								#preusmjeravanje standardnog izlaza e.g. .stdout = open(file, write)

#subprocess
proces = subprocess.Popen(path)			#otvara podproces
process.kill()/.terminate()				#gasi podproces
process.pid()							#pid	
process.send_signal(signal)				#SIGTERM = terminate
										
#zvuk
winsound.PlaySound("*", winsound.MB_OK)		#default windows zvuk

#slika
img=Image.open(source)					#otvara sliku
img.show()								#prikazuje sliku (?)
img.format / img.size / img.mode		#format, dimenzije, nacin rada (r, w, b...)
img.getbbox()							#vraca 4-clani tuple, sa dimenzijama (ljevo, gore, desno, dolje)
img.crop(dimenzije)						#prima 4-clani tuple sa koordinatama tocka za rezat
img.tostring()							#izvlaci podatke iz slike, red po red
img.getpixel(tuple)						#uzima pixel
img.putpixel(tuple, boja)				#stavlja pixel na lokaciju
nova = Image.new(mode, size)			#stvara novu sliku
img.save(dest\name, format)				#spremanje

#draw, crtanje
draw=ImageDraw.Draw(img)				#boje: 128=crveno;
draw.Polygon(coords, outline=x, fill=y)	#spaja sve tocke dane po kordinatama, crta je boje x, ispunjeno bojom y
draw.line(coords, fill=x, width=y)		#spaja dvije tocke crtom boje x sirine y


#twitter
api = twitter.Api()
statusi = api.GetUserTimeline(user)		#user je ili ime ili ID
user = api.getuser(user)
status.gettext()

#base64
base64.b64encode(String)			#vraca string zakodiranog podatka
base64.b64decode(String)			#odkodira

#thread
thread = threading.Thread(target=loop1_10, name='name', arg=(a1, a2, a3...));  #stvori thread naziva 'name' koji ce 
thread.start()						#pokrene thread, zapocet ce pozivajuci target funckciku, s arg parametrima
thread.join()						#ceka da thread zavrsi/terminira
thread.isAlive()					#da li je thread jos aktivan/izvrsavajuc


#inspekcija objekta
[method_name for method_name in dir(object) if callable(getattr(object, method_name))]
									#prikazi sve metode unutar object


#misc
+=, -=, *=, /=, ** {potencija}, >=, ==, !=
uvjeti: or, and, not
break, continue, in,

set(lista1) ^/&/| set(lista2)			#za dobivanje liste (bez duplikata) s odredenim elementima, ovisno o pojavljivanju
										#& - AND; | - OR; ^ - XOR
print = "%d little pigs come out or I'll %s" % (3, 'blow down')	# koristenje % operatora
bool(x)									#daje sud, vraca ili True ili False
sum(list)								#vraca sumu elemenata liste
map(funktion, list)						#obavi funkciju nad svakim elementom liste
isinstance(objekt, vrsta) 				#daje sud oko toga jeli objekt te vrste (list, str, int, float...)
range(len(string))
list(set(list_with)duplicates)			#vraca listu koja sadrzi sve elemente originalne liste, no bez duplikata
3 ** 3 == 27 # 3^3
int('9')==9
chr(105)=='i'
chr(80)=='P'
ord('a') == 97
str(250)=='250'
( 'str', 5, 'C') 						#tuple, ntorka; ne izmjenjivo (a[2] = a[2] + 1) -> error

#pickle ??? kodiranje?

from msvcrt import getch				#izvuce funkciju getch()
getch()									#za 'press any key' funkciju
getche()								#isto, samo sto ujedno ispise tipku na konzolu (ako je pritisnut ispisljiv znak)
kbhit()									#vraca bool ceka li se na pritisak tipke


def main():
  funkcija(sys.argv[1])

if __name__ == '__main__':				za system start
  main()


from random import *
def obtenirFaceSigne(lancer):
	valeur=list()
	if lancer>=0:valeur.append(0)
	elif lancer<0:valeur.append(1)
	return valeur

def obtenirFacesDes(lancer):
	valeur=[0]*8
	for face in range(8):valeur[7-face]=lancer%2;lancer=lancer//2
	return valeur

def obtenirPointsDes(faces):
	valeur=0
	for face in range(8):valeur+=faces[face]*2**(7-face)
	return valeur

def de2FormatDeJeu(lancer):
	faceSigne=obtenirFaceSigne(lancer)
	if lancer<0:lancer*=-1
	valeur=-126
	while not 2**valeur<=lancer<2**(valeur+1):valeur+=1
	compteur=valeur+127;compteurBin=obtenirFacesDes(compteur);ratio=lancer/2**valeur;jeton=ratio-1;score=[0]*23
	for i in range(23):
		resultat=int();niveau=-(i+1)
		if round(jeton,5)==0:resultat=0
		if jeton-2**niveau>=0:jeton-=2**niveau;resultat=1
		else:resultat=0
		score[i]=resultat
	return [faceSigne,compteurBin,score]

def formatDeJeu2de(scoreFormatDeJeu):
	valeur=scoreFormatDeJeu;faceSigne=valeur[0];compteur=valeur[1];jeton=valeur[2];signe=int()
	if faceSigne==[0]:signe=1
	elif faceSigne==[1]:signe=-1
	niveau=obtenirPointsDes(compteur);niveauReel=niveau-127;total=0
	for i in range(23):resultat=-(i+1);total+=jeton[i]*2**resultat
	bonus=1+total;scoreFinal=signe*2**niveauReel*bonus;return round(scoreFinal,5)

def afficherFormatDeJeu(scoreFormatDeJeu):
	valeur=scoreFormatDeJeu;signe=str(valeur[0][0]);compteur=valeur[1];jeton=valeur[2];compteurStr=str()
	for resultat in compteur:compteurStr+=str(resultat)
	jetonStr=str()
	for resultat in jeton:jetonStr+=str(resultat)
	print(signe+' '+compteurStr+' '+jetonStr)

def formatageDesFormatDeJeu(chaine):
	valeur=chaine;valeur=valeur.replace(' ','');print(valeur);signe=[int(valeur[0])];compteur=valeur[1:9];listeCompteur=list()
	for resultat in compteur:listeCompteur.append(int(resultat))
	jeton=valeur[9:33];listeJeton=list()
	for resultat in jeton:listeJeton.append(int(resultat))
	return [signe,listeCompteur,listeJeton]
def playDice() : 
	while 1:
		commande=str(input('[de]>> '));commande=commande.split(' ')
		if commande[0]=='0':break
		elif commande[0]=='ieee':lancer=float(commande[1]);afficherFormatDeJeu(de2FormatDeJeu(lancer))
		elif commande[0]=='dec':scoreFormatDeJeu=formatageDesFormatDeJeu(commande[1]);lancer=formatDeJeu2de(scoreFormatDeJeu);print(lancer)
def main() : 
	while 1 : 
		command = str(input("[de]> "))
		if command == "754" : playDice()
		n = int(command)
		print("Valeur aléatoire : " + str(randint(1,n)))
main()


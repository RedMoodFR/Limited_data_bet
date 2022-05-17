# -*- coding: utf-8 -*-
"""
Created on Tue May 17 01:05:52 2022

@author: guill
"""

from random import random
from random import randint

class experience :
    def __init__(self) :
        self.resultats = {'piles' : 0, 'faces' : 0}
        if random() >= 0.5 :
            self.character = 'tricheur'
            self.chance = 0.75
        else :
            self.character = 'normal'
            self.chance = 0.5
            
    def lancer(self, n) :
        for i in range(n) :
            if random() >= self.chance :
                self.resultats['faces'] += 1
            else :
                self.resultats['piles'] += 1

class Partie :
    def __init__(self) :
        self.score = 0
        self.points = 100
        self.resultats = {'tricheurs' : {'justes' : 0, 'faux' : 0}, 'normaux' : {'justes' : 0, 'faux' : 0}}
        self.faux = 0
        self.justes = 0
        self.experience = experience()
        self.etat = 'en cours'
        self.lancers = 0
        self.paris = 0
        self.lancers_partie = 0
        self.lancers_moyens = 0
        self.n_experiences = 1
    
    def feedback_partie(self) :
        print('Tricheurs : Justes :', self.resultats['tricheurs']['justes'], 'Faux :', self.resultats['tricheurs']['faux'])
        print('Normaux : Justes :', self.resultats['normaux']['justes'], 'Faux :', self.resultats['normaux']['faux'])
        print('\n-----------\n')
        print('Piles :', self.experience.resultats['piles'])
        print('Faces :', self.experience.resultats['faces'])
        print('Points :', self.points)
    
    def action(self, action) :
        if action == 1 :
            if self.points < 1 :
                return False
            self.experience.lancer(1)
            self.points -= 1
            self.lancers += 1
            self.lancers_partie += 1
            if self.points <= 0 :
                self.etat = 'choix forcé'
            return
        elif action == 2 :
            if self.points < 5 :
                return False
            self.experience.lancer(5)
            self.points -= 5
            self.lancers += 5
            self.lancers_partie += 5
            if self.points <= 0 :
                self.etat = 'choix forcé'
            return
        elif action == 3 :
            self.paris += 1
            if self.experience.character == 'normal' :
                self.score += 1
                self.resultats['normaux']['justes'] += 1
                self.points += 15
                self.justes += 1
            else :
                self.faux += 1
                self.resultats['normaux']['faux'] += 1
                self.points -= 30
                if self.points <= 0 :
                    self.etat = 'finie'
            self.experience = experience()
        elif action == 4 :
            self.paris += 1
            if self.experience.character == 'tricheur' :
                self.score += 1
                self.resultats['tricheurs']['justes'] += 1
                self.points += 15
                self.justes += 1
            else :
                self.faux += 1
                self.resultats['tricheurs']['faux'] += 1
                self.points -= 30
                if self.points <= 0 :
                    self.etat = 'finie'
            self.lancers_moyens = (self.lancers_moyens * (self.n_experiences-1) + self.lancers_partie)/self.n_experiences
            if self.etat != 'finie' :
                self.experience = experience()
                self.n_experiences += 1
                self.lancers_partie = 0
    
    def save_partie(self, joueur = "anonyme") :
        with open('scoreboard.csv', 'a') as f :
            f.write(joueur+';'+str(self.points)+';'+str(self.lancers)+';'+str(self.paris)+';'+str(self.justes)+';'+str(self.faux)+';'+\
                    str(self.resultats['tricheurs']['justes'])+';'+str(self.resultats['tricheurs']['faux'])+';'+\
                    str(self.resultats['normaux']['justes'])+';'+str(self.resultats['normaux']['faux'])+'\n')
        
        

def jeu() :
    partie = Partie()
    partie.feedback_partie()
    while partie.etat != 'finie':
        while True :
            action =  input('Action : ')
            if action not in ['1','2','3','4'] :
                print('action doit être égal à 1, 2, 3 ou 4')
                continue
            action = int(action)
            if partie.etat == 'choix forcé' and action in [1,2] :
                print('pas assez de points')
                continue
            partie.action(action)
            break
        partie.feedback_partie()
    partie.feedback_partie()
    return partie
    
def reset_scoreboard() :
    with open('scoreboard.csv', 'w') as f :
        f.write("Pseudo;Points;Lancers;Paris;Justes;Faux;Tricheur justes;Tricheurs faux;Normaux justes;Normaux faux\n")    
    
def crazy_monkey(n_parties) :
    best_score = 0
    for i in range(n_parties) :
        partie = Partie()
        while partie.etat != 'finie':
            if partie.etat != 'choix forcé' :  
                action =  randint(1,4)
            else :
                action =  randint(3,4)
            partie.action(action)
        partie.save_partie("CrazyMonkey1")
        if partie.justes > best_score :
            best_score = partie.justes
        print(i+1)
    print(best_score)
    
def crazy_monkey2(n_parties) :
    best_score = 0
    for i in range(n_parties) :
        partie = Partie()
        while partie.etat != 'finie':
            action =  randint(3,4)
            partie.action(action)
        partie.save_partie("CrazyMonkey2")
        if partie.justes > best_score :
            best_score = partie.justes
        print(i+1)
    print(best_score)
        
def statistician1(n_parties) :
    for i in range(n_parties) :
        partie = Partie()
        while partie.etat != 'finie':
            #PRISE DE DECISION
            action = 0
            if partie.etat == 'choix forcé' and action in [1,2] :
                print('pas assez de points')
                continue
            partie.action(action)
            break

def input_n_parties() :
    while True :
        a = input("Nombre de parties : ")
        try :
            a = int(a)
        except :
            print("VOUS DEVEZ ENTRER UN NOMBRE")
            continue
        if a < 0 :
            print("NOMBRE DE PARTIES NEGATIF")
            continue
        if a == 0 :
            print ("NOMBRE DE PARTIES NUL")
            continue
        return a

while True :
    choix = input("""
        Choisissez une option :
        1- Jouer soi-même
        2- CrazyMonkey 1 (full aléatoire)
        3- CrazyMonkey 2 (paris aléatoire sans lancer)
        4- Quitter
        Votre choix : """)
    if choix == '1' :
        jeu()
        continue
    if choix == '2' :
        crazy_monkey(input_n_parties())
    if choix == '3' :
        crazy_monkey2(input_n_parties())
        continue
    if choix == '4' :
        break

            
        
        
    
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
        self.juste = 0
        self.experience = experience()
        self.etat = 'en cours'
        self.pieces_lancées = 0
        self.paris = 0
    
    def feedback_partie(self) :
        print('Tricheurs : Justes :', self.resultats['tricheurs']['justes'], 'Faux :', self.resultats['tricheurs']['faux'])
        print('Normaux : Justes :', self.resultats['normaux']['justes'], 'Faux :', self.resultats['normaux']['faux'])
        print('\n-----------\n')
        print('Piles :', self.experience.resultats['piles'])
        print('Faces :', self.experience.resultats['faces'])
        print('Points :', self.points)
    
    def action(self, action) :
        if action == 1 :
            self.experience.lancer(1)
            self.points -= 1
            self.pieces_lancées += 1
            if self.points <= 0 :
                self.etat = 'choix forcé'
            return
        elif action == 2 :
            self.experience.lancer(5)
            self.points -= 5
            self.pieces_lancées += 5
            if self.points <= 0 :
                self.etat = 'choix forcé'
            return
        elif action == 3 :
            self.paris += 1
            if self.experience.character == 'normal' :
                self.score += 1
                self.resultats['normaux']['justes'] += 1
                self.points += 15
                self.juste += 1
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
                self.juste += 1
            else :
                self.faux += 1
                self.resultats['tricheurs']['faux'] += 1
                self.points -= 30
                if self.points <= 0 :
                    self.etat = 'finie'
            self.experience = experience()
    
    def save_partie(self, joueur = "anonyme") :
        True
        
        

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
        f.write("Pseudo;Points;Pièces lancées;Paris;Justes;Faux;Tricheur justes;Tricheurs faux;Normaux justes;Normaux faux\n")    
    
def crazy_monkey() :
    for i in range(10000) :
        partie = Partie()
        while partie.etat != 'finie':
            while True :
                action =  randint(1,4)
                action = int(action)
                if partie.etat == 'choix forcé' and action in [1,2] :
                    print('pas assez de points')
                    continue
                partie.action(action)
                break
        print(i+1)
jeu()
input()

            
        
        
    
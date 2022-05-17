# Limited_data_bet
 A python version of the game proposed by [Primer](https://www.youtube.com/watch?v=QC91Bf8hQVo&t=268s).
 
 For now my version of the game is in french, but i will implement english.
 
 Rules of the game :
 - You will realise a serie of experiments;
 - In each experiment, a character will flip coins;
 - Half of them are 'cheaters' : they will flip head 75% of the time;
 - Half of them are 'regular' : they will flip head 50% of the time;
 - You can ask them to flip 1 or 5 coins multiple times;
 - Flipping a coin cost you 1 point;
 - You start with 100 points;
 - If you guess right you win 15 points;
 - If you guess wrong you loose 30 points;
 - Guessing ends the experiment;
 - If your score is equal or under zero at the end of an experiment, the game is over.

Commands for the player on my version :
- Flipping 1 coin : '1'
- Flipping 5 coins : '2'
- Betting 'regular' : '3'
- Betting 'cheater' : '4'

The reason I duplicated the game on python is to try different strategies of decision taking using bots :
 - CrazyMonkey1 : will choose 1 of the 4 options randomly (IMPLEMENTED).
 - CrazyMonkey2 : will only bet randomly without flipping coins (IMPLEMENTED).
 - Statistician1 : will bet if his expectation of win/loss based on the poisson probability of the character to be a cheater is positive (NOT IMPLEMENTED).
 - Statistician2 : will bet if his expectation of win/loss based on the poisson probability of the character to be regular is positive (NOT IMPLEMENTED).
 - Statistician3 : will bet if his expectation of win/loss based on the poisson probability of the character to be a cheater AND on the propability of the character to be regular is positive (NOT IMPLEMENTED).
 - Bayesians : will take decision in similar conditions than statisticians but based on bayesian's probabilites (NOT IMPLEMENTED).
 - Learner : A machine learning agent which have to choose between the four actions possible. reward based on points and on succes (NOT IMPLEMENTED).
 - Manager : A machine learning agent which have to choose which agent will take the decision between those above. reward based on points and on succes (NOT IMPLEMENTED).
 - DemocraticVote : A group of different agents take their decision. The decision that is the most taken is one the that is chosen (NOT IMPLEMENTED).

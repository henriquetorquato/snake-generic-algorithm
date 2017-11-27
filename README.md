# Snake's Generic Algorithm #

> This is an unfinished project, there are still some improvements to be made for it to be considered finished.

## What is this? ##

This is a [generic algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm) aproach, or a attempt at one, to make a bot that plays [Snake's](https://en.wikipedia.org/wiki/Snake_(video_game)).

Generich algorithms are based on the process of natural selection from Charles Darwin, it uses mechanics like: `generations`, `reproduction` and `survival of the strongest` to mimic a evolution scenario.

In this project, each entity (snake) has a chromosome, which represent the combination of moves that it will perform when it is being tested. Within a time limit, these entities perform these movements in an attempt to catch food (apples), and his chromosome is scored based in his performance or "survivability".

These entities are grouped in the form of generations. Each generation has an index, corresponding to the amount of iterations that its population has already undergone. At the end of each generation, entities are organized based on the score of it's chromosome, and each one passes a test based on how much it "survived". In this process the weaker entities are killed, thus destroying the less efficient chromosome, and the chromosome of the surviving entities undergo a mutation process, becoming more or less efficient is surviving.

Treating the scenario this way, there is an expectation that in some generations, the entity will begin to "understand" that its goal and pick up food, which is the same goal of the Snake's game.

> I am not a specialist in the field, I created this project based on my understanding on the subject. Any suggestion, objection or complaint about the way it was made, be sure to issue on it.

## To-do ##

 - [ ] Remake timespam of testing
 - [ ] Remake new chromosomes generation
 - [ ] Implement the body of the snake
 - [ ] Implement better evaluation of survivability
 - [ ] Change configurations to a ".ini" file (ConfigParser)
 - [ ] Remake snake change of direction
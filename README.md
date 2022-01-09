# finalOPPtask - Pokemon game

Name : Tal Ornan ID: 209349356<br />
Name : Tzach Itshak Ofir ID: 208062943<br />


![pokemon-1591427_1920](https://user-images.githubusercontent.com/76403961/148697885-be26bf80-4612-46c3-9d91-225fc1206909.jpg)

### ****To implement the game we use our implemtion of directed weight graph we did in OPPTask4. You can find the algo explantion in the WIKI.****
 
#### *****To implement the game we did a few classes.*****

1.GameController - get the GameView and the GameModle and use them both to impement the game.<br /> 
2.GameInfo - get all the info of the game by the client and put on an object.<br />
3.GameModle- the algo of the game , the best way to choose that pokamon need to eat to get the biggest num of pokamon .<br />
4.GameView - the Gui implemntion of the game.<br />
5.Agent - class represent an agent from client and make Agent object.<br />
6. Pokamon -class represent an Pokamon from client and make Pokamon object.<br />

#### ****GameModle:****
**Fields:**<br />
This class contains the model of the game. it conains the business logic of the class - 
        The logic of the game. in the class the main algorithem is implementes. the target of this class in to maximize
        the grade of all the agents.
        The  Algorithm contains three main parts:
            1. init - we are init each agent in closest as possible to the most valuable pokemons. in order to do so,
            Merging is executeed over the pokemons object(the value fielst), and agent is assign using to the closet node.
            2.  Algorithm -
                1. check if there are agent that already on the way of eating pokemons, if so, we should ignore those agents, and those pokemons
                2. we are using the closet path  Algorithm, between each agent and pokemons.
                3. if we are close(decided on 1 edges) to a pokemon - we are assign the the agent to this pokemon.
                4. take all the unassign pokemons are sort them by thier value.
                5. take the dikstra of each agent and divide by the speed - we want to send the first agent(ascnding order)
                6. run this algorithem over and over until the game is ending.
            3. for all pokemons that are "on the way on the agent, add them to the assign pokemons list
        this class is in use in order to simplify the the use in the json that return from the client


**Functions:**<br />
runAndUpdate - run the algorithem and update the server
init_game - init each agent as close as possible to the node.
gameAlgo - the main algorithm - 
        The  Algorithm contains three main parts:
            1. init - we are init each agent in closest as possible to the most valuable pokemons. in order to do so,
            Merging is executeed over the pokemons object(the value fielst), and agent is assign using to the closet node.
            2.  Algorithm -
                1. check if there are agent that already on the way of eating pokemons, if so, we should ignore those agents, and those pokemons
                2. we are using the closet path  Algorithm, between each agent and pokemons.
                3. if we are close(decided on 1 edges) to a pokemon - we are assign the the agent to this pokemon.
                4. take all the unassign pokemons are sort them by thier value.
                5. take the dikstra of each agent and divide by the speed - we want to send the first agent(ascnding order)
                6. run this algorithem over and over until the game is ending.
            3. for all pokemons that are "on the way on the agent, add them to the assign pokemons list




#### ****Agent:****
**Fields:**<br />
this class simply present a agent. its wrapper to the json the return from the client "get agents"



**Functions:**<br />
 



#### ****Pokamon:****
**Fields:**<br />

this class simply present a pokemons. its wrapper to the json the return from the client "get pokemons"


**Functions:**<br />



#### ****GameInfo:****
**Fields:**<br />
this class simply present a game info. its wrapper to the json the return from the client "get pokemons"



**Functions:**<br />

#### ****GameController:****
**Fields:**<br />
the contoller of the game, contains the view and model of the game, and is part of the mvs design pattern.
it's responsible for running the algorithem and run the ui logic.



**Functions:**<br />

execute_game - simple run the algorithem and update the ui accornly 


#### ****GameView:****
**Fields:**<br />
The view of the function, contains the GUI logics of the game.
it create the gui objects and update them every few milisceonds.
the gui is scalable, and contains the following data:
1. node
2. edges
3. agent - brown clor
4. pokemon - yello for "up" and blue for "down"
5. quit button - for quiting the game
6. 6. titels - how long till the game is ending, number of points. amd moves


**Functions:**<br />
scale - scale the screen 
show_agents show the agents 
show_nodes - show the nodes.
show_edges - show the edges
show_pokemons - show the pokemons
show_info - shoe info in the upper left corner
button - show the button 
show_all - run all the above and update the screen after changes.






### ****Gui screenShoot:****
![WhatsApp Image 2022-01-09 at 21 52 55](https://user-images.githubusercontent.com/76403961/148698947-329d197e-e69e-4238-8b19-52b0622918b1.jpeg)

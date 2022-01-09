# finalOPPtask - Pokemon game

Name : Tal Ornan ID: 209349356<br />
Name : Tzach Itshak Ofir ID: 208062943<br />


![pokemon-1591427_1920](https://user-images.githubusercontent.com/76403961/148697885-be26bf80-4612-46c3-9d91-225fc1206909.jpg)

### ****Video of the GUI****
https://user-images.githubusercontent.com/76403961/148702089-23f19796-e58b-4192-90f5-934c8ff859b2.mp4

### ****To implement the game we use our implemtion of directed weight graph we did in OPPTask4. You can find the algo explantion in the WIKI.****
 
#### *****To implement the game we did a few classes.*****

##### ****GameModle:****
This class contains the model of the game. it conains the business logic of the class - 
        The logic of the game. in the class the main algorithem is implementes. the target of this class in to maximize
        the grade of all the agents.
        The  Algorithm contains three main parts:
            1. init - we are init each agent in closest as possible to the most valuable pokemons. in order to do so,
            Merging is executeed over the pokemons object(the value fielst), and agent is assign using to the closet node.<br />
            2.  Algorithm -<br />
                1. check if there are agent that already on the way of eating pokemons, if so, we should ignore those agents, and those pokemons<br />
                2. we are using the closet path  Algorithm, between each agent and pokemons.<br />
                3. if we are close(decided on 1 edges) to a pokemon - we are assign the the agent to this pokemon.<br />
                4. take all the unassign pokemons are sort them by thier value.<br />
                5. take the dikstra of each agent and divide by the speed - we want to send the first agent(ascnding order)<br />
                6. run this algorithem over and over until the game is ending.<br />
            3. for all pokemons that are "on the way on the agent, add them to the assign pokemons list
        this class is in use in order to simplify the the use in the json that return from the client


**Functions:**<br />
runAndUpdate - run the algorithem and update the server
init_game - init each agent as close as possible to the node.
gameAlgo - the main algorithm - 
        The  Algorithm contains three main parts:
            1. init - we are init each agent in closest as possible to the most valuable pokemons. in order to do so,
            Merging is executeed over the pokemons object(the value fielst), and agent is assign using to the closet node.<br />
            2.  Algorithm -<br />
                1. check if there are agent that already on the way of eating pokemons, if so, we should ignore those agents, and those pokemons<br />
                2. we are using the closet path  Algorithm, between each agent and pokemons.<br />
                3. if we are close(decided on 1 edges) to a pokemon - we are assign the the agent to this pokemon.<br />
                4. take all the unassign pokemons are sort them by thier value.<br />
                5. take the dikstra of each agent and divide by the speed - we want to send the first agent(ascnding order)<br />
                6. run this algorithem over and over until the game is ending.<br />
            3. for all pokemons that are "on the way on the agent, add them to the assign pokemons list<br />


#### ****Pokamon:**** 
this class simply present a pokemons. its wrapper to the json the return from the client "get pokemons"

#### ****GameInfo:****
this class simply present a game info. its wrapper to the json the return from the client "get pokemons"

#### ****GameController:****
the contoller of the game, contains the view and model of the game, and is part of the mvs design pattern.
it's responsible for running the algorithem and run the ui logic.

**Functions:**<br />

execute_game - simple run the algorithem and update the ui accornly 


#### ****GameView:****
The view of the function, contains the GUI logics of the game.
it create the gui objects and update them every few milisceonds.
the gui is scalable, and contains the following data:<br />
1. node<br />
2. edges<br />
3. agent - brown clor<br />
4. pokemon - yello for "up" and blue for "down"<br />
5. quit button - for quiting the game<br />
6. 6. titels - how long till the game is ending, number of points. amd moves<br />


**Functions:**<br />
1.scale - scale the screen <br />
2.show_agents show the agents<br /> 
3.show_nodes - show the nodes.<br />
4.show_edges - show the edges<br />
5.show_pokemons - show the pokemons<br />
6.show_info - shoe info in the upper left corner<br />
7.button - show the button <br />
8.show_all - run all the above and update the screen after changes.<br />

### ****Gui screenShoot:****

![WhatsApp Image 2022-01-09 at 23 14 25 (1)](https://user-images.githubusercontent.com/76403961/148701856-8d1e608a-d696-42a7-9c7d-1097c8da2455.jpeg)



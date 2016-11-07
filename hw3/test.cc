#include "mdp-simulation.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <map>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <time.h>
using namespace std;

void getPolicy(vector<vector<float> > &Q);
int main (void)
{
  srand(time(NULL));
  int rowSize = MAX_GRID*MAX_GRID;
  int columnSize = 4;
  int numEpisodes = 100000;
  float alpha = 0.5;
  float gamma = 0.9;
  float epsilon = 1.0;
  int currentGrid, nextGrid;
  Action action;

  vector<vector<float> > Q(rowSize, vector<float>(columnSize));
  vector<vector<int> > num_visited(rowSize, vector<int>(columnSize)); //for computing alpha

  ofstream myFile;
  myFile.open("rewards.txt");

  for(int i=0; i<numEpisodes; i++)
  {
  	State initialState = State(rand() % 10,rand() % 10);
  	
  	int steps = 0;
  	int totalReward = 0;
  	epsilon = 1.0*(numEpisodes - i)/numEpisodes;
  	double E = 0.0;

  	while(steps<100)
  	{
  		State currentState = initialState;
  		currentGrid = currentState.x * MAX_GRID + currentState.y;
  		
  		E = (double)rand()/(double)RAND_MAX;
  		if(E<epsilon)
  			action = static_cast<Action>(rand()%4);
  		else
  			action = Action(max_element(Q[currentGrid].begin(), Q[currentGrid].end())-Q[currentGrid].begin());
  		
  		alpha = 1.0/(1+(num_visited[currentGrid][action]));
  		totalReward = totalReward + my_reward(currentState);

  		State nextState = my_next_state(currentState, action);  		
  		nextGrid = nextState.x * MAX_GRID + nextState.y;
  		
  		Q[currentGrid][action]= (1-alpha)*Q[currentGrid][action] + alpha*(my_reward(currentState) + gamma*(*max_element(Q[nextGrid].begin(), Q[nextGrid].end())));
  		
  		num_visited[currentGrid][action] ++; //to keep a count of how many times the cell has been visited
  		initialState = nextState;
  		steps++; 		
    }
    myFile<<totalReward<<"\n";
  }
 //To print Q matrix, uncomment this:

 /*for(int m=0;m<rowSize;m++)
  {
  	for(int n=0;n<columnSize;n++)
  		cout << Q[m][n]<< ' ';
  	cout<< "\n";
  }*/
  myFile.close();
  vector<int> bestAction(rowSize);
  vector<vector<int> > Policy(MAX_GRID, vector<int>(MAX_GRID));
  for(int i=0; i<rowSize; i++){
  	bestAction[i] = max_element(Q[i].begin(), Q[i].end())-Q[i].begin();
  	int x = (i)/10;
  	int y = (i)%10;
  	Policy[x][y] = bestAction[i];
    }
    
  	for(int p=0;p<MAX_GRID;p++)
  	{
  		for(int q = 0;q<MAX_GRID;q++){
  			if(Policy[p][q]==0)
  				Policy[p][q]= 'N';
  			else if(Policy[p][q]==1)
  				Policy[p][q]='S';
  			else if(Policy[p][q]==2)
  				Policy[p][q]='E';	
  			else
  				Policy[p][q]='W';
  		}
  	}

  	for(int m=0;m<MAX_GRID;m++)
  	{
  		for(int n = 0;n<MAX_GRID;n++)
   		{
   			printf(" %c",Policy[m][n]);
   			cout<<" ";
   		}	
  		cout <<"\n ";
  	}
   return 0;
}

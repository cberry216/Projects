/*
 * The backend of Minesweeper application. Handles the memory of where the mines are located, where the player has guessed,
 * etc.
 * 
 * Works in tandem with the visual driver.
 * 
 * by Christopher Berry
 */

public class MineManager {
	
	private final int CONTINUE = -1;	//condition: game is not over
	private final int LOSER = 0;		//condition: game is over, player lost
	private final int WINNER = 1;		//condition: game is over, player won

	private int x;						//X-dimension of grid
	private int y;						//Y-dimension of grid
	private int mines;					//number of mines in field
	private int spaces;					//number of non-mine spaces in field, used to tell if game is over
	private boolean[][] mineField;		//boolean grid, true indicates there is a mine there
	private boolean[][] guessField;		//boolean grid, true indicates the player has guessed there
	private boolean endGame = false;	//true if game is over

	/**
	 * constructs a default MineManger with dimensions 10,10 with 50 mines.
	 */
	public MineManager() {
		x = 10;
		y = 10;
		mines = 50;
		spaces = (x * y) - mines;
		mineField = new boolean[x][y];
		guessField = new boolean[x][y];
		initField();
	}
	
	/**
	 * constructs a MineManager with given parameters.
	 * 
	 * @param x, x-dim of minefield
	 * @param y, y-dim of minefield
	 * @param mines, number of mines in minefield
	 */
	public MineManager(int x, int y, int mines){
		this.x = x;
		this.y = y;
		this.mines = mines;
		spaces = (this.x * this.y) - this.mines;
		mineField = new boolean[this.x][this.y];
		guessField = new boolean[this.x][this.y];
		initField();
	}
	
	/**
	 * Initializes the minefield with mines placed randomly throughout the board.
	 */
	public void initField(){
		int placedMines = 0;
		while(placedMines < mines){
			int randX = (int)(Math.random() * x);
			int randY = (int)(Math.random() * y);
			if(mineField[randX][randY] == false){
				mineField[randX][randY] = true;
				placedMines++;
			}
		}
	}
	
	/**
	 * makes the guess field value at position (x,y) true and if the position
	 * is a mine the game is over, else it decreases the number of free spaces 
	 * by 1. It then makes a recursive call.
	 * 
	 * @param x x-coordinate to guess
	 * @param y y-coordinate to guess
	 * @return int, the number of adjacent mines
	 * @throws OutOfBoardException if the guess lies outside the confines of the board
	 * @throws PreviouslyGuessedException is the guess has already been guessed
	 */
	public int makeGuess(int x, int y){
		try{
			if(x >= this.x || y >= this.y 
					|| x < 0 || y < 0)
				throw new OutOfBoardException(x, y);
			if(guessField[x][y])
				throw new PreviouslyGuessedException(x, y);
			if(mineField[x][y] == true)
				endGame = true;
			else{
				spaces--;
			}
			guessField[x][y] = true;
			makeGuessRec(x,y);
		}
		catch(OutOfBoardException e){
			e.reportError();
		}
		catch(PreviouslyGuessedException e){
			e.reportError();
		}
		catch(Exception e){
			e.printStackTrace();
		}
		return(getAdjacentMines(x, y));
	}
	
	/**
	 * Is passed coordinates from {@link MineManager#makeGuess(int, int)} and recursively
	 * guess all positions around the position if the number of adjacent mines is 0.
	 * If the number of adjacent mines is 0, all 8 positions around the current position
	 * are guess if the position has not already been guessed.
	 * 
	 * @param x x-pos of guess
	 * @param y y-pos of guess
	 */
	public void makeGuessRec(int x, int y){
		if(getAdjacentMines(x, y) == 0){
			if(x > 0 && y > 0 && !guessField[x-1][y-1])
				makeGuess(x-1, y-1);
			if(y > 0 && !guessField[x][y-1])
				makeGuess(x, y-1);
			if(x < this.x-1 && y > 0 && !guessField[x+1][y-1])
				makeGuess(x+1, y-1);
			if(x > 0 && !guessField[x-1][y])
				makeGuess(x-1, y);
			if(x < this.x-1 && !guessField[x+1][y])
				makeGuess(x+1,y);
			if(x > 0 && y < this.y-1 && !guessField[x-1][y+1])
				makeGuess(x-1, y+1);
			if(y < this.y-1 && !guessField[x][y+1])
				makeGuess(x, y+1);
			if(x < this.x-1 && y < this.y-1 && !guessField[x+1][y+1])
				makeGuess(x+1, y+1);
		}
	}
	
	/**
	 * checks if game is over.
	 * 
	 * @return int, {@link MineManager#LOSER} if the game is over and there are greater than 0 spaces left.
	 * 			int, {@link MineManager#WINNER} if the number of spaces left is 0.
	 * 			int, {@link MineManager#CONTINUE} if the game is not over and there are spaces left to guess.
	 */
	public int checkGameOver(){
		if(endGame == true && spaces > 0)
			return LOSER;
		else if(spaces == 0)
			return WINNER;
		else
			return CONTINUE;
		
	}
	
	/**
	 * gets the number of adjacent mines to a current position.
	 * 
	 * @param x x-pos of current position
	 * @param y y-pos of current position
	 * @return int, the number of mines surrounding the current position (including corners)
	 * @throws ArrayIndexOutOfBoundsException if the positions lies outside of the board
	 */
	public int getAdjacentMines(int x, int y){
		int adjMines = 0;
		try{
			if(mineField[x-1][y-1])
				adjMines++;
		}
		catch(ArrayIndexOutOfBoundsException e){}
		try{
			if(mineField[x][y-1])
				adjMines++;
		}
		catch(ArrayIndexOutOfBoundsException e){}
		try{
			if(mineField[x+1][y-1])
				adjMines++;
		}
		catch(ArrayIndexOutOfBoundsException e){}
		try{
			if(mineField[x-1][y])
				adjMines++;
		}
		catch(ArrayIndexOutOfBoundsException e){}
		try{
			if(mineField[x+1][y])
				adjMines++;
		}
		catch(ArrayIndexOutOfBoundsException e){}
		try{
			if(mineField[x-1][y+1])
				adjMines++;
		}
		catch(ArrayIndexOutOfBoundsException e){}
		try{
			if(mineField[x][y+1])
				adjMines++;
		}
		catch(ArrayIndexOutOfBoundsException e){}
		try{
			if(mineField[x+1][y+1])
				adjMines++;
		}
		catch(ArrayIndexOutOfBoundsException e){}
		
		return adjMines;
	}
	
	/**
	 * gets the guess field.
	 * 
	 * @return boolean[][], the boolean array of guesses
	 */
	public boolean[][] getGuessField(){
		return guessField;
	}
	
	/**
	 * gets the mine field.
	 * 
	 * @return boolean[][], the boolean array of mines
	 */
	public boolean[][] getMineField(){
		return mineField;
	}

	/**
	 * gets the x-dimension of board.
	 * 
	 * @return int, x-dim of board
	 */
	public int getX(){
		return x;
	}
	
	/**
	 * gets the y-dimension of board.
	 * 
	 * @return int, y-dim of board.
	 */
	public int getY(){
		return y;
	}
	
	/**
	 * moves the mine from the current position to a random position given that the random
	 * position does not contain a mine.
	 * 
	 * @param x x-coord of current position
	 * @param y y-coord of current position
	 */
	public void moveMine(int x, int y){
		mineField[x][y] = false;
		boolean placed = false;
		while(!placed){
			int randX = (int)(Math.random() * this.x);
			int randY = (int)(Math.random() * this.y);
			if(!mineField[randX][randY]){
				mineField[randX][randY] = true;
				placed = true;
			}
		}
	}
	
	/**
	 * Makes guess on all spaces that are not mines or have not been guess yet.
	 */
	public void solve(){
		for(int i = 0; i < this.x; i++){
			for(int j = 0; j < this.y; j++){
				if(!mineField[i][j] && !guessField[i][j])
					makeGuess(i, j);
			}
		}
	}
	
	

}

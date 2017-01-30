/*
 * The front end the Minesweeper application. Handles the layout of how the board is printed onto the screen.
 * 
 * Works in tandem with MineManager
 * 
 * by Christopher Berry
 */

public class VisualDriver {

	private MineManager mineField;
	
	/**
	 * creates a visual driver to display the mine field.
	 * @param mineField the {@link MineManager} to which the board will be printed from
	 */
	public VisualDriver(MineManager mineField) {
		this.mineField = mineField;
	}
	
	/**
	 * prints the current state of the guess board, each number indicating the number of adjacent mines
	 */
	public void printCurrentField(){
		if(mineField.getX() <= 10){
			System.out.print("  ");
			for(int j = 0; j < mineField.getX(); j++){
				System.out.print(" " + j);
			}
		}
		else{
			System.out.print("  ");
			for(int i = 0; i < 10; i++){
				System.out.print("  ");
			}
			for(int i = 10; i < mineField.getX(); i++){
				String blank = "" + i;
				System.out.print(" " + blank.charAt(0));
			}
			System.out.print("\n  ");
			for(int i = 0; i < mineField.getX(); i++){
				System.out.print(" " + i % 10);
			}
		}
		System.out.print("\n");
		for(int i = 0; i < mineField.getY(); i++){
			System.out.print("  ");
			for(int j = 0; j < mineField.getX(); j++){
				System.out.print(" _");
			}
			System.out.print("\n");
			System.out.printf("%2d", i);
			for(int j = 0; j < mineField.getX(); j++){
				if(mineField.getMineField()[j][i] && mineField.getGuessField()[j][i])
					System.out.print("|X");
				else if(mineField.getGuessField()[j][i])
					System.out.print("|"+mineField.getAdjacentMines(j, i));
				else
					System.out.print("|_");
			}
			System.out.print("|\n");
		}
	}
	
	/**
	 * prints the mine field board where each 'X' is a mine and each number is how many mines are adjacent to
	 * that square.
	 */
	public void printDebugField(){
		System.out.print("  ");
		for(int j = 0; j < mineField.getX(); j++){
			System.out.print(" " + j);
		}
		System.out.print("\n");
		for(int i = 0; i < mineField.getY(); i++){
			System.out.print("  ");
			for(int j = 0; j < mineField.getX(); j++){
				System.out.print(" _");
			}
			System.out.print("\n");
			System.out.print(i + " ");
			for(int j = 0; j < mineField.getX(); j++){
				if(mineField.getMineField()[j][i])
					System.out.print("|X");
				else if(true)
					System.out.print("|"+mineField.getAdjacentMines(j, i));
			}
			System.out.print("|\n");
		}
	}

	/**
	 * sets {@link VisualDriver#mineField} to the provided {@link MineManager}
	 * 
	 * @param m the {@link MineManager} to replace the current {@link MineManager}
	 */
	public void setManager(MineManager m){
		mineField = m;
	}
}

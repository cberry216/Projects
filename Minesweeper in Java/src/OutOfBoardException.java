
@SuppressWarnings("serial")
public class OutOfBoardException extends Exception {
	
	private int x;
	private int y;
	
	public OutOfBoardException(int x, int y){
		super();
		this.x = x;
		this.y = y;
	}
	
	public void reportError(){
		System.out.printf("Your guess, (%d, %d), lies outside of the board.%n", x, y);
	}

}

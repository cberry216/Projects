
@SuppressWarnings("serial")
public class PreviouslyGuessedException extends Exception {

	private int x;
	private int y;
	
	public PreviouslyGuessedException(int x, int y){
		super();
		this.x = x;
		this.y = y;
	}
	
	public void reportError(){
		System.out.printf("Your guess, (%d, %d), has already been guessed.%n", x, y);
	}

}

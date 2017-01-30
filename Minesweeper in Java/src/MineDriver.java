import java.util.Scanner;

public class MineDriver {
	private static int[] getCoords(String s){
		int[] coords = new int[2];
		String[] strCoords = s.split(",");
		coords[0] = Integer.parseInt(strCoords[0]);
		coords[1] = Integer.parseInt(strCoords[1]);
		return coords;
	}
	public static void main(String[] args){
		Scanner scan = new Scanner(System.in);
		System.out.print("Enter dimensions of mine field (X,Y): ");
		String dim = scan.nextLine();
		System.out.print("Enter number of mines: ");
		int mines = scan.nextInt();
		System.out.println();
		int[] dims = getCoords(dim);
		int x = dims[0];
		int y = dims[1];
		int moves = 0;
		MineManager field = new MineManager(x,y,mines);
		VisualDriver vis = new VisualDriver(field);
		vis.printCurrentField();
		while(field.checkGameOver() == -1){
			System.out.print("Enter coordinates of next guess (X,Y): ");
			String strGuess = scan.next();
			if(strGuess.equals("debug"))
				vis.printDebugField();
			else if(strGuess.equals("solve")){
				field.solve();
				vis.setManager(field);
				vis.printCurrentField();
			}
			else{
				int[] guess = getCoords(strGuess);
				if(moves == 0 && field.getMineField()[guess[0]][guess[1]])
					field.moveMine(guess[0], guess[1]);
				field.makeGuess(guess[0], guess[1]);
				moves++;
				vis.setManager(field);
				vis.printCurrentField();
			}
		}
		System.out.println();
		if(field.checkGameOver() == 0)
			System.out.println("You lost.");
		else
			System.out.println("You won!");
		System.out.println("Moves: " + moves);
		scan.close();
	}
}

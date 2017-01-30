package Descriptions;

/*
 * Vector: a class that represents a 3-dimension vector in the IJK reference frame.
 * 		Parameterized by T which should only be values of double, float, or int.
 */

public class Vector<T>{
	
	protected final int DIM = 3; //dimension of the vector, always 3
	protected double[] ijk = new double[DIM]; //index of array denotes i, j, and k direction of vector
	protected double mag; //magnitude of the array
	
	/**
	 * Initializes a Vector with values i, j, and k
	 */
	public Vector(double i, double j, double k) {
		ijk[0] = i;
		ijk[1] = j;
		ijk[2] = k;
		mag = magnitude();
	}
	/**
	 * Initializes a default Vector with i, j, and k values equals to 0.
	 */
	public Vector() {
		ijk[0] = 0;
		ijk[1] = 0;
		ijk[2] = 0;
	}
	
	/**
	 * Computes and returns the dot product of the current vector with the called vector
	 * @param v vector that is used for dot product
	 * @return the dot product of current vector and v.
	 */
	public double dotProduct(Vector<T> v){
		double sum = 0;
		for(int i = 0; i < DIM; i++){
			sum += (ijk[i] * v.ijk[i]);
		}
		return sum;
	}
	
	/**
	 * Computes and returns the cross product of the current vector with the called vector
	 * @param v vector that is used as the second vector in cross product
	 * @return vector representing the cross product of the 2 vectors.
	 */
	public Vector<T> crossProduct(Vector<T> v){
		Vector<T> cross = new Vector<T>();
		for(int i = 0; i < DIM; i++){
			double val = (ijk[(i+1)%3] * v.ijk[(i+2)%3]) - (ijk[(i+5)%3] * v.ijk[(i+4)%3]);
			cross.set(i,val);
		}
		return cross;
	}
	
	/**
	 * Comptues and returns the magnitude of the current vector
	 * @return magnitude of vector
	 */
	public double magnitude(){
		double sumSqr = 0;
		for(int i = 0; i < DIM; i++){
			sumSqr += ijk[i] * ijk[i];
		}
		return Math.sqrt(sumSqr);
	}
	
	public Vector<T> scaler(double n){
		Vector<T> scalarVector = new Vector<T>();
		for(int i = 0; i < DIM; i++)
			scalarVector.ijk[i] = ijk[i] * n;
		return scalarVector;
	}
	
	public Vector<T> addVector(Vector<T> v){
		Vector<T> newV = new Vector<T>();
		for(int i = 0; i < DIM; i++)
			newV.ijk[i] = ijk[i] + v.ijk[i];
		return newV;
	}
	
	/**
	 * set the value in a given index in the ijk array to a value
	 * @param ind index of value to change (0 = i, 1 = j, 2 = k)
	 * @param val value to change the provided index to
	 */
	public void set(int ind, double val){ijk[ind] = val;}
	
	/**
	 * Returns the array ijk
	 * @return the array ijk
	 */
	public double[] get(){return ijk;}
	
	
	@Override
	public String toString(){
		String s = "";
		char[] ijkc = new char[]{'i','j','k'};
		for(int i = 0; i < DIM; i++){
			if(ijk[i] < 0)
				s += " - " + (-1)*ijk[i] + ijkc[i];
			else if(ijk[i] > 0)
				s += " + " + ijk[i] + ijkc[i];
		}
		return s;
	}

	/**
	 * Returns whether the given vector is equivalent to the current vector
	 * @param v vector to compare the current vector to
	 * @return true if the current vector is equivalent to the called vector and false otherwise
	 */
	@SuppressWarnings("unchecked")
	@Override
	public boolean equals(Object v) {
		Vector<T> v2 = (Vector<T>)v;
		for(int i = 0; i < DIM; i++){
			if(ijk[i] != v2.ijk[i])
				return false;
		}
		return true;
	}

}

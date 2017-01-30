package Orbits;

import Descriptions.*;

public class OrbitalElements {

	protected Vector<Double> r;	//radius vector
	protected Vector<Double> v;	//velocity vector
	protected Vector<Double> h;	//specific angular momentum vector
	protected double i;			//inclination
	protected double a;			//semi-major axis
	protected double Omega;		//longitude of ascending node
	protected double lowOmega;	//argument of periapsis
	protected Vector<Double> e;	//eccentricity
	protected double theta;		//true anamoly 


	public OrbitalElements(Vector<Double> r, Vector<Double> v) {
		this.r = r;
		this.v = v;
		h = r.crossProduct(v);
		i = Math.acos(h.dotProduct(new Vector<Double>(0,0,1.0))/h.magnitude())* 180 / Math.PI;
		Vector<Double> nodeLine = h.crossProduct(new Vector<Double>(0,0,1.0));
		Omega = calcOmega(nodeLine);
		e = calcEccentricity(this.r,this.v, 1);
		lowOmega = calcLowOmega(nodeLine, e);
		theta = calcTheta(e,this.r);
	}

	protected double calcOmega(Vector<Double> nodeLine){
		double omg;
		try{
			if(nodeLine.get()[1] >= 0)
				omg = Math.acos(nodeLine.dotProduct(new Vector<Double>(1.0,0,0))/nodeLine.magnitude()) * 180 / Math.PI;
			else
				omg = 360 - (Math.acos(nodeLine.dotProduct(new Vector<Double>(1.0,0,0))/nodeLine.magnitude()) * 180 / Math.PI);
			return omg;
		}
		catch(ArithmeticException e){
			System.out.println("Line of nodes is undefined for this orbit.");
			return 0;
		}

	}
	
	protected Vector<Double> calcEccentricity(Vector<Double> r, Vector<Double> v, double mu){
		Vector<Double> ecc = new Vector<Double>();
		ecc = (r.scaler(v.magnitude() - (mu/r.magnitude())).addVector(v.scaler(-1 * r.dotProduct(v)))).scaler(1/mu);
		return ecc;
	}
	
	protected double calcLowOmega(Vector<Double> nodeLine, Vector<Double> ecc){
		double lomg;
		try{
			if(e.get()[2] >= 0)
				lomg = (Math.acos((nodeLine.dotProduct(ecc))/(nodeLine.magnitude() * ecc.magnitude()))) * 180 / Math.PI;
			else
				lomg = 360 - (Math.acos((nodeLine.dotProduct(ecc))/(nodeLine.magnitude() * ecc.magnitude()))) * 180 /Math.PI;
			return lomg;
		}
		catch(ArithmeticException e){
			System.out.println("Either eccentricity is 0 or Line of Node is undefined");
			return 0;
		}
	}
	
	protected double calcTheta(Vector<Double> ecc, Vector<Double> r){
		try{
			double thet;
			thet = Math.acos((ecc.dotProduct(r))/(ecc.magnitude() * r.magnitude())) * 180 / Math.PI;
			return thet;
		}
		catch(ArithmeticException e){
			System.out.println("Eccentricity is zero.");
			return 0;
		}
	}
	
	public Vector<Double> getR(){return this.r;}
	public Vector<Double> getV(){return this.v;}
	public Vector<Double> getH(){return this.h;}
	public double getI(){return this.i;}
	public double getOmega(){return this.Omega;}
	public Vector<Double> getEccentricity(){return this.e;}
	public double getLowOmega(){return this.lowOmega;}
	public double getTheta(){return this.theta;}

}

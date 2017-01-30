package tests;

import static org.junit.Assert.*;
import Descriptions.*;

import org.junit.Before;
import org.junit.Test;

public class VectorTest {

	Vector<Double> nullVector;
	Vector<Double> iVector;
	Vector<Double> jVector;
	Vector<Double> kVector;
	Vector<Double> ijk1Vector;
	Vector<Double> ijk2Vector;
	
	@Before
	public void before(){
		nullVector = new Vector<Double>();
		iVector = new Vector<>(2.4, 0, 0);
		jVector = new Vector<>(0, 3.1, 0);
		kVector = new Vector<>(0, 0, 5.6);
		ijk1Vector = new Vector<>(-1.4, 3.6, .45);
		ijk2Vector = new Vector<>(8.1, -6.4, -3.3);
	}
	
	@Test (timeout = 1000)
	public void test1DVectorDotProduct(){
		assertEquals(0.0, iVector.dotProduct(jVector), .00001);
		assertEquals(0.0, iVector.dotProduct(kVector), .00001);
		assertEquals(0.0, jVector.dotProduct(kVector), .00001);
	}
	
	@Test (timeout = 1000)
	public void test3DVectorDotProduct(){
		assertEquals(-35.865, ijk1Vector.dotProduct(ijk2Vector), .0001);
		assertEquals(-35.865, ijk2Vector.dotProduct(ijk1Vector), .0001);
	}
	
	@Test (timeout = 1000)
	public void test1DVectorsCrossProduct(){
		Vector<Double> ans;
		ans = new Vector<>(0, 0, 7.44);
		for(int i = 0; i < 3; i++)
			assertEquals(ans.get()[i], iVector.crossProduct(jVector).get()[i], .00001);
		ans = new Vector<>(0, -13.44, 0);
		for(int i = 0; i < 3; i++)
			assertEquals(ans.get()[i], iVector.crossProduct(kVector).get()[i], .00001);
		ans = new Vector<>(17.36, 0, 0);
		for(int i = 0; i < 3; i++)
			assertEquals(ans.get()[i], jVector.crossProduct(kVector).get()[i], .00001);
	}
	
	@Test (timeout = 1000)
	public void test3DVectorsCrossProduct(){
		Vector<Double> ans;
		ans = new Vector<>(-9.0, -0.975, -20.20);
		for(int i = 0; i < 3; i++)
			assertEquals(ans.get()[i], ijk1Vector.crossProduct(ijk2Vector).get()[i], .001);
	}
	
	@Test (timeout = 1000)
	public void testEquals(){
		Vector<Double> v1 = new Vector<>(1, 2, 3);
		Vector<Double> v2 = new Vector<>(1, 2, 3);
		Vector<Double> v3 = new Vector<>();
		assertTrue(v1.equals(v2));
		assertTrue(v2.equals(v1));
		assertFalse(v1.equals(v3));
		assertFalse(v2.equals(v3));
	}
	
	@Test (timeout = 1000)
	public void testScalarVector(){
		Vector<Double> vec = new Vector<Double>(1,2,3);
		Vector<Double> newVec = vec.scaler(5);
		for(int i = 1; i < 4; i++)
			assertEquals("Value should be " + (i * 5), i * 5, newVec.get()[i-1], .00001);
	}
	
	@Test (timeout = 1000)
	public void testAddVector(){
		Vector<Double> vec1 = new Vector<Double>(1,2,3);
		Vector<Double> vec2 = new Vector<Double>(1,2,3);
		Vector<Double> newVec = vec1.addVector(vec2);
		for(int i = 0; i < 3; i++)
			assertEquals((i+1) * 2, newVec.get()[i], .00001);
	}

}

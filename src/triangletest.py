#/usr/bin/python

import triangle
import unittest
import random
import math

class TestInvalidTriangles(unittest.TestCase):
    def testZero(self):
        """isNotTriangle should return True with zero inputs [bcaa54a165bb7858]"""
        
        random.seed();
        
        for i in range(10):
            j = random.randint(1,100);
            
            t = [0, 0, 0];
            result = triangle.isNotTriangle(t);
            self.assertTrue(result);
            
            t = [j, 0, 0];
            result = triangle.isNotTriangle(t);
            self.assertTrue(result);
            
            t = [j, j, 0];
            result = triangle.isNotTriangle(t);
            self.assertTrue(result);
            
            t = [0, j, j];
            result = triangle.isNotTriangle(t);
            self.assertTrue(result);
            
            t = [0, j, 0];
            result = triangle.isNotTriangle(t);
            self.assertTrue(result);
            
            t = [0, 0, j];
            result = triangle.isNotTriangle(t);
            self.assertTrue(result);
    
    def testNegative(self):
        """isNotTriangle should return True with negative inputs [f8868f9890e547f0]"""
            
        t = [-5, 5, 5];
        result = triangle.isNotTriangle(t);
        self.assertTrue(result);
        
    def testImpossible(self):
        """isNotTriangle should return True with impossible triangles [08ad593071aa995d]"""
        
        t = [3, 6, 9];
        result = triangle.isNotTriangle(t);
        self.assertTrue(result);
        
        t = [3, 6, 10];
        result = triangle.isNotTriangle(t);
        self.assertTrue(result);
        
        t = [2, 6, 9];
        result = triangle.isNotTriangle(t);
        self.assertTrue(result);

class Equilateral(unittest.TestCase):
    def testEqual(self):
        """isEquilateral should return True with equal values [f769dfadbe9d3afd]"""
        
        random.seed();
        
        for i in range(10):
            j = random.randint(2,10);
            t = [j, j, j];
            result = triangle.isNotTriangle(t);
            self.assertFalse(result);
            
            result = triangle.isEquilateral(t);
            self.assertTrue(result);
            
    def testNotEqual(self):
        """isEquilateral should return False with inequal values [bb5f925639d15c1f]"""
        
        random.seed();
        
        for i in range(10):
            j = random.randint(2,10);
            t = [j, j, j+1];
            result = triangle.isNotTriangle(t);
            self.assertFalse(result);
            
            result = triangle.isEquilateral(t);
            self.assertFalse(result);
            
            t = [j, j+1, j+2];
            result = triangle.isNotTriangle(t);
            self.assertFalse(result);
            
            result = triangle.isEquilateral(t);
            self.assertFalse(result);
            
class Scalene(unittest.TestCase):
    def testScalene(self):
        """isScalene should return True with scalene triangles [bc8859b03e2bc0fa]"""
        # this is a bad test
        
        random.seed();
        
        for i in range(10):
            j = random.randint(2,10);
            t = [j, j+1, j+2];
            result = triangle.isNotTriangle(t);
            self.assertFalse(result);
            
            result = triangle.isScalene(t);
            self.assertTrue(result);
    
    def testNotScalene(self):
        """isScalene should return False with not scalene triangles [2e79614fb2af8162]"""
        # another bad test
        
        random.seed();
        
        for i in range(10):
            j = random.randint(2,10);
            t = [j, j, j];
            result = triangle.isNotTriangle(t);
            self.assertFalse(result);
            
            result = triangle.isScalene(t);
            self.assertFalse(result);
            
            t = [j, j, j+1];
            result = triangle.isNotTriangle(t);
            self.assertFalse(result);
            
            result = triangle.isScalene(t);
            self.assertFalse(result);

class Isosceles(unittest.TestCase):
    def testIsosceles(self):
        """isIsoscles should return True with isosceles triangles [816d8bb3fdd27f88]"""
        # probably a poor test
        
        random.seed();
        
        for i in range(10):
            j = random.randint(2,10);
            t = [j, j, j+1];
            result = triangle.isNotTriangle(t);
            self.assertFalse(result);
            
            result = triangle.isIsosceles(t);
            self.assertTrue(result);
        
    def testNotIsosceles(self):
        """isIsosceles should return False with not isosceles triangles [6bcd95296db8bd5c]"""
        # this is likely another poor test
        
        for i in range(10):
            j = random.randint(2,10);
            t = [j, j, j];
            result = triangle.isNotTriangle(t);
            self.assertFalse(result);
            
            result = triangle.isIsosceles(t);
            self.assertFalse(result);
            
            t = [j, j+1, j+2];
            result = triangle.isNotTriangle(t);
            self.assertFalse(result);
            
            result = triangle.isIsosceles(t);
            self.assertFalse(result);
            
class Right(unittest.TestCase):
    def testRight(self):
        """isRight should return True with right triangles [a9dd9066a3c456dd]"""
        # I use pythagorean triples here, since each side is an integer
        # given 2 ints m, n
        # a = 2mn : b = m**2 - n**2 : c = m**2 + n**2
        
        random.seed();
        
        for i in range(10):
            j = random.randint(2,10);
            k = random.randint(j+1,20);
            t = [2 * j * k, k**2 - j**2, k**2 + j**2]
            result = triangle.isNotTriangle(t);
            self.assertFalse(result);
            
            result = triangle.isRight(t);
            self.assertTrue(result);
        
    def testNotRight(self):
        """isRight should return False with not right triangles [346561df2a581258]"""
        # I'm going to use the pythagorean theorum to reject right triangles...
        
        random.seed();
        
        for i in range(10):
            j = k = l = 0;
            while(j**2 + k**2 == l**2
                  or k**2 + l**2 == j**2
                  or l**2 + j**2 == k**2
                  or j + k <= l
                  or k + l <= j
                  or l + j <= k):
                j = random.randint(2,100);
                k = random.randint(2,100);
                l = random.randint(2,100);
            t = [j, k, l];
            result = triangle.isNotTriangle(t);
            self.assertFalse(result);
            
            result = triangle.isRight(t);
            self.assertFalse(result);

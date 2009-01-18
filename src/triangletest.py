#/usr/bin/python

import triangle
import unittest
import random

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
        
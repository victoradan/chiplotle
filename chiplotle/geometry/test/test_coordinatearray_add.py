from chiplotle import *
from py.test import raises


def test_coordinatearray__add__01( ):
   '''Two CoordinateArrays of the same size can be added.'''
   a = CoordinateArray([(1, 2), (3, 4)])
   b = CoordinateArray([(1, 1), (2, 2)])
   t = a + b
   assert isinstance(t, CoordinateArray)
   assert t is not a
   assert t is not b
   assert t == [(2, 3), (5, 6)]


def test_coordinatearray__add__02( ):
   '''Two CoordinateArrays of different length cannot be added.'''
   a = CoordinateArray([(1, 2), (3, 4)])
   b = CoordinateArray([(1, 1), (2, 2), (3, 3)])
   assert raises(ValueError, 't = a + b')


def test_coordinatearray__add__03( ):
   '''A CoordinateArray and an int can be added.'''
   a = CoordinateArray([(1, 2), (3, 4)])
   t = a + 2
   assert isinstance(t, CoordinateArray)
   assert t is not a
   assert t == [(3, 4), (5, 6)]


def test_coordinatearray__radd__04( ):
   '''An int and a CoordinateArray can be added.'''
   a = CoordinateArray([(1, 2), (3, 4)])
   t = 2 + a
   assert isinstance(t, CoordinateArray)
   assert t is not a
   assert t == [(3, 4), (5, 6)]


def test_coordinatearray__add__05( ):
   '''A CoordinateArray and a float can be added.'''
   a = CoordinateArray([(1, 2), (3, 4)])
   t = a + 2.3
   assert isinstance(t, CoordinateArray)
   assert t is not a
   assert t == [(3.3, 4.3), (5.3, 6.3)]


def test_coordinatearray__add__06( ):
   '''A float and a CoordinateArray can be added.'''
   a = CoordinateArray([(1, 2), (3, 4)])
   t = 2.3 + a
   assert isinstance(t, CoordinateArray)
   assert t is not a
   assert t == [(3.3, 4.3), (5.3, 6.3)]


def test_coordinatearray__add__07( ):
   '''A CoordinateArray and a Coordinate can be added.'''
   a = CoordinateArray([(1, 2), (3, 4)])
   t = a + Coordinate(2, 3)
   assert isinstance(t, CoordinateArray)
   assert t is not a
   assert t == [(3, 5), (5, 7)]


def test_coordinatearray__radd__08( ):
   '''A Coordinate and a CoordinateArray can be added.'''
   a = CoordinateArray([(1, 2), (3, 4)])
   t = Coordinate(2, 3) + a
   assert isinstance(t, CoordinateArray)
   assert t is not a
   assert t == [(3, 5), (5, 7)]


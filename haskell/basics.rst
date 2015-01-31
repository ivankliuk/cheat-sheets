Haskell basics
==============


**Function definition**

.. code :: haskell

  λ> let add x y = x + y

**Function call**

.. code :: haskell

  λ> add 1 2
  3
  λ> 1 + 2
  3
  λ> (+) 1 2
  3

**Lists**

List is a sequence of values with the same type. The type of a list says nothing about it's length.

.. code :: haskell

  λ> :type ['a', 'b', 'c']
  ['a', 'b', 'c'] :: [Char]

.. code :: haskell

  λ> let f = [1,2,4,5]
  λ> let f = [1,2,3,4,5]
  λ> 0 : f
  [0,1,2,3,4,5]
  λ> f !! 2
  3
  λ> [1,2] ++ [3,4,5]
  [1,2,3,4,5]

Lists are are compared in lexicographical order. First the heads are compared. If they are equal then the second elements are compared, etc.
  
.. code :: haskell

  λ> [1,2,3] < [2]
  True
  λ> ["a","b","c"] < ["b","b","c"]
  True

**Tuples**

A tuple is a sequence of values of different types. The type of a tuple describes its size.

.. code :: haskell

  λ> :type ('a', 2, False)
  ('a', 2, False) :: (Char, t, Bool)

**Where** clause

User ``where`` to define intermediate results that are local to the function

.. code :: haskell

  λ> let heron a b c = sqrt (s * (s - a) * (s - b) * (s - c)) where s = (a + b + c) / 2

Often used functions
````````````````````

Operations with lists

.. code :: haskell

  λ> head [1,2,3,4,5]
  1
  λ> tail [1,2,3,4,5]
  [2,3,4,5]
  λ> last [1,2,3,4,5]
  5
  λ> init [1,2,3,4,5]
  [1,2,3,4]
  λ> reverse [5,4,3,2,1]  
  [1,2,3,4,5]

``elem`` takes a thing and a list of things and tells us if that thing is an element of the list. It's usually called as an infix function because it's easier to read that way.

.. code :: haskell

  λ> 4 `elem` [3,4,5,6]  
  True  
  λ> 10 `elem` [3,4,5,6]  
  False 

``take`` and ``drop``

.. code :: haskell

  λ> take 3 [1,2,3,4,5]
  [1,2,3]
  λ> take 10 [1,2,3,4,5]
  [1,2,3,4,5]
  λ> take 0 [1,2,3,4,5]
  []
  λ> drop 3 [1,2,3,4,5]
  [4,5]
  λ> drop 10 [1,2,3,4,5]
  []
  λ> drop 0 [1,2,3,4,5]
  [1,2,3,4,5]

.. code :: haskell

  λ> minimum [1,2,3,4,5]
  1
  λ> maximum  [1,2,3,4,5]
  5
  λ> maximum [1,2,3,4,5]
  5
  λ> sum [1,2,3,4,5]
  15
  λ> product  [1,2,3,4,5]
  120

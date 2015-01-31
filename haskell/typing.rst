Haskell Typing System
=====================

.. code :: haskell

  λ> :type "Hello World!"
  "Hello World!" :: [Char]
  λ> :type 1
  1 :: Num a => a
  λ> :t True
  True :: Bool
  λ> :t [1, 2, 3]
  [1, 2, 3] :: Num t => [t]
  λ> :t (1, 2, 3)
  (1, 2, 3) :: (Num t, Num t1, Num t2) => (t, t1, t2)

Number type

.. code :: haskell

  λ> :t 1234
  1234 :: Num a => a
  λ> :t 1234.5
  1234.5 :: Fractional a => a
  λ> :t -1234.5
  -1234.5 :: Fractional a => a

Polymorphism

.. code :: haskell

  λ> :t length
  length :: [a] -> Int
  λ> :t [1,2,3]
  [1,2,3] :: Num t => [t]
  λ> :t length [1,2,3]
  length [1,2,3] :: Int
  λ> :t ['a','b','c']
  ['a','b','c'] :: [Char]
  λ> :t length ['a','b','c']
  length ['a','b','c'] :: Int

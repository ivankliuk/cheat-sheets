GHC's interactive environment
=============================

| :t(ype) - shows expression's type

.. code :: haskell

  λ> :type 1 + 1
  1 + 1 :: Num a => a

| :i(nfo) - shows info about function, typeclass, type, ...

.. code :: haskell

  λ> :info Bool
  data Bool = False | True        -- Defined in `GHC.Types'
  instance Bounded Bool -- Defined in `GHC.Enum'
  instance Enum Bool -- Defined in `GHC.Enum'
  instance Eq Bool -- Defined in `GHC.Classes'
  instance Ord Bool -- Defined in `GHC.Classes'
  instance Read Bool -- Defined in `GHC.Read'
  instance Show Bool -- Defined in `GHC.Show'

| :m(odule) - add a module to current scope

.. code :: haskell

  λ> sort [1,3,7,2,9,0,5,8,4,6]

  <interactive>:117:1:
      Not in scope: `sort'
      Perhaps you meant `sqrt' (imported from Prelude)
  λ> :m + Data.List
  λ> sort [1,3,7,2,9,0,5,8,4,6]
  [0,1,2,3,4,5,6,7,8,9]
  
| :! - execute shell command

.. code :: haskell

  λ> :! date
  Fri Nov 28 11:30:57 EET 2014

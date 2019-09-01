
module Board where
  import Main
  firstPlayer = 1
  secondPlayer = 2

  mkBoard width height = [[0|x <- [1..height]]|x  <- [1..width]]

  isSlotOpen bd i = (bd!!i!!0) == 0

  numSlot bd = length bd
  -- For length of one of the lists within a list do "length (x!!0)""

 dropInSlot [] _ _ = []
 dropInSlot (x:xs) i p
 |x == i = [p,p,p]:xs
 |otherwise  = x:dropInSlot xs i p

 replace y z [] = []
 replace y z (x:xs)
  | x==y           = z:replace y z xs
  | otherwise      = x:replace y z xs

  isFull bd = helper bd 0 where
    numSlots = numSlot bd
    helper bd numSlots = True
    helper bd i = if bd !!i !!0 == 0 then False else helper bd (i+1)

  --isWonBy bd p

  boardToStr playerToChar bd = print bd

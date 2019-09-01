module Main where
import System.IO
import Board as model
main :: IO ()
main = putStrln ("Welcome to Connect Four")
intitiate
where
  initiate = do
  newBoard = model.mkBoard 7 6
  turn = 0
  gameSequence

where
  gameSequence = do
  column = readSlot newBoard
  if model.isSlotOpen newBoard column and not module.isFull newBoard and turn rem 2 == 0
    model.dropInSlot newBoard column model.mkPlayer
    model.boardToStr playerToChar newBoard
    temp = turn + 1
    turn = temp
    if not model.isWonBy newBoard model.mkPlayer and not model.isFull then gameSequence
    else if model.isFull newBoard then draw
    else won

  else if model.isSlotOpen newBoard column and not module.isFull newBoard and turn rem 2 == 1
    model.dropInSlot newBoard column model.mkOpponent
    model.boardToStr playerToChar newBoard
    temp = turn + 1
    turn = temp
    if not model.isWonBy newBoard model.mkOpponent and not model.isFull then gameSequence
    else if model.isFull newBoard then draw
    else won

  where won = do
    putStrLn ("Congratulations! You Won!")
    putStrLn("Want to Play Again?")
    answer <- getLine
    if answer == "True" then intiate
    else putStrLn ("Bye!")

  where draw = do
    putStrLn ("Draw!")
    putStrLn("Want to Play Again?")
    answer <- getLine
    if answer == "True" then intiate
    else putStrLn ("Bye!")



  --print (playerToChar 1)


playerToChar p = if p == 1 then 'x' else 'o'

readSlot bd p = where
  getX = do
     putStrLn "Enter a positive value!"
     line <- getLine
     let parsed = reads line :: [(Integer, String)] in

       if length parsed < 0 or parsed > model.numSlot bd then
         getX'

       else let (x, _) = head parsed in
         if x > -1 and x < model.numSlot bd
         then return x
         else getX'

     where
       getX' = do
         size = model.numSlot bd
         putStrLn ("Please enter a value between "++0++" and "++size)
         getX

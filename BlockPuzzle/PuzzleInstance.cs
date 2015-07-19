using System;
using System.Collections.Generic;
using System.Text;

namespace BlockPuzzle
{
    // PuzzleInstance is a object that represents an instance of the BlockPuzzle game
    // has nxn board with PuzzleBlocks with n^2 unique #s
    // responds to move(position), puzzleCompleted(), availableMoves(), setConfiguration(configuration)
    class PuzzleInstance
    {
        private PuzzleBlock[,] puzzleBoard;
        private BlockPuzzleConfigList targetConfiguration;
        private Tuple<int, int> emptyBlockPosition; //keep track of where the emptyblock is

        public PuzzleInstance(BlockPuzzleConfigList initConfig, BlockPuzzleConfigList targetConfig)
        {
            initiatePuzzleBoard(targetConfig);
            setupConfiguration(initConfig);
        }

        private void initiatePuzzleBoard(BlockPuzzleConfigList target)
        {
            puzzleBoard = new PuzzleBlock[Globals.gridDimension, Globals.gridDimension];
            for (int r = 0; r < Globals.gridDimension; r++)
            {
                for (int c = 0; c < Globals.gridDimension; c++)
                {
                    puzzleBoard[c, r] = new PuzzleBlock(0, c, r);
                }
            }
            targetConfiguration = target;
        }

        public void setupConfiguration(BlockPuzzleConfigList initialConfiguration)
        {
            int i = 0;
            for (int r = 0; r < Globals.gridDimension; r++)
            {
                for (int c = 0; c < Globals.gridDimension; c++)
                {
                    puzzleBoard[c, r].Number = initialConfiguration[i];
                    i++;
                }
            }
            emptyBlockPosition = findEmptyBlockPos();            
        }

        public List<string> getAvailableMoves()
        {
            var moves = new List<string>();

            // consider adjacent blocks of emptyBlock that are within bounds of the grid
            int emptyBoxXPos = emptyBlockPosition.Item1;
            int emptyBoxYPos = emptyBlockPosition.Item2;

            int upperBound = Globals.gridDimension - 1;
            //consider 4 sides
            if (emptyBoxXPos + 1 <= upperBound)
            {
                //move to left is possible
                moves.Add("left");
            }
            if (emptyBoxXPos - 1 >= 0)
            {
                //move to right is possible
                moves.Add("right");
            }
            if (emptyBoxYPos - 1 >= 0)
            {
                //move to down is possible
                moves.Add("down");
            }
            if (emptyBoxYPos + 1 <= upperBound)
            {
                //move to up is possible
                moves.Add("up");
            }

            return moves;
        }

        public bool move(string move)
        {
            int emptyBoxXPos = emptyBlockPosition.Item1;
            int emptyBoxYPos = emptyBlockPosition.Item2;
            int upperBound = Globals.gridDimension - 1;
            switch (move)
            {
                //check if move is possible and legal (target pos has block with num 0)
                case "up":
                    if (emptyBoxYPos + 1 <= upperBound)
                    {
                        int sourceNumber = puzzleBoard[emptyBoxXPos, emptyBoxYPos + 1].Number;
                        puzzleBoard[emptyBoxXPos, emptyBoxYPos].Number = sourceNumber;
                        puzzleBoard[emptyBoxXPos, emptyBoxYPos + 1].Number = 0;
                        emptyBlockPosition = Tuple.Create(emptyBoxXPos, emptyBoxYPos + 1);
                        return true;
                    }
                    break;
                case "down":
                    if (emptyBoxYPos - 1 >= 0)
                    {
                        int sourceNumber = puzzleBoard[emptyBoxXPos, emptyBoxYPos - 1].Number;
                        puzzleBoard[emptyBoxXPos, emptyBoxYPos].Number = sourceNumber;
                        puzzleBoard[emptyBoxXPos, emptyBoxYPos - 1].Number = 0;
                        emptyBlockPosition = Tuple.Create(emptyBoxXPos, emptyBoxYPos - 1);
                        return true;
                    }
                    break;
                case "left":
                    if (emptyBoxXPos + 1 <= upperBound)
                    {
                        int sourceNumber = puzzleBoard[emptyBoxXPos + 1, emptyBoxYPos].Number;
                        puzzleBoard[emptyBoxXPos, emptyBoxYPos].Number = sourceNumber;
                        puzzleBoard[emptyBoxXPos + 1, emptyBoxYPos].Number = 0;
                        emptyBlockPosition = Tuple.Create(emptyBoxXPos + 1, emptyBoxYPos);
                        return true;
                    }
                    break;
                case "right":
                    if (emptyBoxXPos - 1 >= 0)
                    {
                        int sourceNumber = puzzleBoard[emptyBoxXPos - 1, emptyBoxYPos].Number;
                        puzzleBoard[emptyBoxXPos, emptyBoxYPos].Number = sourceNumber;
                        puzzleBoard[emptyBoxXPos - 1, emptyBoxYPos].Number = 0;
                        emptyBlockPosition = Tuple.Create(emptyBoxXPos - 1, emptyBoxYPos);
                        return true;
                    }
                    break;
                default:
                    break;

            }
            return false;
        }

        public bool puzzleCompleted()
        {
            int i = 0;
            for (int r = 0; r < Globals.gridDimension; r++)
            {
                for (int c = 0; c < Globals.gridDimension; c++)
                {
                    if (puzzleBoard[c, r].Number != targetConfiguration[i])
                    {
                        return false;
                    }
                    i++;
                }
            }
            return true;
        }

        public override string ToString()
        {
            var result = new StringBuilder();
            for (int i = 0; i < Globals.gridDimension; i++)
            {
                for (int j = 0; j < Globals.gridDimension; j++)
                {
                    result.Append(puzzleBoard[j, i].Number.ToString());
                    result.Append(" ");
                }
                result.AppendLine();
            }
            return result.ToString();
        }

        public BlockPuzzleConfigList getCurrentConfiguration()
        {
            var config = new BlockPuzzleConfigList();
            for (int i = 0; i < Globals.gridDimension; i++)
            {
                for (int j = 0; j < Globals.gridDimension; j++)
                {
                    config.Add(puzzleBoard[j, i].Number);
                }
            }
            return config;
        }

        private Tuple<int, int> findEmptyBlockPos()
        {
            //find location of "0" number on the board and return it
            for (int r = 0; r < Globals.gridDimension; r++)
            {
                for (int c = 0; c < Globals.gridDimension; c++)
                {
                    if (puzzleBoard[c, r].Number == 0)
                    {
                        return Tuple.Create(puzzleBoard[c, r].getXPos(), puzzleBoard[c, r].getYPos());
                    }
                }
            }
            return Tuple.Create(-1, -1);
        }
    }
}

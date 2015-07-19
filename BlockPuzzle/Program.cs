using System;
using System.Collections.Generic;

namespace BlockPuzzle
{
    class Program
    {        
        static void Main(string[] args)
        {            
            PuzzleInstance puzzle = new PuzzleInstance(Globals.initialConfiguration); //could also supply any arbitrary initial configuration
            PuzzleSolver solver = new PuzzleSolver(puzzle);
            var listOfMovesToSolve = solver.solve(); 
            if (listOfMovesToSolve != null)
            {
                printSolution(listOfMovesToSolve);
            }
        }

        static void printSolution(List<Tuple<int, string>> listOfMoves)
        {
            int i = 0;
            for (i = 0; i < listOfMoves.Count; i++)
            {
                Console.WriteLine("Step {0}: Move {1} {2}", i+1, listOfMoves[i].Item1, listOfMoves[i].Item2);                
            }
        }
    }
}

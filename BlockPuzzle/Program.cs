using System;
using System.Collections.Generic;

namespace BlockPuzzle
{
    class Program
    {        
        static void Main(string[] args)
        {            
            PuzzleInstance puzzle = new PuzzleInstance(Globals.initialConfiguration, Globals.targetConfiguration); //could also supply any arbitrary initial and target configurations
            PuzzleSolver solver = new PuzzleSolver(puzzle);
            var listOfMovesToSolve = solver.solve(); 
            if (listOfMovesToSolve != null)
            {
                Console.WriteLine("Solution found!");
                printSolution(listOfMovesToSolve);
            }
            else{
                Console.WriteLine("No Solution found!");
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

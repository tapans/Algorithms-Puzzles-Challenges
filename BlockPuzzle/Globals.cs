using System;
using System.Collections.Generic;
using System.Linq;

namespace BlockPuzzle
{
    static class Globals
    {
        public static int gridDimension = 3; //3x3 grid;

        public static BlockPuzzleConfigList initialConfiguration = new BlockPuzzleConfigList()
        {
            3,
            7,
            1,
            6,
            4,
            2,
            8,
            5,
            0
        };

        public static BlockPuzzleConfigList targetConfiguration = new BlockPuzzleConfigList()
        {
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9
        };            

        public static void doTests()
        {
            //Extremely Raw test of crucial PuzzleInstance & PuzzleBlock methods
            Console.WriteLine("----------------BEGIN RAW TEST-----------------");
            var p = new PuzzleInstance(Globals.initialConfiguration, Globals.targetConfiguration);
            Console.Write(p);
            var m = p.getAvailableMoves().First();
            Console.WriteLine("making the move to: {0}", m);
            p.move(m);
            Console.Write(p);
            Console.WriteLine("is puzzle solved: {0}", p.puzzleCompleted());
            p.setupConfiguration(Globals.targetConfiguration);
            Console.Write(p);
            Console.WriteLine("is puzzle solved: {0}", p.puzzleCompleted());
            p = new PuzzleInstance(Globals.initialConfiguration, Globals.targetConfiguration);
            p.move("right");
            p.move("right");
            p.move("down");
            p.move("down");
            p.move("left");
            p.move("left");
            p.move("up");
            p.move("up");
            p.move("right");
            Console.Write(p);
            Console.WriteLine("-----------------END RAW TEST------------------");

            Console.WriteLine("----------------BEGIN RAW PUZZLE_STATE_NODE TEST-----------------");
            p = new PuzzleInstance(Globals.initialConfiguration, Globals.targetConfiguration);
            var root = new PuzzleStateNode("", p.getCurrentConfiguration());
            PuzzleStateNode child;
            var tempConfig = p.getCurrentConfiguration();
            foreach (string move in p.getAvailableMoves())
            {
                p.setupConfiguration(tempConfig);
                p.move(move);
                child = new PuzzleStateNode(move, p.getCurrentConfiguration());
                root.Nodes.Add(child);

                Console.WriteLine(child.Parent.GetType());
            }
            Console.WriteLine(null == root.Parent);
            Console.WriteLine("----------------END RAW PUZZLE_STATE_NODE TEST-----------------");
        }

    }
}

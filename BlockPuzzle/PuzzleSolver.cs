using System;
using System.Collections.Generic;

namespace BlockPuzzle
{
    // is an object that has a PuzzleInstance representation of a Block Puzzle Game
    // responds to solve() which goes through builds a Tree of PuzzleState configurations 
    //  to determine which state has the winning configuration and uses the tree structure to infer the sequence of positions leading up to the state
    class PuzzleSolver
    {
        private PuzzleInstance puzzleInstance;
        private HashSet<BlockPuzzleConfigList> encounteredConfigurations;
        private List<Tuple<int, string>> solution;
        private int numStatesToProcess = 0;
        public PuzzleSolver(PuzzleInstance puzzInst)
        {
            puzzleInstance = puzzInst;
            encounteredConfigurations = new HashSet<BlockPuzzleConfigList>();
        }
        
        public List<Tuple<int, string>> solve()
        {
            var stateConfig = puzzleInstance.getCurrentConfiguration();
            var puzzleStateRootNode = new PuzzleStateNode("", stateConfig);
            encounteredConfigurations.Add(stateConfig);

            Queue<PuzzleStateNode> q = new Queue<PuzzleStateNode>();
            q.Enqueue(puzzleStateRootNode);
            int numChildren;
            int i;
            while (q.Count > 0)
            {
                PuzzleStateNode node = q.Dequeue();
                if (solveHelper(node, node.getCurrentConfiguration()))
                {
                    Console.WriteLine("solution found!");
                    return solution;
                }
                numChildren = node.Nodes.Count;
                for (i=0; i<numChildren; i++)
                {
                    q.Enqueue((PuzzleStateNode) node.Nodes[i]);
                }
            }
            Console.WriteLine("NO solution found!");
            return null;
        }
        
        private bool solveHelper(PuzzleStateNode node, BlockPuzzleConfigList stateConfig)
        {
            PuzzleStateNode childPuzzleStateNode;
            BlockPuzzleConfigList tempConfig;
            puzzleInstance.setupConfiguration(stateConfig);
            var moves = puzzleInstance.getAvailableMoves();
            foreach (string move in moves)
            {
                puzzleInstance.setupConfiguration(stateConfig); //reset puzzleInstance from previous loop changes
                puzzleInstance.move(move);
                tempConfig = puzzleInstance.getCurrentConfiguration();
                    
                if (encounteredConfigurations.Add(tempConfig))                    
                {
                    childPuzzleStateNode = new PuzzleStateNode(move, tempConfig);                                                
                    node.Nodes.Add(childPuzzleStateNode);
                    if (puzzleInstance.puzzleCompleted())
                    {
                        childPuzzleStateNode.SolvedState = true;
                        solution = getSolutionList(childPuzzleStateNode);
                        return true;
                    }
                }
            }
            return false;
        }

        private List<Tuple<int, string>> getSolutionList(PuzzleStateNode node)
        {
            var result = new List<Tuple<int, string>>();
            var moves = new Stack<Tuple<int, string>>();
            while (node.Parent != null)
            {
                string move = node.getLastMove();
                moves.Push(Tuple.Create(getMovedNum(node.getCurrentConfiguration(), move), move));
                node = (PuzzleStateNode) node.Parent;
            }
            while (moves.Count > 0)
            {
                result.Add(moves.Pop());
            }
            return result;
        }

        private int getMovedNum(List<int> configuration, string move)
        {
            int numBlocks = configuration.Count;
            for (int i=0; i< numBlocks; i++)
            {
                if (configuration[i] == 0)
                {
                    //The number of the block that was moved is in the location relative to where the block with number 0 is.
                    if (move == "up")
                    {
                        return configuration[i - Globals.gridDimension];
                    }
                    else if (move == "down")
                    {
                        return configuration[i + Globals.gridDimension];
                    }
                    else if (move == "left")
                    {
                        return configuration[i - 1];
                    }
                    else if(move == "right")
                    {
                        return configuration[i + 1];
                    }
                }
            }
            return -1;
        }

        /* Originally used this method to check for visited states, but was cpu intensive, so switched to using hashset instead
        private bool isNewConfiguration(BlockPuzzleConfigList configuration)
        {
            int numElms = configuration.Count;
            int i;
            bool existingConfigurationFound;
            foreach (BlockPuzzleConfigList c in this.encounteredConfigurations)
            {
                existingConfigurationFound = true;
                for (i = 0; i < numElms; i++)
                {
                    if (c[i] != configuration[i])
                    {
                        existingConfigurationFound = false;
                    }
                }
                if (existingConfigurationFound)
                {
                    return false;
                }
            }
            return true;
        }
        */

        /* recursive solution caused stack overflow due to large number of function calls
        private void createPuzzleStateTree(PuzzleStateNode node)
        {
            bool solved = solveHelper(node, node.getCurrentConfiguration());
            if (solved || this.numStatesToProcess == 0)
            {
                return;
            }
            else
            {
                for (int i = 0; i < node.Nodes.Count; i++)
                {
                    createPuzzleStateTree((PuzzleStateNode)node.Nodes[i]);
                }
            }
        }
        */

        //initial solution which did not work because of too much memory allocation 
        //  due to constant appending of previous moves with current move for current state
        /*
        public List<string> solve()
        {
            List<string> prevMoves = new List<string>();
            List<int> currentConfig = this.puzzleInstance.getCurrentConfiguration();
            PuzzleState currState = new PuzzleState(prevMoves, currentConfig);
            this.statesToConsider.Push(currState);
            this.encounteredConfigurations.Add(currentConfig);

            List<string> moves;
            List<string> tempPrevMvs;
            PuzzleState newState;
            List<int> tempConfig;
            while (null != currState)
            {
                currentConfig = currState.getCurrentConfiguration();
                this.puzzleInstance.setupConfiguration(currentConfig);
                
                moves = this.puzzleInstance.getAvailableMoves();
                var lastMove = currState.getPrevMoves().LastOrDefault();
                foreach (String move in moves)
                {
                    this.puzzleInstance.setupConfiguration(currentConfig);
                    if (move != Globals.getComplementMove(lastMove))
                    {
                        this.puzzleInstance.move(move);
                        tempConfig = this.puzzleInstance.getCurrentConfiguration();

                        if (this.puzzleInstance.puzzleCompleted())
                        {
                            Console.WriteLine("FOUND A SOLUTION!");
                            tempPrevMvs = new List<string>();
                            prevMoves = currState.getPrevMoves();
                            foreach (string oldMv in prevMoves)
                            {
                                tempPrevMvs.Add(oldMv);
                            }
                            tempPrevMvs.Add(move);
                            return tempPrevMvs;
                        }

                        if (isNewConfiguration(tempConfig))
                        {
                            tempPrevMvs = new List<string>();
                            prevMoves = currState.getPrevMoves();
                            foreach (string oldMv in prevMoves)
                            {
                                tempPrevMvs.Add(oldMv);
                            }
                            tempPrevMvs.Add(move);
                            newState = new PuzzleState(tempPrevMvs, tempConfig);
                            statesToConsider.Push(newState);
                            encounteredConfigurations.Add(tempConfig);
                        }
                    }
                }
                currState = statesToConsider.Count > 0 ? statesToConsider.Pop() : null;
            }
            Console.WriteLine("Could not find a solution!");
            return null;
        }
        */
    }
}

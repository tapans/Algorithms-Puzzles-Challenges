using System.Collections.Generic;
using System.Windows.Forms;

namespace BlockPuzzle
{
    //is an object to encapsulate a particular state of the puzzleInstance
    //has a history of previous moves leading up to current configuration, current configuration of puzzle instance
    //responds to: getPrevMoves(), getCurrentConfiguration(), 
    class PuzzleStateNode : TreeNode{
         private string lastMove;
         private BlockPuzzleConfigList currentConfiguration;
         private bool solvedState = false;

         public PuzzleStateNode(string prevMove, BlockPuzzleConfigList configuration)
         {
            lastMove = prevMove;
            currentConfiguration = configuration;
         }

         public string getLastMove()
         {
             return lastMove;
         }

         public BlockPuzzleConfigList getCurrentConfiguration()
         {
             return currentConfiguration;
         }    
        
        public bool SolvedState
        {
            get
            {
                return solvedState;
            }
            set
            {
                solvedState = value;
            }
        }    
    }
}

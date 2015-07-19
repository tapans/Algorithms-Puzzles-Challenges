using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BlockPuzzle
{
    class BlockPuzzleConfigList : List<int>, IEquatable<BlockPuzzleConfigList>
    {
        //This will prevent adding two equal objects to be added to the Set – provided that they should be considered equal of course.
        //http://dotnetcodr.com/2014/01/08/using-hashset-in-net-to-allow-unique-values-only/
        public override int GetHashCode()
        {
            int numElems = Count;
            int sum = 0;
            for (int i = 0; i< numElems; i++)
            {
                sum += i * this[i];
            }
            return sum.GetHashCode();
        }

        public bool Equals(BlockPuzzleConfigList other)
        {
            int numElems = other.Count;
            for (int i = 0; i < numElems; i++)
            {
                if (this[i] != other[i])
                {
                    return false;
                }
            }
            return true;
        }
    }
}

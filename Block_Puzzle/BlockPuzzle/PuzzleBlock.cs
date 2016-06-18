namespace BlockPuzzle
{
    //PuzzleBlock is a object that 
    // has a Block position in x,y coordinates, and an associated number
    // it responds to getting and setting the number, and getting x,y coordinates of the block
    class PuzzleBlock
    {
        private int number;
        private int pos_x;
        private int pos_y;

        public PuzzleBlock(int number, int x, int y)
        {
            this.number = number;
            pos_x = x;
            pos_y = y;
        }

        public int Number
        {
            get
            {
                return number;
            }
            set
            {
                number = value;
            }
        }

        public int getXPos()
        {
            return pos_x;
        }

        public int getYPos()
        {
            return pos_y;
        }
    }
}

var BlockPuzzleGame;
		var steps;		

		function addClass(es,c){
			for (i=0;i<es.length;i++){
				es[i].className += " " + c;	
			}
			
		}

		function removeClass(es,c) {
			for (i=0;i<es.length;i++){
				es[i].className = es[i].className.replace( new RegExp('(?:^|\\s)'+c+'(?!\\S)') ,'');
			}			
		}

		(function(){
			BlockPuzzleGame = {

				gameDimension: 3,				
				initialConfiguration: [3,7,1,6,4,2,8,5,0],
				targetConfiguration: [0,1,2,3,4,5,6,7,8],
				blocks: document.getElementsByClassName("block"),
				listeners: [],

				init: function(){
					this.render();
					this.resetGame();										
				},

				render: function(){
					var gameBoard = "<table>";
					var block;
					for (i=0; i<this.gameDimension; i++){
						gameBoard += "<tr>";
						for (j=0; j<this.gameDimension; j++){
							block = "<td><div id=" + j + "," + i + " class='block'></div></td>";
							gameBoard += block;							
						}
						gameBoard += "</tr>";
					}
					gameBoard += "</table>";
					document.getElementById("gameBoard").innerHTML = gameBoard;
				},

				resetGame: function(){
					//When you use "var" , you are instantiating (or overwriting) a variable in the current scope. 
					//This will also prevent access of variables named the same in higher scope, within the current scope					 					
					var numBlocks = this.blocks.length;
					for (i=0;i<numBlocks;i++){
						this.blocks[i].innerHTML = this.initialConfiguration[i];						
					}
					removeClass(this.blocks, "emptyBlock");
					this.emptyPosBlock = this.findEmptyPosBlock();
					this.hideEmptyPosBlock();

					steps = 0;
					document.getElementById('displayMessage').innerHTML = "";
					document.getElementById('restartBtn').style.backgroundColor = "green";
					removeClass(document.getElementsByClassName("block"), "winBlock");

					this.bindEvents();
				},

				bindEvents: function(){								
					document.getElementById("restartBtn").addEventListener("mousedown", this.resetGame.bind(this));

					numBlocks = this.blocks.length;
					for (i=0; i<numBlocks; i++){
						this.listeners[i] = this.move.bind(this)
						this.blocks[i].addEventListener("mousedown", this.listeners[i]);
						this.blocks[i].addEventListener("mousedown", this.listeners[i]);
					}					
				},

				findEmptyPosBlock: function(){
					var numBlocks = this.blocks.length;
					for (i=0;i<numBlocks;i++){
						if (this.blocks[i].innerHTML == "0"){
							return this.blocks[i];
						}
					}
				},

				hideEmptyPosBlock: function(){
					addClass([this.emptyPosBlock], "emptyBlock");					
				},

				move: function(event){			
					
					//check if emptyBlock is located anywhere around me.
					//if it is => remove emptyBlock class from current emptyPosBlock, set its number to numer of elemToMove, set emptyPosBlock to elemToMove after setting its label to 0, and call hideEmptyPosBlock
					var elemToMove = event.srcElement;	
					var emptyPosBlock = this.emptyPosBlock;						
					var emptyPos = emptyPosBlock.id.split(",");
					var emptyPosX = emptyPos[0];
					var emptyPosY = emptyPos[1];
					var elemToMovePos = elemToMove.id.split(",");
					var elemToMovePosX = elemToMovePos[0];
					var elemToMovePosY = elemToMovePos[1];					

					if (elemToMovePosX == emptyPosX && Number(elemToMovePosY - 1) == emptyPosY
						|| elemToMovePosX == emptyPosX && Number(elemToMovePosY) + 1 == emptyPosY
						|| Number(elemToMovePosX) - 1 == emptyPosX && elemToMovePosY == emptyPosY
						|| Number(elemToMovePosX) + 1 == emptyPosX && elemToMovePosY == emptyPosY){
						var sourceNum = elemToMove.innerHTML;
						emptyPosBlock.innerHTML = sourceNum;
						elemToMove.innerHTML = "0";
						removeClass([emptyPosBlock], "emptyBlock");
						this.emptyPosBlock = elemToMove;
						this.hideEmptyPosBlock();

						steps++;

						if (elemToMovePosX > emptyPosX) direction="left"; 
						if (elemToMovePosX < emptyPosX) direction="right"; 
						if (elemToMovePosY > emptyPosY) direction="up"; 
						if (elemToMovePosY < emptyPosY) direction="down"; 

						statusUpdate = "Step " + steps + ": Moved " + sourceNum + " " + direction + " <br>";
						if (this.gameWon()){
							addClass(document.getElementsByClassName("block"), "winBlock");
							statusUpdate += "<br><span id='wonMssg'>Congratulations! You completed the puzzle in " + steps + " steps!</span><br>";
							for (i=0;i<this.blocks.length;i++){
								this.blocks[i].removeEventListener("mousedown", this.listeners[i]);
								this.blocks[i].removeEventListener("mousedown", this.listeners[i]);
							}
							document.getElementById('restartBtn').style.backgroundColor = "red";
						} 
						var statusElem = document.getElementById("displayMessage");
						statusElem.innerHTML += statusUpdate;
						statusElem.scrollTop = statusElem.scrollHeight;
					}					
				},

				gameWon: function(){
					var numBlocks = this.blocks.length;
					for (i=0;i<numBlocks;i++){
						if (this.blocks[i].innerHTML != this.targetConfiguration[i]){
							return false;
						}						
					}
					return true;
				}
			}

			BlockPuzzleGame.init();	
		})();

#String Diff in real time editor

###Context:
Imagine Alice and Bob are using a web application like Google Docs where they can edit text in real time.<br>
Suppose Alice typed a word on this shared doc, after which Bob came in and made an edit.<br>
The client-side (browser) should ideally only send the delta back to the server instead of the entire string <br>
(If there were millions of lines in the document, you wouldn't want to send all those lines back to the server for only changing a letter, for example)

###Problem:
Write a method that takes the existing word and the new word (after the edit is made), and return an object like:<br>
<pre>
{ 
	type : "...",
	index: i,
	diff : "..."
}
</pre>
- type is one of ["replacement", "deletion", "insertion"] indicating the type of edit made
- index is the start position of where the edit is made on the longer string
- diff is the actual changed string.

###Assumptions:
- for replacement, assume the diff of the new string always has unique characters (no overwriting letter(s) with same letter(s)). 
		So can't change "hello" to "hAllE"

Examples: 
```
get_diff("hell", "heEl")  would return  {
											type : "replacement",
											index: 2,
											diff : "E"
										}

get_diff("hell", "hellO") would return  {
											type: "insertion",
											index: 4,
											diff: "O"
										}

get_diff("heLL", "he") would return     {
											type: "deletion",
											index: 2,
											change: "LL"
										}

get_diff("case", "cHHase") would return {
											type : "insertion",
											index: 1,
											change: "HH"
										}						
```
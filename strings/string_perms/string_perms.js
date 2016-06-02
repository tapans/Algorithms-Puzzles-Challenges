#!/usr/bin/node

function get_string_perms(s){
	//BC: return if len <= 1
	if (s.length <= 1){
		return [s];
	} 

	//recursive step
	else {
		var num_chars = s.length;
		var i = 0;
		var curr_perms = [];
		for (; i < num_chars; i++){
			var substr_perms = get_string_perms(s.slice(0,i) + s.slice(i+1))
			substr_perms = substr_perms.map(function(sub_perm){ return s[i] + sub_perm });
			curr_perms = curr_perms.concat(substr_perms)
		}
		return curr_perms;
	}
}

//enter desired input string as command line parameter
console.log(get_string_perms(process.argv[2] || "abc"))	

function get_diff(old_str, new_str){
	if (old_str === new_str) return diff_obj("no change", 0, "");

	var type, index, diff;
	var len_old_str = old_str.length;
	var len_new_str = new_str.length;
	var i = 0;
	var diff = "";
	if (len_old_str === len_new_str){
		type = 'replacement';
		while ((old_str[i] === new_str[i]) && (i < len_old_str)){
			i++;
		}
		index = i;
		while ((old_str[i] !== new_str[i]) && (i < len_old_str)){			
			diff += new_str[i];
			i++;
		}
		return diff_obj(type, index, diff);
	} else {		
		var smaller_str = len_old_str > len_new_str ? new_str : old_str;
		var larger_str = len_old_str > len_new_str ? old_str : new_str;		
		type = len_old_str > len_new_str ? "deletion" : "insertion";
	
		var len_diff = Math.abs(len_old_str - len_new_str);
		while ((smaller_str[i] === larger_str[i]) && (i < smaller_str.length)){
			i++;
		}
		index = i;
		var end_index = index + len_diff;
		while (i < end_index){
			diff += larger_str[i];
			i++;
		}
		return diff_obj(type, index, diff);
	}

	function diff_obj(type, index, diff){
		return {
			type: type,
			index: index,
			diff: diff
		}
	}
}
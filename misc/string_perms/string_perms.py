#!/usr/bin/python
import sys

def get_string_perms(s):
    if (len(s) <= 1):
        return [s]
    else:
        curr_perms = []
        for i in range(len(s)):
            substr_perms = get_string_perms(s[:i] + s[i+1:])
            curr_perms += [s[i] + substr_perm for substr_perm in substr_perms]
        return curr_perms

if __name__ == '__main__':
	#enter desired input string as command line parameter	
	print(get_string_perms(sys.argv[1] if len(sys.argv) > 1 else "abc"))

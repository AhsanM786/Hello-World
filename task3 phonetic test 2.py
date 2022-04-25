#test
def to_nato (words)
	nato = { "a" => "Alfa", "b" => "Bravo", "c" => "Charlie", "d" => "Delta", "e" => "Echo", "f" => "Foxtrot", "g" => "Golf", "h" => "Hotel", "i" => "India", "j" => "Juliett", "k" => "Kilo", "l" => "Lima", "m" => "Mike", "n" => "November", "o" => "Oscar", "p" => "Papa", "q" => "Quebec", "r" => "Romeo", "s" => "Sierra", "t" => "Tango", "u" => "Uniform", "v" => "Victor", "w" => "Whiskey", "x" => "Xray", "y" => "Yankee", "z" => "Zulu"}
	code = []
	words = words.downcase.split("").reject {|x| x == " "}

	words.length.times do |x|

		if Array("a".."z").include? (words[x]) then
			code << (nato[words[x]]) + " "
		else
			code << words[x] + " "
		end
	end

	code.join.chomp(" ")
end 

words = "If you, can read"
p to_nato (words)

# ---------------------------------
#     Test Run
# 

os.setlocale('rus_rus.1251')

function abc(text)
	print(#text)
	origsymbol = {}
	numsymbol = {}

	for i = 1, #text do
		s = text:sub(i, i)
		temp = 0
		for j = 1, #origsymbol do
			if s ~= origsymbol[j] then
				temp = temp + 1
			elseif s == origsymbol[j] then
				break
			end
		end
		if temp == #origsymbol then
			origsymbol[#origsymbol + 1] = s
			x = 0
			for n = 1, #text do
				stemp = text:sub(n, n)
				if s == stemp then
					x = x + 1
				end
			end
			numsymbol[#numsymbol + 1] = x
		end
	end

	numabc = ''
	for i = 1, #origsymbol do
		numabc = numabc .. origsymbol[i] .. '-' .. numsymbol[i] .. ' '
	end

	print(numabc)
end
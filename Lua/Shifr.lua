--Programma kodirovki teksta 29.01.2022 Pokid'ko Maksik Sergeevich'
os.setlocale('rus_rus.1251')

print("Ishodniy text")
text = [[
]]
--text = io.read()
print(text)

origSymbol = {}
codeSymbol = {}
codeText = ""

math.randomseed(os.time())

function rnd()
	r = string.char(math.random(14, 127))
	for i = 1, #codeSymbol do
		if r == codeSymbol[i] then
			rnd()
		end
	end
	return r
end

for i = 1, #text do
	ch = string.lower(text: sub(i, i))
	temp = 0
	for j = 1, #origSymbol do
		if ch ~= origSymbol[j] then
			temp = temp + 1
		elseif ch == origSymbol[j] then
			codeText = codeText .. codeSymbol[j]
			break
		end
	end
	if temp == #origSymbol then
		origSymbol[#origSymbol + 1] = ch
		r = rnd()
		codeSymbol[#codeSymbol + 1] = r
		codeText = codeText .. r
	end
end

print(codeText)
io.read()
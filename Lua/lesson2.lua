--26.01.2022
os.setlocale('rus_rus.1251')

x = io.read('*n')

if x == 0 then
	print('0')
elseif (x < 5 or x == 5) and x > 0 then
	print('1-5')
else
	print('another')
end

function sum(a, b)
	local c = a + b
	return(c)
end
print(sum(10, 20))
print(c)

multi = function(a, b)
	local c = a * b
return(c)
end

print(multi(5, 6))

x = io.read('*n')
--26.01.2022
--[[
Mnogostrochni'
Kommentari'
]]
os.setlocale('rus_rus.1251')

io.write('privet')
print("privet mir")
print([[
privet
mir
]])

x = 123
print(x)
print(type(x))
print(type('x'))
print(type(print))
print(type(true))
print(type(null))

--B CHISLO
y = '5' --Stroki vsegda constantu
y = tonumber(y)
print(y)
x, y = y, x
print(x, y)
print(x..y)
a, b, c = 5, 10, 20
print(a, b ,c)

x = io.read('*n')
--26.01.2022
--[[
Mnogostrochni'
Kommentari'
]]
os.setlocale('rus_rus.1251')


--print stinguet i vuvodit a io write tol'ko vuvodit
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
y = tostring(y)
print(y)
x, y = y, x
print(x, y)
print(x..y)
a, b, c = 5, 10, 20
print(a, b ,c)

print(5 ^ 2)

x = io.read('*n')
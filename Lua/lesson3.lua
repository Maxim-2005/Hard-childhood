--Math	- matematicheskaya biblioteka
--os		- biblioteka operacionnoi sistemu
--string	- rabota so strokami
--table	- rabota s tablicami

print(string.upper('aaa AAA'))
print(string.lower('aaa AAA'))
print(string.gsub('aaazaaaaa', 'z', 'x', 3))
print(string.find("Hello World", 'Wo', 1))
print(string.reverse("Hello World"))
print(string.format('Year: %d', 2022))
print(string.char(97, 98, 99, 100))
print(string.byte('abcd', 4))
print(string.byte('abcd'))
print(string.len('abracadabra'))
print(string.rep('-=*=-', 10))

print(math.random()) -- ot 0 do 1
print(math.random(100)) 
print(math.random(10, 50))

arr = {
2, 8, 15, 42, 44, 56
}
print(arr[4])
print(#arr) --dlinna massiva

arr2 = {
ppn = 'ponedelnik', 
vtor = 'vtornik', 
sred ='sreda', 
ct = 'chetverg', 
pt = 'pyatnica'
}

print(arr2.vtor)
print(arr2.vtor..arr2.sred)

table.sort(arr2)
print(#arr2)

metaArr = {}
setmetatable(arr, metaArr) -- mnojestva(znacheniy) iz massiva

x = io.read('*n')
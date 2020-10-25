program bm;

var RND, ST :word;

begin

//Create A Random Number
randomize;
RND :=random(1,1000);

repeat

//Player Choice
Write ('Введите число: ');
Read (ST);

//Check > < =
if RND>ST then Writeln ('Больше');
if RND<ST then Writeln ('Меньше');
if RND=ST then Writeln ('Вы угадали: ', RND);

until RND=ST;

end.
program P5;

uses GraphABC;

begin
  
  for var x := 0 to Window.Width -1 do
  for var y := 0 to Window.Height -1 do 
  
  SetPixel (x, y, RGB (0*x-y, x-0*y, 0*0));
  
end.
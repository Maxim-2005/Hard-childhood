program P8;

uses GraphABC;

begin
  
  onmousedown := (x, y, mb) -> moveto (x, y);
  onmousemove := (x, y, mb) -> if mb = 1 then lineto (x, y);
  
end.
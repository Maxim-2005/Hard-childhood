program P7;

uses GraphABC;

begin
  
  Pen.Color := RGB (170, 150, 0);
  
  //Солнце
  DrawCircle (200, 50, 30);
  
  //Крыша
  line (100, 100, 150, 50);
  line (200, 100, 150, 50);
  
  Pen.Color := RGB (150, 150, 150);
  
  //Стены
  DrawRectangle (200, 200, 100, 100);
  
  Pen.Color := RGB (150, 220, 240);
  
  //Окно
  DrawCircle (150, 150, 25);
  
end.
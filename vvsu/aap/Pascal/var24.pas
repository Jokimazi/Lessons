program var24;

var a, x:integer;
   error:boolean;

Begin
  error:= True;
  while error do
    begin
    write('Введите трехзначное целое число: '); readln(x);
    if (x mod 1000 = 0) and (x div ) then 
     begin
        error:= False;
      end
    else
        writeln('Введите ТРЕХЗНАЧНОЕ ЦЕЛОЕ число!!!');
    end;
  a:= (x div 10) mod 10;
  write(a);
  a:= abs(x div 100);
  write(a);
  a:= abs(x mod 10);
  write(a);
end.
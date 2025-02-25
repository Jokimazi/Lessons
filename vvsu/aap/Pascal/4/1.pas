var a,b:integer;

begin
  write('Введите первое число: '); readln(a);
  write('Введите второе число: '); readln(b);
  
  if a mod 2 = 0 then a:= 1
  else a:=0;
  if b mod 2 = 0 then b:= 1
  else b:=0;
  
  if a = 1 then writeln('Первое четное')
  else writeln('Первое нечетное');
  if b = 1 then writeln('Второе четное')
  else writeln('Второе нечетное'); 
  
  if (a= 1) and (b= 1) then writeln('Оба четные');
  if (a= 0) and (b= 0) then writeln('Оба нечетные');
end.
var a,b,c,n,d:integer;

begin
  readln(n);
  
  a:= n div 1000;
  b:= (n - a*1000) div 100;
  c:= (n - a*1000 - b*100) div 10;
  d:= n - a*1000 - b*100 - c*10;
  writeln(a);
  writeln(b);
  writeln(c);
  writeln(d);
  
  if (a+b) = (c+d) then write('Билет счастливый')
  else write('Билет не счастливый');
  
end.
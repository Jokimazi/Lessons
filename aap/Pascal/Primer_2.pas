program Primer_2;

var x, y, z:integer;

Begin
  write('Введите значение переменной X типа Integer...');
  read(x);
  write('Введите значение переменной Y типа Integer...');
  read(y);
  z:= x+y; writeln('x+y ->', z);
  z:= x-y; writeln('x-y ->', z);
  z:= x*y; writeln('x*y ->', z);
  z:= x div 2; writeln('x div 2 ->', z);
  z:= x mod 2; writeln('x mod 2 ->', z);
  writeln('x=y ->', x=y);
  writeln('x<>y ->', x<>y);
  writeln('x>=y ->', x>=y);
end.
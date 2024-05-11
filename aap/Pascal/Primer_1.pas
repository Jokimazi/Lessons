program Primer_1;

var x, y, z:real;

Begin
  write('Введите значение переменной X типа Real...');
  read(x);
  write('Введите значение переменной Y типа Real...');
  read(y);
  z:= x+y; writeln('x+y=', z);
  z:= x-y; writeln('x-y=', z);
  z:= x*y; writeln('x*y=', z);
  z:= x/y; writeln('x/y=', z);
  writeln('x=y ', x=y);
  writeln('x<>y ', x<>y);
  writeln('x>=y ', x>=y);
end.
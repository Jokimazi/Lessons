program Primer_4;

var x, y, f:real;
          z:integer;

Begin
  writeln('Значение MaxInt: ', MaxInt);
  writeln('Значение Пи: ', PI);
  write('Введиет значение аргумента: '); readln(x);
  writeln('Trunc(x)=', trunc(x));
  writeln('Int(x)=', int(x));
  writeln('Frac(x)=', frac(x));
  f:= abs(x); writeln('Значение функции abs: ', f);
  f:= sqrt(x); writeln('Значение функции sqrt: ', f);
  f:= exp(x); writeln('Значение функции exp: ', f);
  f:= ln(x); writeln('Значение функции ln: ', f);
  
  f:= sin(x); writeln('Значение функции sin: ', f);
  f:= cos(x); writeln('Значение функции cos: ', f);
  f:= arctan(x); writeln('Значение функции arctan: ', f);
  
  write('Введите значение аргумента: ');
  readln(y);
  f:= exp(y*ln(x));
  writeln('Значение функции x^y: ', f);
  
  write('Введите значение агрумента типа integer: ');
  readln(z);
  writeln('odd(z)= ', odd(z));
end.
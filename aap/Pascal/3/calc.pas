var operacij, operator1:string;
      n, m, answer:real;
      
begin
  answer:=0;
  writeln('Введите арифметическое выражение');
  writeln('(каждую часть выражения - с новой строки, например:)...');
  writeln('(первое слагаемое - одна часть)');
  writeln('(знак "+" - вторая часть)');
  writeln('(второе слагаемое - третье слагаемое - третья часть)');
  writeln('(знак "=" - четвертая часть)');
  repeat
    readln(n);
    readln(operacij);
    readln(m);
    case operacij of 
      '+': answer:=n+m;
      '-': answer:=n-m;
      '*': answer:=n*m;
      '/': answer:=n/m;
      'div': answer:=trunc(n) div trunc(m);
      'mod': answer:=trunc(n) mod trunc(m);
    end;
    readln(operator1);
  until operator1 ='=';
  writeln(n, operacij, m, operator1, answer:10:4)
end.
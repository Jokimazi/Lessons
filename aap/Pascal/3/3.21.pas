var x, a:integer;

Begin
  x:= random(100)+1;
  
  repeat
      write('Отгадайте целое число от 1 до 100: '); readln(a);
      if (a > 100) or (a < 1) then writeln('Сказано было ОТ 1 ДО 100!!!!!!')
      else begin
      if a < x then writeln('Подсказка: ваше чило меньше загананного');
      if a > x then writeln('Подсказка: ваше чило больше загананного');
      end;
  until a = x;
  writeln('Поздравляем! Вы отгадали число ', a, '!');
end.
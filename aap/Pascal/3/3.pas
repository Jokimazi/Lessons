var a, x:byte;

Begin
  x:= random(100)+1;
  write('Угадайте мое случайное заданное целое число из диапозона от 1 до 100: '); readln(a);
  repeat
    if a > x then
      begin 
        writeln('Подсказка - ваше число больше загаданного');
        write('Попробуйте еще раз: '); readln(a);
      end;
    if a < x then
      begin 
        writeln('Подсказка - ваше число меньше загаданного');
        write('Попробуйте еще раз: '); readln(a);
      end;
    until a = x;
  write('Поздравляю - вы угадали заданное число ', a, '!');
end.
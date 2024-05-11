var i, a, eng, ger, fr, nof, n:integer;

begin
  eng:=0; ger:=0; fr:=0; nof:=0;
  write('Сколько человек проходит тестирование?: '); readln(n);
  
   writeln('Какой язык вы изучаете?:');
   writeln('1 - английский');
   writeln('2 - немецкий');
   writeln('3 - французский');
   writeln('0 - никакой из выше перечисленных');
  
  for i:=1 to n do
  begin
    write('Ответ ', i, ' человека: '); readln(a);
    
    case a of
    1: eng:=eng+1;
    2: ger:=ger+1;
    3: fr:=fr+1;
    0: nof:=nof+1;
    end;
    end;
    writeln('Изучающих английский - ', eng);
    writeln('Изучающих немецкий - ', ger);
    writeln('Изучающих французский - ', fr);
    writeln('Нечего не изучающих из представленных - ', nof);
end.
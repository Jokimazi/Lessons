var s:real;
    i:integer;
  
Begin
  for i:=1 to 50 do
    begin
      s:= s + (1/i);
      writeln('1/',i);
    end;
  write(s)
end.
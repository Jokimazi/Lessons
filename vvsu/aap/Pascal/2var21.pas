var a,b,c:integer;

Begin
  write('Введите стоимость товара в магазине A: '); readln(a);
  write('Введите стоимость товара в магазине B: '); readln(b);
  write('Введите стоимость товара в магазине C: '); readln(c);
  
  if (a = b) and (b = c) then
    begin
      write('Цена на товаров в магазинах одинаковая');
      exit;
    end;
  if (a > b) and (a >c) then write('Стоимость товара из магазина A наибольшая')
  else
    begin
      if (b > a) and (b > c) then write('Стоимость товара из магазина B наибольшая')
      else write('Стоимость товара из магазина C наибольшая')
    end;
end.
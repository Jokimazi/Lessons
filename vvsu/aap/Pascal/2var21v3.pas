var a, b, c:integer;

Begin
  write('Введите стоимость товара в магазине A: '); readln(a);
  write('Введите стоимость товара в магазине B: '); readln(b);
  write('Введите стоимость товара в магазине C: '); readln(c);
  
  case a, b, c of
    (a = b) and (b = c):
    
  end;
  
  if (a = b) and (b = c) then
    begin
      write('Цена на товаров во всех магазинах одинаковая');
      exit;
    end;
  if (a = b) and (c <> a) then
    begin
      write('Цена на товары в магазинах A и B наибольшая');
      exit;
    end;
  if (a = c) and (b <> a) then
    begin
      write('Цена на товары в магазинах A и C наибольшая');
      exit;
    end;
  if (c = b) and (a <> c) then
    begin
      write('Цена на товары в магазинах C и B наибольшая');
      exit;
    end;
  if (a > c) and (a > c) then
    begin
      write('Цена на товар в магазине A наибольшая');
      exit;
    end;
  if (b > a) and (b > c) then
    begin
      write('Цена на товар в магазине B наибольшая');
      exit;
    end;
  if (c > a) and (c > b) then
    begin
      write('Цена на товар в магазине С наибольшая');
      exit;
    end;
end.
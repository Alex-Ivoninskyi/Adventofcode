Program Day1_2;
var f : text;
    s : string;
    i, ans : integer;
begin
  Assign(f, 'input.txt');
  reset(f);
  read(f, s);
  for i := 1 to length(s) do
    begin
      if s[i] = '(' then
        ans := ans + 1
      else
        ans := ans - 1;
      if ans = -1 then
      begin
        writeln(i);
        break;
      end;
    end;
end.

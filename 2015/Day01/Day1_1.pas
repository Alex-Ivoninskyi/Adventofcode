Program Day1_1;
var f: text;
    s: string;
    i, ans: integer;
begin
  Assign(f, 'input.txt');
  reset(f);
  read(f, s);
  for i:= 1 to length(s) do
    if s[i] = '(' then 
      ans:= ans + 1 
    else ans:= ans - 1;
      writeln(ans); 
end.

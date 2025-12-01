pw=0;i=50
for op in open("input.in"):s,n=op[0],int(op[1:]);o=i;i+=n*(2*(s=="R")-1);pw+=abs(i//100)+(s=="L")*((i%100==0)-(o==0));i%=100
print(pw)

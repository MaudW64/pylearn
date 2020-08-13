# print 的各種用法
name='Maud'
age=" is 22 years old."
chi=75
mat=56
eng=80
print(name+age)
print(mat, chi, eng, sep=" & ")
print("scores: ",chi+mat+eng)

print(mat, chi, eng, sep=" & ")  #沒輸入end 則默認為end="\n"

print(mat, chi, eng, sep=" & ",end="")  #輸入空白end 則代表不使用\n(不跳行)


print(mat, chi, eng, sep=" & ",end=".\n")

print(mat, chi, eng, end=".\n=================\n")

exit()
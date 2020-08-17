# for迴圈結尾 pass, break, continue

score = 80
if score >= 60:
    print('及格')
else:
    pass

# break  跳離最接近的迴圈
# continue 略過最接近的迴圈一次

for m in range(5):
    for n in range(10):
        if n == 7:
            #continue  # 此處換成break，比較差異
            break
            #pass
        print(n,end='')
    print(n,end='\n')

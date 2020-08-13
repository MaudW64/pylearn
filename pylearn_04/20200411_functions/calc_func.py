import mydef01 as my1
import mydef02 as my2

my1.line()
w1 = int(input("輸入方形的寬："))
h1 = int(input("輸入方形的高："))
sol01 = my2.qual(w1,h1)

print(sol01)


r_01 = int(input("圓的半徑："))
sol_02 = my2.circle(r_01)
area_01 = sol_02[0]
length_01 = sol_02[1]
print("輸入半徑為:{},面積為{},圓周長為:{}".format(r_01,area_01,length_01))

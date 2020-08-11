# 名目尺度：抽煙與否（類別資料）
x=c("y","n","n","y","y","n","n","y","y")  #是否抽菸
table(x)

# 飲酒偏好: 1 紅酒、2 白酒、3 黃酒、4 啤酒
drink=c(3,4,1,1,3,4,3,3,1,3,2,1,2,1,2,3,2,3,1,1,1,1,4,3,1) 
table(drink)
par(mfrow=c(1,2))
barplot(drink)           # 沒有Y軸畫圖（計數）
barplot(table(drink))    # 對Y軸畫圖（計數）

par(mfrow=c(1,2))
barplot(table(drink)/length(drink),col=1:4)     #  四種顏色：對Y軸分組頻率條狀圖
barplot(table(drink),col=c("red","yellow","blue","white"))   # 對Y軸分組頻率條狀圖（指定顏色：上色）
par(mfrow=c(1,1))



#圓餅圖
drink.count=table(drink)    # Y軸資料分組後指定值給drikn.count
par(mfrow=c(1,3))
pie(drink.count)
names(drink.count)=c("wine","wite","yellow","beer")
pie(drink.count)
pie(drink.count,col=c("purple","green","cyan","white"))
par(mfrow=c(1,1))



#比例尺度（連續資料）
library(readxl)
MS=read.table("mathstat.txt",head=T)
MS
head(MS)
dim(MS)

View(MS) 
attach(MS)
names(MS) 

#直方圖
hist(MS$maths)
hist(MS$stats)

#莖葉圖
stem(MS$stats)
stem(MS$maths)

#四分位數
summary(MS$maths)
summary(MS$stats)

# 
EDA <- function (x)
{ 
  par(mfrow=c(2,2))            #同時繪製四張圖         
  hist(x)                      #直方圖  
  dotchart(x)                  #點圖  
  boxplot(x,horizontal=T)      #箱式圖  
  qqnorm(x);qqline(x)          #常態機率圖  
  par(mfrow=c(1,1))            #還原單張圖  
}

EDA(MS$maths)
EDA(MS$stats)



#收入 
pays<-c(1500,2500,5000,5200,5500,5600,5700,5800,5850,5850,5900,5950,6500,80000)
mean(pays)
summary(pays)
boxplot(pays)
mean(pays,trim=0.1)

# 非常態分配處理
pay=c(11,19,14,22,14,28,13,81,12,43,11,16,31,16,23,42,22,26,17,22,
      13,27,108,16,43,82,14,11,51,76,28,66,29,14,14,65,37,16,37,35,
      39,27,14,17,13,38,28,40,85,32,25,26,16,12,54,40,18,27,16,14,
      33,29,77,50,19,34)
EDA(pay)
log.pay =log10(pay)   
EDA(log.pay)



# 集中與分散程度
salary=c(2000,2100,2200,2300,2350,2450,2500 ,2700,2900,2850,3500,3800,2600,
         3000,3300,3200,4000,3100,4200)
mean(salary)            # 平均數
median(salary)          # 中位數
var(salary)             # 變異數
sd(salary)              # 標準差
fivenum(salary)         # 五分法
summary(salary)         # 四分位與最大最小
IQR(salary)             # 第三分位與第一分位差距

salaryg=cut(salary,breaks=c(2000,3000,4000,max(salary)))
table(salaryg)          # 2000~3000、3000~4000、4000以上

par(mfrow=c(1,2))
hist(salary)            # 直方圖：薪資的頻率計數
hist(salary,prob=T)     # 直方圖：薪資的頻率直方圖
rug(salary)             # 分組寫在圖上

par(mfrow=c(1,1))      
par(mfrow=c(1,2))
boxplot(salary)               # 箱式圖
boxplot(salary,horizontal=T)
par(mfrow=c(1,1))


# faithful是R的內建資料，主要是火山爆發與等待時間的資料 
hist(faithful$eruptions,prob=T,breaks=25)          # 密度函數圖
lines(density(faithful$eruptions),col='red')

# 離群值
salarym=c(salary,15000)    # 新增一筆離群
boxplot(salarym)           # 箱式圖

boxplot.stats(x,coef=1.5, do.conf=TRUE, do.out=TRUE)    # 箱式圖的值stats由5個值，箱式圖下虛線、第二個值是Q1，第三是中位數、第四個是Q3，最後一個是上虛線
boxplot.stats(salarym)  


##Grubb test 檢定離群值
install.packages("outliers")
library(outliers)
set.seed(5)
x = rnorm(10)       ##隨機模擬標準常態分配10個數字
x
grubbs.test(x)
grubbs.test(x,type=10)       # type=10檢驗一個離群值，預設值
grubbs.test(x,type=11)       # type=11檢驗兩邊兩個離群值
grubbs.test(x,type=20)       # type=20尾部檢驗兩個離群值
grubbs.test(x,opposite=TRUE)  # opposit檢驗反方向離群值


##Dixon Q test檢定離群值
set.seed(8)
x=rnorm(10)
x
dixon.test(x)
dixon.test(x,opposite=TRUE)
dixon.test(x,type=10)



###############################
### two variables
smoke=c("Y","N","N","Y","N","Y","Y","Y","N","Y")
study=c(1,2,2,3,3,1,2,1,3,2)
smoke=c("Y","N","N","Y","N","Y","Y","Y","N","Y")
study=c("<5h","5-10h","5-10h",">10h",">10h","<5h","5-10h","<5h",">10h","5-10h")
table(smoke,study)
tab=table(smoke,study)
View(tab) 

prop.table(tab,1) #各資料佔列的比率（列相加為1)
prop.table(tab,2) #各資料佔欄的比率（欄相加為1)
prop.table(tab)   #各資料佔總和的比率（總計相加為1)

##條狀圖
par(mfrow=c(1,3))
barplot(table(smoke,study))     
barplot(table(study,smoke))     
barplot(table(study,smoke),beside=T,legend.text=c("<5h","5-10h",">10"))
legend()
par(mfrow=c(1,1))




##分析兩組藥物使用前後：資料分兩欄
x=c(5,5,13,7,11,11,9,8,9)    ##實驗組
y=c(11,8,4,5,9,5,10,5,4,10)  ##對照組
boxplot(x,y)
##分析兩組藥物使用前後：資料用1欄，加上代號
d=c(5,5,5,13,7,11,11,9,8,9,11,8,4,5,9,5,10,5,4,10)
g=c(1,1,1, 1,1, 1, 1,1,1,1, 2,2,2,2,2,2, 2,2,2, 2)
boxplot(d~g)

#分析財政收入收入（yy）、稅收（xx）資料
yx=read.table("reg1.txt",header=T)
yx
data.entry(c(yx))
plot(xx,yy)                
abline(lm(yy~xx))  
cor(xx,yy)
cor(yy,xx)

cor(yx$xx,yx$yy,method="spearman")
cor(rank(yx$xx),rank(yx$yy))
plot(xx,yy) 



# Cars93包括27個變數，價格分成經濟型、普通型、奢侈型，
install.packages("MASS")
library(MASS)
data(Cars93)
dim(Cars93)
attach(Cars93)
names(Cars93)

price=cut(Price,c(0,12,20,max(Price)))        # 價格分成0-12、12-20、20-最大
table(price)
levels(price)=c("cheap","okay","expensive")   # 價格分成經濟型、普通型、奢侈型
table(price)
mpg=cut(MPG.highway,c(0,20,30,max(MPG.highway)))   #  公里數換0-20、20-30、30-最大
table(mpg)
levels(mpg)=c("gas guzzler","oky","miser")     # 高速公路每加侖的公里數換成耗油、普通、省油
table(mpg)

table(Type)       # 分析Type欄位與價格、公里數的關係                     
table(price,Type)
table(price,mpg)
table(price,Type,mpg)

par(mfrow=c(1,2))
barplot(table(price,Type))            # 分析條狀圖
barplot(table(price,Type),beside=T)

barplot(table(Type,price))
barplot(table(Type,price),beside=T)
par(mfrow=c(1,1))


boxplot(Price~Type)        # 箱線圖
r1=rnorm(1000)
f1=factor(rep(1:10,100))
boxplot(r1~f1)
stripchart(Type~price)    # 點帶圖


# 散佈圖
iris
head(iris)
levels(iris$Species)
iris.lab = rep(c("1","2","3"),rep(50,3))

par(mfrow=c(1,2))    
plot(iris[,1],iris[,3],type="n")      # 第1欄與第3欄散佈圖 type是否要顯示點
text(iris[,1],iris[,3],cex=0.6)       # cex縮小字體
plot(iris[,1],iris[,3],type="n") 
text(iris[,1],iris[,3],iris.lab,cex=0.7)  
par(mfrow=c(1,1)) 

pairs(iris)               #所有欄位
pairs(iris[,1:4])         #第1欄位到第4欄位

pairs(iris[1:4],pch=21,bg=iris.lab)
pairs(iris[1:4],pch=21, bg=c("red", "green3", "blue")[unclass(iris$Species)])

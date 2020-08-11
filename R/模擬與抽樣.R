install.packages("lattice")       
install.packages("MASS")                                     
install.packages("nnet")                                      
library(lattice)                                            
library(MASS)                                        
library(nnet)   

install.packages("mice")
library(mice)
data(nhanes2)     #nhanes2資料
nrow(nhanes2);ncol(nhanes2)  
summary(nhanes2)   #age年齡、bmi、hyp 是否有高血壓、 chl膽固醇
head(nhanes2)      #輸出前六筆

###遺漏值處理
sum(is.na(nhanes2))    #計算遺漏值
sum( complete.cases(nhanes2))  #計算完整值
md.pattern(nhanes2)    #有多少樣本是遺漏、1表示沒有遺漏、最後一欄表示各個變數遺漏的變數計數

#方法1:刪除

#方法2:插補法
imp=mice(nhanes2,m=4)       #mice函數，產生4個完整資料
fit=with(imp,lm(chl~age+hyp+bmi))  #mice函數，用三個變數去預測資料
pooled=pool(fit)                  
summary(pooled) 

#插補法：
sub=which(is.na(nhanes2[,4])==TRUE) #第四個欄位中有缺值的行
dataTR=nhanes2[-sub,]               #第四個欄位中沒有缺值的資料
dataTE=nhanes2[sub,]                #第四個欄位中有缺值的資料
#抽樣法
dataTE[,4]=sample(dataTR[,4],length(dataTE[,4]),replace=T) #在非遺漏值抽樣填寫回去
dataTE
#平均法
dataTE[,4]=mean(dataTR[,4])
dataTE
#回歸法
lm=lm(chl~age,data=dataTR)
nhanes2[sub,4]=round(predict(lm,dataTE))
head(nhanes2)
#熱平台插補：找一個與遺漏值相近的樣本，利用觀察值進行插補
accept=nhanes2[which(apply(is.na(nhanes2),1,sum)!=0),]  #遺漏值的樣本
donate=nhanes2[which(apply(is.na(nhanes2),1,sum)==0),]  #無遺漏值的樣本
accept[1,]
donate[1,]
accept[2,]
sa=donate[which(donate[,1]==accept[2,1]&donate[,3]==accept[2,3]&donate[,4]==accept[2,4]),]
sa
accept[2,2]=sa[1,2]
accept[2,]
#冷平台插補：資料分層，使用平均法進行插補
leve11=nhanes2[which(nhanes2[,3]=="yes"),]
leve11
leve11[4,4]=mean(leve11[1:3,4])
leve11




# 模擬
# 均勻分配
n=10
runif(n,min=0,max=1)

set.seed(1)
n=100
x=runif(n,min=0,max=1)
hist(x,prob=T,main="均勻分配")  # 長條圖
curve(dunif(x,0,1),add=T)     # 在長條圖上新增均勻分配線

#常態分配
n=100        # 樣本數
mu=0      # 平均數
sigma=1      # 標準差
x=rnorm(n,mu,sigma)
hist(x,prob=T,main="標準常態分配 平均數=0, 標準差=1")  # 長條圖
curve(dnorm(x),add=T)      # 在長條圖上新增標準常態分配線

#指數分配
n=100           # 樣本數
exp=1/10        # 指數分配中，入為10，為均值的倒數
x=rexp(n,exp)   # rexp()模擬n的樣本，lamda=10
hist(x,prob=T,col=gray(0.9), main="均值為10的指數分配")  # 長條圖
curve(dexp(x,1/10),add=T)      # 在長條圖上新增指數分配線



# 均勻分配取log 與指數分配比較
Nsim=10^4
U=runif(Nsim)
 
X=-log(U)     # log
Y=rexp(Nsim)  # exp
   
par(mfrow=c(1,2))  #比對

hist(X,freq=F,main="均勻分配取對數")
curve(dexp(x,1),add=T,col="red")

hist(Y,freq=F,main="指數分配模擬")
curve(dexp(x,1),add=T,col="red")



# 二項分配是離散 隨著n的次數增加，趨近常態分布 
par(mfrow=c(1,3))
p=0.25
for(n in c(10,20,50))   # n為10，20，50
{  x=rbinom(100,n,p) 
    hist(x,prob=T, main=paste("n=",n)) 
    xvals=0:n                          
 	points(xvals,dbinom(xvals,n,p),type="h",lwd=3) 
}
par(mfrow=c(1,1))







# 抽樣
# 隨機抽樣 （抽出放回）
sample(c("H","T"),10,rep=T)

# bootstrap抽樣 （依照原始資料為基礎，模擬抽樣）
faithful   # 讀入內建資料 eruptions變數為紀錄火山爆發的時間
attach(faithful)   # 資料設定

sample(eruptions,10, replace=T)      #抽要樣本數為10
Sample=sample(eruptions, 1000,rep=T) #抽要樣本數為1000的bootsrtap養本

par(mfrow=c(1,2))
hist(eruptions,breaks=25)
hist(Sample,breaks=25)

par(mfrow=c(1,1)) 




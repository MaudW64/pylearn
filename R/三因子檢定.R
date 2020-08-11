#單因子變異數分析
PlantGrowth  # PlantGrowth植物生長資料，分為對照組、實驗組一、實驗組二，每組10樣本
oneway.test(weight ~ group, data=PlantGrowth, var.equal=T) # 檢定三組平均數
anova(lm(weight ~ group, data=PlantGrowth))                # 可用anova函數
summary(lm(weight ~ group, data=PlantGrowth))
aov(weight ~ group, data=PlantGrowth)                       # 可用aov函數
summary(aov(weight ~ group, data=PlantGrowth))

#雙因子變異數分析：沒有交互作用
range=c(582,562,653,491,541,516,601,709,392,758,582,487) # 火箭射程
A=c(1,1,1,2,2,2,3,3,3,4,4,4)                             # 4種燃料
B=c(1,2,3,1,2,3,1,2,3,1,2,3)                             # 3種推進器

# 火箭射程散佈圖
 plot(range~A,pch=B)
  legend(1.5,750,legend=1:3,pch=B)

# 火箭各因子箱線圖
par(mfrow=c(1,2))
  boxplot(range~A,xlab="A"); boxplot(range~B,xlab="B") 
  par(mfrow=c(1,1))

# 火箭射程雙因子檢定
A = factor(A) ; B = factor(B)
range.aov <- aov(range ~ A + B )
 summary(range.aov)
summary(aov(range ~ A + B ))


#雙因子變異數分析：有交互作用
#提高原料利用率：供給速度、濃度兩因子
Y=c ( 60.7,61.1,61.5,61.3,61.6,62.0,61.7,61.1,61.5,60.8,61.7,61.2, 62.2,62.8,62.1,61.7,
      60.6,60.3,60.6,61.0,61.4,61.5,60.7,60.9)
A=c(1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3)
B=c(1,1,2,2,3,3,4,4, 1,1,2,2,3,3,4,4, 1,1,2,2,3,3,4,4) 
A=factor(A); B=factor(B)
summary(aov(Y~A+B+A*B))

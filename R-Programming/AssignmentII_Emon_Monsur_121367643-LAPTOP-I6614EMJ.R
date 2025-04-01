rm(list = ls())
library(lpSolve)


#(i)
u <- c(36, 40, 32, 43, 29,
       28, 27, 29, 40, 38,
       34, 35, 41, 29, 55,
       41, 42, 35, 27, 36,
       25, 28, 40, 34, 38,
       31, 30, 43, 40, 38)
b <- c(72, 115, 82, 28, 91, 63, 19, 61, 82, 18, 20)
A <- rbind(c(rep(1,5),rep(0,25)),
           c(rep(0,5),rep(1,5),rep(0,20)),
           c(rep(0,10),rep(1,5),rep(0,15)),
           c(rep(0,15),rep(1,5),rep(0,10)),
           c(rep(0,20),rep(1,5),rep(0,5)),
           c(rep(0,25),rep(1,5)),
           rep(c(1,0,0,0,0),6),
           rep(c(0,1,0,0,0),6),
           rep(c(0,0,1,0,0),6),
           rep(c(0,0,0,1,0),6),
           rep(c(0,0,0,0,1),6))
dir <- c(rep("<=",6),rep(">=",5))
o=lp(direction = "min",objective.in = u,const.mat = A,const.dir = dir,const.rhs = b)
o$status
o$objval
o$solution

#solve with lp.transport
bs=c(72, 115, 82, 28, 91, 63); bd=c(19, 61, 82, 18, 20)
o=lp.transport(cost.mat = matrix(u,nrow = 6,byrow = T),direction = "min",row.signs = rep("<=",6),row.rhs = bs,col.signs = rep(">=",5),col.rhs = bd,integers = F)
colnames(o$solution)=c("A","B","C","D","E"); rownames(o$solution)=c("1|","2|","3|","4|","5|","6|")
o$status
o$solution
o$objval

#(ii)
x=matrix(u,nrow=6,byrow=T)
colnames(x)=c("A","B","C","D","E"); rownames(x)=c("1|","2|","3|","4|","5|","6|")
print(x)

xx=matrix(b,nrow=1,byrow=T)
print(xx)

#A-coefficients for Retail Outlets and Supplier Depot
xy=matrix(A,nrow=11,byrow=T)
print(xy)

#
# now Solve as an Lp Problem
#
dir <- c(rep("<=",6),rep(">=",5))
o=lp("min", u, A, dir, b); soln=o$solution; print(o$objval)


x=matrix(soln,nrow=6,byrow=T)
colnames(x)=c("A","B","C","D","E"); rownames(x)=c("1|","2|","3|","4|","5|","6|")
print(x) #best solution

#worst allocation
o=lp("max", u, A, dir, b); soln=o$solution ; print(o$bjval)

x = matrix(soln,nrow=6,byrow=T)
colnames(x)=c("A","B","C","D","E"); rownames(x)=c("1|","2|","3|","4|","5|","6|")
print(x) #(worst solution)


#(iii)
u <- c(36, 40, 32, 43, 29,
       28, 27, 29, 40, 38,
       34, 35, 41, 29, 55,
       41, 42, 35, 27, 36,
       25, 28, 40, 34, 38,
       31, 30, 43, 40, 38)
b <- c(72, 115, 82, 28, 91, 63, 19, 61, 82, 18, 20)
A <- rbind(c(rep(1,5),rep(0,25)),
           c(rep(0,5),rep(1,5),rep(0,20)),
           c(rep(0,10),rep(1,5),rep(0,15)),
           c(rep(0,15),rep(1,5),rep(0,10)),
           c(rep(0,20),rep(1,5),rep(0,5)),
           c(rep(0,25),rep(1,5)),
           rep(c(1,0,0,0,0),6),
           rep(c(0,1,0,0,0),6),
           rep(c(0,0,1,0,0),6),
           rep(c(0,0,0,1,0),6),
           rep(c(0,0,0,0,1),6))
dir <- c(rep("<=",6),rep(">=",5))


o=lp( "min", u, A, dir, b, compute.sens=1); soln=o$solution
o$solution

ds=seq(-3,3,length=200); fs=NULL
for(k in 1:30) {  ffs=NULL;for(d in ds) {  un=u ; un[k]=u[k]+d; o=lp("min", un, A, dir, b); solnn=o$solution
ffs=c(ffs,100*sum(sum(solnn*un-soln*un)/sum(solnn*un))) }
fs=cbind(fs,ffs) }


matplot(ds,fs,type="l",lty=c(1),main="Sensitivity of Lp Solution to cost changes (one-at-a-time)",
        ylab="% Deviation from Prmal Optimal",xlab="cn_j= c_j", lwd=1.5)
legend("center",legend=as.character(c(1:30)),col=c(1:30),pch=16); abline(h=0,lty=c(2))


u <- c(5,4,3,5,4,3)
b <- c(28,25,-20,-10,-14,0,0,0)
A <- rbind(c(1,1,1,0,0,0),c(0,0,0,1,1,1),
           c(-1,0,0,-1,0,0),c(0,-1,0,0,-1,0),
           c(0,0,-1,0,0,-1),c(1,0,0,-1,0,0),
           c(0,1,0,0,-1,0),c(0,0,-1,0,0,3))
dir <-rep("<=",8)

o=lp("max", u, A, dir, b, compute.sens=1); soln=o$solution
o$solution

ds=seq(-3,3,length=200); fs=NULL
for(k in 1:6) {  ffs=NULL;for(d in ds) {  un=u ; un[k]=u[k]+d; o=lp("max", un, A, dir, b); solnn=o$solution
ffs=c(ffs,100*sum(sum(solnn*un-soln*un)/sum(solnn*un))) }
fs=cbind(fs,ffs) }


matplot(ds,fs,type="l",lty=c(1),main="Sensitivity of Lp Solution to cost changes (one-at-a-time)",
        ylab="% Deviation from Primal Optimal",xlab="cn_j - c_j", lwd=1.5)
legend("center",legend=as.character(c(1:6)),col=c(1:6),pch=16); abline(h=0,lty=c(2))


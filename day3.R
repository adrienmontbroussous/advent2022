library(data.table)
library(stringr)
myCon = file(description = "day3.txt", open="r", blocking = TRUE)
input=readLines(myCon)
input3<-data.table(V1=input)

input3[,nb:=nchar(V1)]
input3[,firstc:=substring(V1,1,nb/2)]

input3[,secondc:=substring(V1,nb/2+1,nb)]
input3[1]$V1
input3[1]$firstc
input3[1]$secondc
trouver_intru <- function(chaine1, chaine2) {
  i = 1
  j = 1
  found = FALSE
  while (found == FALSE) {
    print(i)
    print(length(chaine1))
    print(chaine1)
    print(substr(chaine1, i, i))
    if (str_detect(string=chaine2,pattern= substr(chaine1, i, i))[1]) {
      j = i
      found = TRUE
    } else {
      i = i + 1
    }
  }
  return(substring(chaine1, j, j))
  rm(j)
}

input3[,intru:=mapply(trouver_intru,input3$firstc,input3$secondc)]
input3$intru


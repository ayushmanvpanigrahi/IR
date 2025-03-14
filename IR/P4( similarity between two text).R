install.packages("tm")
install.packages("ggplot2")
install.packages("textreuse")
install.packages("devtools")
install.packages("NLP")

library("tm")
require("NLP")


PATH = "D://File_Download//Demo-Projects//Practical//IR//Rstudio//Text"
my.corpus<-Corpus(DirSource(PATH))

my.corpus<-tm_map(my.corpus,removeWords,stopwords(kind="english"))
my.tdm<-TermDocumentMatrix(my.corpus)
my.df<-as.data.frame(inspect(my.tdm))
barplot(as.matrix(my.tdm)) 

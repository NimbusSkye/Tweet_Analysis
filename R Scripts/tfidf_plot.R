library(tidyverse)
library(here)
library(ggplot2)
library(gridExtra)

data=read_csv(here("tfidf.csv"))
cats=c('mv','pv','gv','c','pc','cd','cs','ot')
p=list()

for (i in 1:8) {
  sub=data%>%filter(category==cats[i])
  p[[i]]=ggplot(sub,aes(tfidf,reorder(word, tfidf),fill=tfidf))+
    geom_bar(stat='identity') +
    ggtitle(paste("Top words in",cats[i])) +
    ylab("word") + 
    theme_grey(base_size=17)
}

grid.arrange(grobs=p,ncol=2)
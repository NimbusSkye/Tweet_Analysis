library(ggplot2)
library(tidyverse)
library(here)

annotated_1000_combined=read_csv(here("annotated_1000_combined.csv"))
sentiment_by_coding=annotated_1000_combined%>%
  group_by(coding,sentiment)%>%
  summarise(n=n(),.groups="keep")%>%
  ungroup(sentiment)%>%
  mutate(percent=n/sum(n))

sentiment_by_coding$percent=sentiment_by_coding$percent%>%round(digits=2)

ggplot(sentiment_by_coding, aes(x=coding, y=n, fill=sentiment)) +
  geom_bar(stat="identity", position="stack") +
  ylab("Count") +
  xlab("Category") +
  ggtitle("Sentiments by Category") +
  labs(fill='Sentiment') +
  geom_text(aes(label = paste0(percent*100,"%")), 
           position = position_stack(vjust = 0.5), size = 2)
library(tidyverse)


xs <- seq(0, 10, by = 0.1)
ys <- seq(20, 0, by = -0.2 )
ds <- cbind(xs, ys)

ggplot(ds, aes(x = xs, y = ys)) + geom_line()+ 
geom_point()+
labs(x = "Knowledge on Energy Usage",
    y = "Energy Usage")+
    theme_bw()

ggsave("energy_use.png", width = 6, height = 4)

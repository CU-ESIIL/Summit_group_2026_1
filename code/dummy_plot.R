library(tidyverse)


xs <- seq(0, 10, by = 0.1)
ys <- seq(20, 0, by = -0.2 )
ys <- ys + rnorm(length(xs), mean = 0, sd = 1)
ds <- cbind(xs, ys)

ggplot(ds, aes(x = xs, y = ys)) + geom_smooth()+ 
geom_point()+
labs(x = "Knowledge on Energy Usage (Unit of Knowledge)",
    y = "Energy Usage (Unit of Energy Usage)",
    title = "Team <5'9 Analysis of Energy Knowledge and Energy Usage")+
    theme_bw()

ggsave("docs/assets/figures/energy_use.png", width = 6, height = 4)

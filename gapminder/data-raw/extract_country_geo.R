library(here)
library(tidyverse)

area <- read.csv(here("data-raw", "country_area.txt"), header = TRUE, sep = "\t")
latlong <- read.csv(here("data-raw", "country_latlong.txt"), header = TRUE, sep = "\t")

country_geo <- left_join(area, latlong, by = "country") %>%
  select(country, latitude, longitude, area)

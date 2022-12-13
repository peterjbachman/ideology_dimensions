library(ggplot2)
library(data.table)

# Read in data
df <- fread("data/summed_sim_data_01.csv")

# Subset data to one session for some testing
df_102 <- df[session == 101 & party %in% c("D", "R")]
df_102

ggplot(data = df_102, aes(x = party, y = mean_sim)) +
  geom_point()

df$name <- paste(df$firstname, df$lastname)

test <- df[party == "D", .(count = .N, mean_sim = mean_sim, session = session),
  by = .(name)
]
df_test <- test[count > 19]

ggplot(data = df_test, aes(x = session, y = mean_sim, color = name)) +
  geom_line() +
  theme_minimal()


df_grouped_party <- df[party %in% c("D", "R"),
  .(mean_sim = mean(mean_sim)),
  by = .(session, party)
]
df_grouped_party

ggplot(data = df_grouped_party, aes(x = session, y = mean_sim, color = party)) +
  geom_line()

df_grouped_chamber <- df[party == "D",
  .(mean_sim = mean(mean_sim)),
  by = .(session, chamber)
]
df_grouped_chamber

ggplot(data = df_grouped_chamber, aes(x = session, y = mean_sim, color = chamber)) +
  geom_line()
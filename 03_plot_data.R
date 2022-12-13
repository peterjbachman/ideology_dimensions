library(ggplot2)
library(ggthemes)
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
df_test <- df_test[name %in% unique(df_test$name)[1:4]]

# Plots of some legislators that show up more than 19 times.
ggplot(data = df_test, aes(x = session, y = mean_sim, color = name)) +
  geom_line() +
  labs(
    x = "Session of Congress",
    y = "Similarity to Universalism or Populism",
    color = "Name of Legislator"
  ) +
  theme_clean()

# Plots grouped by Party
df_grouped_party <- df[party %in% c("D", "R"),
  .(mean_sim = mean(mean_sim)),
  by = .(session, party)
]

ggplot(data = df_grouped_party, aes(x = session, y = mean_sim, color = party)) +
  geom_line() +
  labs(
    x = "Session of Congress",
    y = "Similarity to Universalism or Populism",
    color = "Political Party"
  ) +
  theme_clean() +
  scale_color_gdocs(labels = c("Democrat", "Republican"))

# Plots grouped by chamber in Democratic Party
df_grouped_chamber <- df[party == "D",
  .(mean_sim = mean(mean_sim)),
  by = .(session, chamber)
]

ggplot(
  data = df_grouped_chamber,
  aes(x = session, y = mean_sim, color = chamber)
) +
  geom_line() +
  labs(
    x = "Session of Congress",
    y = "Similarity to Universalism or Populism",
    color = "Legislative Chamber"
  ) +
  theme_clean() +
  scale_color_few(labels = c("House", "Senate"))

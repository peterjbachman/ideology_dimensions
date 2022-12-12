library(data.table)

# Quickly rename the session properly
for (i in 82:102) {
  path <- paste0("data/session_", i, "_sim.csv")
  df <- fread(path)
  df$session <- i
  fwrite(df, path)
}

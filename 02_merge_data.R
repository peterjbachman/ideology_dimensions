library(dplyr)
library(data.table)


# Quickly rename the session properly
for (i in 82:102) {

  # Generate paths to files
  path_sim <- paste0("data/session_", i, "_sim.csv")
  if (i < 100) {
    session <- paste0("0", i)
  } else {
    session <- i
  }
  path_speak <- paste0(
    "/Users/peter/Data/floor_speech/hein-bound/",
    session,
    "_SpeakerMap.txt"
  )

  # Load in files
  df_sim <- fread(path_sim)
  df_speak <- fread(path_speak)

  # Merge data
  df_merge <- merge(df_sim, df_speak, by = "speech_id")

  # Average out the Similarity to the dimension
  df_sum <- df_merge %>%
    group_by(speakerid) %>%
    summarise(
      mean_sim = mean(similarity)
    )

  # Simplify Speaker Data to merge
  df_speak_simp <- df_speak %>%
    select(!speech_id) %>%
    unique()

  # Create final merge, bind it to total dataset
  df_session <- merge(df_sum, df_speak_simp, by = "speakerid") %>%
    mutate(
      session = i
    )

  if (i == 82) {
    df_final <- df_session
  } else {
    df_final <- rbind(df_final, df_session)
  }

  if (i == 102) {
    fwrite(df_final, "data/summed_sim_data_01.csv")
  }
}

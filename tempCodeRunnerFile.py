while True:
    # # if 1:
    #     query = takeCommand().lower()                 # Logic for executing tasks based on query why we are taking in lower case bcoz queries
    #    # also so that Query will be easily matched, are there in lower case and Queries will be recognized in the lower case only
    #     if 'wikipedia' in query:
    #         speak('Searching Wikipedia...')
    #         query = query.replace("wikipedia", "")
    #         results = wikipedia.summary(query, sentences=2)             # return two results and sentences
    #         speak("According to Wikipedia")
    #         print(results)       # Also print the results
    #         speak(results)

    #     elif 'open youtube' in query:
    #         webbrowser.open("youtube.com")

    #     elif 'open google' in query:
    #         webbrowser.open("google.com")

    #     elif 'open stackoverflow' in query:
    #         webbrowser.open("stackoverflow.com")   

    #     elif 'play music' in query:
    #         music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'      # Address of the folder
    #         songs = os.listdir(music_dir)             # os.listdir will list all the directories in one list
    #         print(songs)    
    #         os.startfile(os.path.join(music_dir, songs[0]))        # sing the songs, also we can add mp3 folder type
    #                           # songs[0] will sing songs as randomly suprise will create

### Project idea: Personalized Spotify Playlist Stats & Quiz: Spot your Spotify.

A package that contains two subpackages: stats and quiz. Stats allows users to gain insights about their Spotify playlist such as top artist, longest song, slowest song, etc. Quiz allows users to enter a game where they will be questioned on how well they know their playlist. The program will read a CSV file of the user playlist that users can obtain using Exportify.

**Package**: spotyourspotify
  - **Subpackage**: stats: contains all the code for parsing and analysing playlist

    - **Module**: readdata: for parsing the playlist

      - **Functions**: 
        - readdata: converting csv file input to dataframe
        - showtable: displays input dataframe (mainly for troubleshooting)
        - cleandata: fixes any potential issues with dataframe (NA values, bad values, etc)
        - properties: various functions that return information about the playlist/songs
        - getsong: functions to get song as an object by index, or by song id, or randomly, depending on context

    - **Module**: showstats: contains the code for analysing playlist and giving fun stats

      - **Functions**: 
        - toplabel/topartist/topgenre: returns most represented record label, artist, or genre in the playlist
        - longestsong/shortestsong: returns longest or shortest song based on duration column
        - fastestsong/slowestsong: returns fastest or shortest song based on tempo column
        - showallstats: returns a list of various stats

  - **Subpackage**: quiz: contains modules and functions to build and run the quiz for the user based on their playlist stats.

    - **Module**: makequiz: build the quiz with question libraries

      - **Functions**: 
        - getdata: randomly choose 4 song and its corresponding data (artist, album, record, length, etc.)
        - makequestion: make a question based on the data
            - artist_question: make a question like "Which these artists performs song X?"
            - length_question: make a question like "Which of these songs is the longest?"
            - age_question: make a question like "Which of these songs is the oldest?"
            - tempo_question: make a question like "Which of these songs is the slowest?"
        - check_answer: checks the user's input and compare it to the corresponding data.

    - **Module**: playgame: run the quiz

      - **Functions**: 
        - getoptions: shows the available options that users can choose during a quiz including question types, start quiz, end quiz.
        - setseed: ask users to optionally set seed for reproducibility of questions.
        - playgame: starts the quiz
        - getscore (optional): shows the user's score
        - scoreboard (optional): stores the user's score

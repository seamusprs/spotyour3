import random
from stats import readdata as rd

class Question:
    """
    A class for a question in the quiz game.

    The Question class allows for questions to be built based on the current playlist.
    It includes functions for fetching songs, checking the desired question type,
    and checking the validity of answers.

    Parameters
    ----------
    playlist : Playlist
        An instance of the 'Playlist' class that holds the playlist currently being quizzed on.

    Attributes
    ----------
    cur_question : str
        A string containing the question being asked of the user.
    cur_options : list of str
        A list of strings containing four possible solutions to the question (one correct).
    cur_solution :
        A string containing the correct answer to the question being asked.

    Methods
    -------
    getdata(num_song=4):
        Builds a list of songs randomly selected from the playlist, used as options when generating questions.
    makequestion(question_type : str):
        Takes the desired question type as an argument, calls the appropriate question type function,
        and returns the question information (question, options, and solution).
    checker(user_input, solution):
        Compares the user input answer to the correct solution and returns True if correct, false otherwise.
    """
    def __init__(self, playlist):
        self.playlist = playlist
        self.cur_question = None
        self.cur_options = None
        self.cur_solution = None
        
    def getdata(self, num_song = 4):
        """Builds a list of songs randomly selected from the playlist, used as options when generating questions."""
        try:
            if num_song > self.playlist.length:
                raise ValueError("Number of song request is more than the size of the playlist")
            idx = random.sample(range(self.playlist.length), num_song)
            song_list = []
            for i in idx:
                try:
                    song_list.append(rd.Song(self.playlist, id=i))
                except Exception as ex:
                    raise InvalidPlaylist(f"Unable to access song data: {ex}")
            return song_list
        except ValueError as ex:
            raise ex
        except InvalidPlaylist as ex:
            raise ex
        except Exception as ex:
            raise RuntimeError(f"Error in 'getdata': {ex}")
    
    def makequestion(self, question_type):
        """Takes the desired question type as an argument, calls the appropriate question type function,
        and returns the question information (question, options, and solution)."""
        qtype_def = f"{question_type}_question"
        if not hasattr(self, qtype_def):
            raise ValueError(f"Invalid question type: {qtype_def}")
        q, o, s = getattr(self, qtype_def)()
        self.cur_question = q
        self.cur_options = o
        self.cur_solution = s
        return q, o, s
    
    def checker(self, user_input, solution):
        """Compares the user input answer to the correct solution and returns True if correct, false otherwise."""
        return user_input == solution

    def __str__(self):
        if not self.cur_question:
            return "No question has been generated"
        generated_q = f"Question: \n{self.cur_question} \n\nOptions:\n"
        for i in self.cur_options:
            generated_q += f"{i} \n"
        generated_q += f"\nSolution: {self.cur_solution}"
        return generated_q
    
class QuestionBuilder(Question):
    """
    A class for different question types in the quiz game.

    Inherits from the Question class and includes methods for various types of questions.

    Methods
    -------
    artist_question():
        Builds a question identifying a song's artist.
    label_question():
        Builds a question identifying a song's record label.
    length_question():
        Builds a question comparing song lengths.
    age_question():
        Builds a question comparing song release dates.
    tempo_question():
        Builds a question comparing song tempos (BPM).
    """
    def artist_question(self):
        """Builds a question identifying a song's artist."""
        try:
            data = self.getdata()
            song = random.choice(data)
            question = f"Which artist performs the song '{song.track}'?"
            options = []
            options.append(song.artist)
            for i in data:
                if i.artist != song.artist:
                    options.append(i.artist)
            random.shuffle(options)
            return question, options, song.artist
        except Exception as ex:
            raise RuntimeError(f"Error in 'age_question': {ex}")
    
    def label_question(self):
        """Builds a question identifying a song's record label."""
        try:
            data = self.getdata()
            song = random.choice(data)
            question = f"Which label publishes the song '{song.track}'?"
            options = []
            options.append(song.label)
            for i in data:
                if i.label != song.label:
                    options.append(i.label)
            random.shuffle(options)
            return question, options, song.label
        except Exception as ex:
            raise RuntimeError(f"Error in 'label_question': {ex}")
    
    def length_question(self):
        """Builds a question comparing song lengths."""
        try:
            data = self.getdata()
            question = f"Which of these songs has the longest duration?"
            temp_options = []
            options = []
            for i in data:
                temp_options.append((i.track, i.duration))
            solution = max(temp_options, key=lambda x: x[1])[0]
            for j in temp_options:
                options.append(j[0])
            random.shuffle(options)
            return question, options, solution
        except Exception as ex:
            raise RuntimeError(f"Error in 'length_question': {ex}")
    
    def age_question(self):
        """Builds a question comparing song release dates."""
        try:
            data = self.getdata()
            question = f"Which of these songs is the oldest?"
            temp_options = []
            options = []
            for i in data:
                temp_options.append((i.track, i.release))
            solution = min(temp_options, key=lambda x: x[1])[0]
            for j in temp_options:
                options.append(j[0])
            random.shuffle(options)
            return question, options, solution
        except Exception as ex:
            raise RuntimeError(f"Error in 'age_question': {ex}")
    
    def tempo_question(self):
        """Builds a question comparing song tempos (BPM)."""
        try:
            data = self.getdata()
            question = f"Which of these songs has the slowest tempo?"
            temp_options = []
            options = []
            for i in data:
                temp_options.append((i.track, i.tempo))
            solution = min(temp_options, key=lambda x: x[1])[0]
            for j in temp_options:
                options.append(j[0])
            random.shuffle(options)
            return question, options, solution
        except Exception as ex:
            raise RuntimeError(f"Error in 'tempo_question': {ex}")

class InvalidPlaylist(Exception):
    def __init__(self, message="Playlist is invalid"):
        self.message = message
        super().__init__(self.message)
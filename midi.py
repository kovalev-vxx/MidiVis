from mido import MidiFile


def get_midi(file_path):
    return MidiFile(file_path).tracks

def get_tracks(midi):
    return midi.tracks

def get_tempo(midi):
    return get_tracks(midi)[0].tempo

def get_length(midi):
    return midi.length

def track_parser(track):
    notes = [i for i in track if (i.type=="note_on" and i.time!=0) or (i.type=="note_off")]
    chords = []
    for note in notes:
        if note.type == "note_off" and note.time !=0:
            chords.append({"notes":[note.note], "time": note.time, "velocity": note.velocity})
        elif note.type == "note_off" and note.time ==0:
            chords[len(chords)-1]["notes"].append(note.note) 
        else:
            chords.append({"notes":[0], "time": note.time, "velocity": note.velocity})
    return chords  
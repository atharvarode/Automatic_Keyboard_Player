from music21 import converter

def music_file_to_notes_and_octaves(file_path):
    # Load the music file
    score = converter.parse(file_path)

    # Extract notes and octaves
    notes_and_octaves = []
    for element in score.flat.notesAndRests:  # Use notesAndRests to handle both notes and rests
        if element.isNote:
            note_name = element.name
            octave = element.octave
            notes_and_octaves.append((note_name, octave))
        elif element.isRest:
            # Handle rests (if needed)
            pass

    return notes_and_octaves

# Example usage
file_path = "piano.mid"  # Replace with your music file path
result = music_file_to_notes_and_octaves(file_path)
print(result)
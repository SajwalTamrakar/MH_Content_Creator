from . music_theory import make_formula, make_intervals

music_notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

def notes_replace(notes):
    """Replacing notes becuase music theory is returning double sharps and all"""
    for index, item in enumerate(notes):
        if item == 'A##':
            notes[index] = 'B'
        if item == 'B#':
            notes[index] = 'C'
        if item == 'B##':
            notes[index] = 'C#'
        if item == 'C##':
            notes[index] = 'D'
        if item == 'D##':
            notes[index] = 'E'
        if item == 'E#':
            notes[index] = 'F'
        if item == 'E##':
            notes[index] = 'F#'
        if item == 'F##':
            notes[index] = 'G'
        if item == 'G##':
            notes[index] = 'A'

def scale_generator(root, scale_type):
    """generate scale notes, patterns"""
    scale_notes = []
    key = root.upper()
    scale = scale_type.lower()

    intervs = make_intervals(key)

    if scale == 'major':
        notes = make_formula('P1,M2,M3,P4,P5,M6,M7,P8', intervs)
        notes_replace(notes)
        scale_notes = notes
        pattern = "Key - W - W - H - W - W - W - H"
        notes_pattern = f"Key({notes[0]}) – W({notes[1]}) – W({notes[2]}) – H({notes[3]}) – W({notes[4]}) – W({notes[5]}) – W({notes[6]}) – H({notes[7]})"
        dominant = [notes[0], notes[2], notes[4]]
        dom4 = [notes[0], notes[2], notes[3], notes[4]]

    if scale == 'minor':
        notes = make_formula('P1,M2,m3,P4,P5,m6,m7,P8', intervs)
        notes_replace(notes)
        scale_notes = notes
        pattern = "Key - W - H - W - W - H - W - W"
        notes_pattern = f"Key({notes[0]}) – W({notes[1]}) – H({notes[2]}) – W({notes[3]}) – W({notes[4]}) – H({notes[5]}) – W({notes[6]}) – W({notes[7]})"
        dominant = [notes[0], notes[2], notes[4]]
        dom4 = [notes[0], notes[2], notes[3], notes[4]]
        pentatonic = [notes[0], notes[2], notes[3], notes[4], notes[6]]

    if 'melodic' == scale:
        notes = make_formula('P1,M2,m3,P4,P5,M6,M7,P8', intervs)
        notes_replace(notes)
        scale_notes = notes
        pattern = "Key - W - H - W - W - W - W - H"
        notes_pattern = f"Key({notes[0]}) – W({notes[1]}) – H({notes[2]}) – W({notes[3]}) – W({notes[4]}) – W({notes[5]}) – W({notes[6]}) – H({notes[7]})"
        dominant = [notes[0], notes[2], notes[4]]
        dom4 = [notes[0], notes[2], notes[3], notes[4]]

    # if 'pentatonic' == scale:
    #     notes = make_formula('P1,m3,P4,P5,m7', intervs)
    #     notes_replace(notes)
    #     scale_notes = notes
    #     pattern = "Key - W - H - W - W - W - W - H"
    #     notes_pattern = f"Key({notes[0]}) – W({notes[1]}) – H({notes[2]}) – W({notes[3]}) – W({notes[4]}) – W({notes[5]}) – W({notes[6]}) – H({notes[7]})"
    #     dominant = [notes[0], notes[2], notes[4]]
    #     dom4 = [notes[0], notes[2], notes[3], notes[4]]



    if scale == 'minor':
        return pattern, scale_notes, notes_pattern, dominant, dom4, pentatonic

    else:
        return pattern, scale_notes, notes_pattern, dominant, dom4


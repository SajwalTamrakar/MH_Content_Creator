from fretboardgtr import ScaleGtr, ScaleFromName
from . scale_generator import scale_generator


def fretboardDominant(root, scale_type):


    key = root.upper()
    scale = scale_type.title()

    if scale == 'Minor':
        pattern, scale_notes, notes_pattern, dominant, dom4, pentatonic = scale_generator (root, scale_type)
    else:
        pattern, scale_notes, notes_pattern, dominant, dom4 = scale_generator (root, scale_type)

   
    #
    # if key == 'A' and scale =='Major':

    F=ScaleGtr(scale=dominant, root=key)
    F.customtuning(['E', 'A', 'D', 'G', 'B', 'E'])
    F.pathname(f"media/media/{key} {scale} Dominants.svg")
    F.theme(show_note_name=True, background_color = 'rgb(212,168,83)')
    F.first_fret = 5
    F.last_fret = 9
    if key == 'G':
        F.first_fret = 3
        F.last_fret = 7
    if key == 'B':
        F.first_fret = 7
        F.last_fret = 11
    if key == 'D':
        F.first_fret = 10
        F.last_fret = 15
    if key == 'E':
        F.first_fret = 12
        F.last_fret = 16
    F.draw()
    F.save(extension='JPG')


def fretboardDom4(root, scale_type):

    key = root.upper()
    scale = scale_type.title()

    if scale == 'Minor':
        pattern, scale_notes, notes_pattern, dominant, dom4, pentatonic = scale_generator (root, scale_type)
    else:
        pattern, scale_notes, notes_pattern, dominant, dom4 = scale_generator (root, scale_type)
    #
    # if key == 'A' and scale =='Major':

    F=ScaleGtr(scale=dom4, root=key)
    F.customtuning(['E', 'A', 'D', 'G', 'B', 'E'])
    F.pathname(f"media/media/{key} {scale} Dominants and 4th.svg")
    F.theme(show_note_name=True)
    F.first_fret = 5
    F.last_fret = 9
    if key == 'G':
        F.first_fret = 3
        F.last_fret = 7
    if key == 'B':
        F.first_fret = 7
        F.last_fret = 11
    if key == 'D':
        F.first_fret = 10
        F.last_fret = 15
    if key == 'E':
        F.first_fret = 12
        F.last_fret = 16
    F.draw()
    F.save(extension='JPG')

def fretboard(root, scale_type):

    key = root.upper()
    scale = scale_type.title()

    if scale == 'Minor':
        pattern, scale_notes, notes_pattern, dominant, dom4, pentatonic = scale_generator (root, scale_type)
    else:
        pattern, scale_notes, notes_pattern, dominant, dom4 = scale_generator (root, scale_type)
    #
    # if key == 'A' and scale =='Major':

    F=ScaleGtr(scale=scale_notes, root=key)
    F.customtuning(['E', 'A', 'D', 'G', 'B', 'E'])
    F.pathname(f"media/media/{key} {scale}.svg")
    F.theme(show_note_name=True)
    F.first_fret = 5
    F.last_fret = 10
    if key == 'G':
        F.first_fret = 3
        F.last_fret = 7
    if key == 'B':
        F.first_fret = 7
        F.last_fret = 11
    if key == 'D':
        F.first_fret = 10
        F.last_fret = 15
    if key == 'E':
        F.first_fret = 12
        F.last_fret = 16
    F.draw()
    F.save(extension='JPG')

def minorpentatonic(root, scale_type):

    key = root.upper()
    scale = scale_type.title()

    if scale == 'Minor':
        pattern, scale_notes, notes_pattern, dominant, dom4, pentatonic = scale_generator (root, scale_type)
    else:
        pattern, scale_notes, notes_pattern, dominant, dom4 = scale_generator (root, scale_type)
    #
    # if key == 'A' and scale =='Major':

    F=ScaleGtr(scale=pentatonic, root=key)
    F.customtuning(['E', 'A', 'D', 'G', 'B', 'E'])
    F.pathname(f"media/media/{key} {scale} pentatonic.svg")
    F.theme(show_note_name=True)
    F.first_fret = 5
    F.last_fret = 10
    if key == 'G':
        F.first_fret = 3
        F.last_fret = 7
    if key == 'B':
        F.first_fret = 7
        F.last_fret = 11
    if key == 'D':
        F.first_fret = 10
        F.last_fret = 15
    if key == 'E':
        F.first_fret = 12
        F.last_fret = 16
    F.draw()
    F.save(extension='JPG')

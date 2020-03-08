from typing import Any, List, Tuple
import urwid
import urwid.raw_display
import urwid.web_display


from autosuggest import AutoSuggest


def main():

    suggest = AutoSuggest()

    search_caption= 'search: ' 
    search_term = 'Go into the wild'
    result_list = 'boo'
    search_input = urwid.Edit(search_caption, '')
    result_text = urwid.Text(result_list)
    listbox_content = [
            urwid.Columns([
                            urwid.AttrWrap(search_input, 'editbx'),
                            urwid.AttrWrap(result_text, 'editbx')
            ])
    ]
    header_text = 'Welcome to xuggest'
    listbox = urwid.ListBox(urwid.SimpleListWalker(listbox_content))
    header = urwid.AttrWrap(urwid.Text(header_text), 'header')
    frame = urwid.Frame(urwid.AttrWrap(listbox, 'body'), header=header)

    palette = [
        ('body', 'black', 'dark gray', 'standout'),
        ('editbx', 'light gray', 'dark blue'),
        ('bright' , 'dark gray', 'light gray', ('bold', 'standout'))
    ]
    screen = urwid.raw_display.Screen() 

    def make_results_string(results: List[str]) -> str:
        return '\n'.join(word for word in results)
    def search_input_handler(widget, search_term):

        # find term in search box
        
        results = suggest.get_prefix_children(search_term)
        result_string = make_results_string(results)
        result_text.set_text(result_string)

    def unhandled(key):
        if key == 'f8':
            raise urwid.ExitMainLoop()

    urwid.connect_signal(search_input, 'change', search_input_handler)
    urwid.MainLoop(frame, palette, screen, 
                   unhandled_input=unhandled).run()




if __name__ == '__main__': 

    main()



"""


------------ |   --------------

|search bar| |  | results popup
             |
             |

urwid.Columns([urwid.Edit,   | urwid.Text ])



"""







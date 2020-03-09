from typing import Any, List, Tuple
import urwid
import urwid.raw_display
import urwid.web_display


from autosuggest import AutoSuggest


class Display:


    def __init__(self, data=None):
        self.suggest = AutoSuggest(data)
        self.screen = urwid.raw_display.Screen()
        self.search_input = urwid.Edit('Search: ', '')
        
        self.palette = [
            ('body', 'black', 'dark gray', 'standout'),
            ('editbx', 'light gray', 'dark blue'),
            ('bright' , 'dark gray', 'light gray', ('bold', 'standout'))
        ]

        self.result_text = urwid.Text('')
        self.header_text = 'Welcome to xuggest'
        self.listbox  = self._make_list_box()
        self.header = urwid.AttrWrap(urwid.Text(self.header_text), 'header')
        self.frame = urwid.Frame(urwid.AttrWrap(self.listbox, 'body'),
                                 header=self.header)

    def _make_list_box(self):
        listbox_content = [
                urwid.Columns([
                                urwid.AttrWrap(self.search_input, 'editbx'),
                                urwid.AttrWrap(self.result_text, 'editbx')
                ])
        ]
        return urwid.ListBox(urwid.SimpleListWalker(listbox_content))
        
    def start_engine(self):
  
        def make_results_string(results: List[str]) -> str:
            return '\n'.join(word for word in results)
       
       def search_input_handler(widget, search_term):
            
            results = self.suggest.get_prefix_children(search_term)
            result_string = make_results_string(results)
            self.result_text.set_text(result_string)

        def unhandled(key):
            if key == 'f8':
                raise urwid.ExitMainLoop()

       
        urwid.connect_signal(self.search_input, 'change', search_input_handler)
        header = urwid.AttrWrap(urwid.Text(self.header_text), 'header')
        frame = urwid.Frame(urwid.AttrWrap(self.listbox, 'body'), header=header)

        urwid.MainLoop(self.frame, self.palette, self.screen, 
                       unhandled_input=unhandled).run()




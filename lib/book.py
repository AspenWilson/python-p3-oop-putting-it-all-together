#!/usr/bin/env python3

class Book:
    def __init__(self, title="The World According to Garp", page_count= 69):
        self.title = title
        self._page_count = page_count
    
    def get_page_count (self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if type(page_count) is int:
            self._page_count = page_count
        else:
            print("page_count must be an integer") 

    def turn_page(self):
        print ("Flipping the page...wow, you read fast!" )

    page_count = property(get_page_count, set_page_count)

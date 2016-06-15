#!/usr/bin/env python2
#encoding: UTF-8

class NotesApplication(object):
    
    
    def __init__(self,author):
        self.author = author
        notes=[]
        self.notes=notes
        
        
    def create(self, note_content):
        self.note_content = note_content
        self.notes.append(self.note_content)
        
    def list(self):
        
        for i in range(len(self.notes)):
            print "Note ID: %d" % i
            print self.get(i)
            print "By Author: %s" % self.author
            print ""
        """
        print "Note ID: %d"%self.note_id
        print "%s"%self.note_content
        """
        
    def get(self,note_id):
        return self.notes[note_id]
    
    
    def search(self, search_text):
        print "Showing results for search '%s' \n" % search_text
        for x in self.notes:
            if search_text in x:
                print "Note ID: %s" % self.notes.index(x)
                print x,"\n"
        
        print "Found 0 matches"
        
    def edit(self, note_id, new_content):
        self.notes[note_id] = new_content

if __name__=="__main__":
    note1 = NotesApplication("Jeffrey")
    
    note1.create("Andela ROCKS")
    note1.create("TIA")
    note1.create("WHATSUPP ANDELA")
 
    m=raw_input('Enter the search string: ')
    note1.search(m)
    note1.edit(2,"Hello Andela world")

'''
write a py prog to stimulate the behaviour of a web page or web browsers back button when a user visits a new page push it to the stack 
when user clicks back pop the top page and go back to the previous page 
'''
class Browser:
    def __init__(self):
        self.history=[]
    def visit(self,page):
        self.history.append(page)
    def Undo(self):
        if len(self.history)>1:
            self.history.pop()
            print(f"Back to {self.history[-1]} page")
        else:
            print("No page")
browser=Browser()
browser.visit("google.com")
browser.visit("linkedin.com")
browser.visit("github.com")
browser.visit("youtube.com")
browser.Undo()
browser.Undo()
browser.Undo()
browser.Undo()
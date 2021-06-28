import notify2
import time as tm
import pyperclip as cl
def clip():
	notify2.init("sample")
	tx=cl.waitForNewPaste()
	n=notify2.Notification("ClipBoard Elert\n","you have copied the following text:\n"+tx,"tag-new")
	n.set_urgency(2)
	n.show()
	tm.sleep(5)
	n.close()
	clip()
clip()
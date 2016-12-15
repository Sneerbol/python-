import pyHook
def foo(counter=[0]):
    counter[0] += 1
    print("Нажато раз %i." % counter[0]);
def OnKeyboardEvent(event):

   
    print ('-------')
    
    print ('WindowName:',event.WindowName)
    
    print('Key:', event.Key)
    print(foo())
    
    
    print ('-----------')
    
    
    


    return True


hm = pyHook.HookManager()

hm.KeyDown = OnKeyboardEvent

hm.HookKeyboard()



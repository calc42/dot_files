from keyhac import *

def configure(keymap):
    
    #28 変換
    #29 無変換
    #242 ひらがな
    keymap_global = keymap.defineWindowKeymap()
    
    #keymap.replaceKey( "29", "Shift" )
    
    keymap.defineModifier("28", "User1")
    keymap.defineModifier("29", "User2");
    keymap_global["O-28"] = "28"
    keymap_global["O-29"] = "29"
    #keymap_global["U1-29"] = "29"J
    #keymap_global["U1-J"] = "Left"
    #keymap_global["U1-Shift"] = "29"
    #keymap_global["D-29"] = "Shift"
    dic = {"U2-":"S-"}
    for any in ("", "U2-"):
        keymap_global[any + "U1-J"] = dic.get(any,'') + "Left"
        keymap_global[any + "U1-L"] = dic.get(any,'') + "Right"
        keymap_global[any + "U1-I"] = dic.get(any,'') + "Up"
        keymap_global[any + "U1-K"] = dic.get(any,'') + "Down"
        keymap_global[any + "U1-U"] = dic.get(any,'') + "Home"
        keymap_global[any + "U1-O"] = dic.get(any,'') + "End"
    keymap_global["U1-H"] = "Back"
    keymap_global["U1-D"] = "Delete"
    keymap_global["U1-E"] = "Enter"
    keymap_global["U1-Q"] = "Esc"
    keymap_global["U1-S"] = "A-Tab"
    keymap_global["U1-A"] = "S-A-Tab"
    #keymap_global["U2-U1-J"] = "S-Left"
    
    for keycode in range(1, 255):
        keymap_global["U2-" + str(keycode)] = "S-" + str(keycode)
    keymap_global["U2-tab"] = "S-tab"
    
    #keymap.replaceKey("Space", "RShift")
    #keymap_global["O-RShift"] = "Space"
    
    keymap_global["242"] = "Back"
    #keymap_global[ "A-Space" ] = "A-Tab"
    
    # アクティブ化するか、まだであれば起動する
    def command_ActivateOrExecute( class_name, filename, param = u"", directory = u"" ):
        wnd = Window.find( class_name, None )
        if wnd:
            if wnd.isMinimized():
                wnd.restore()
            wnd = wnd.getLastActivePopup()
            wnd.setForeground()
        else:
            executeFunc = keymap.command_ShellExecute( None, None, filename, param, directory )
            executeFunc()
    
    #keymap_global["U1-F"] = lambda: command_ActivateOrExecute( "MozillaWindowClass" , "G:/Mozilla Firefox/firefox.exe" ) 
    keymap_global["U1-F"] = keymap.command_ActivateWindow( "firefox.exe", "MozillaWindowClass" )
    #keymap_global["U1-B"] = keymap.command_ActivateWindow( "sakura.exe","SakuraView142","SakuraView142")
    keymap_global["U1-X"] = keymap.command_ActivateWindow( "XF.exe")
    keymap_global["U1-C"] = keymap.command_ActivateWindow("cmd.exe")
    
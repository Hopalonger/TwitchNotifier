Dim WShell
Set WShell = CreateObject("WScript.Shell")
WShell.Run "node bot.js", 0
Set WShell = Nothing

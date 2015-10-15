On Error Resume Next
Set oShell = CreateObject("WScript.Shell")
value = oShell.RegRead("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\1\")

If Err.Number = 0 Then
    Wscript.Quit
End If

UntilDate = DateDiff("s", "01/01/1970 00:00:00", now)
Wscript.Echo "<<<win_os:sep(124):persist(" & (UntilDate + 14500) & ")>>>"

strComputer = "."
Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colOperatingSystems = objWMIService.ExecQuery("Select * from Win32_OperatingSystem")
For Each objOperatingSystem in colOperatingSystems
    OS = objOperatingSystem.Caption
    OSVersion = objOperatingSystem.Version
    InstallDate = objOperatingSystem.InstallDate
    SPMajor = objOperatingSystem.ServicePackMajorVersion
    SPMinor = objOperatingSystem.ServicePackMinorVersion
    OSArch = objOperatingSystem.OSArchitecture 
Next

Set colOperatingSystems = objWMIService.ExecQuery("Select * from Win32_ComputerSystem")
For Each objOperatingSystem in colOperatingSystems
    Name = objOperatingSystem.Name
Next

Wscript.Echo Name & "|" & OS & "|" & OSVersion & "|" & OSArch & "|" & SPMajor & "|" & SPMinor & "|" & InstallDate

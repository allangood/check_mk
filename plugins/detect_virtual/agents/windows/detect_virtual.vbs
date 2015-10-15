UntilDate = DateDiff("s", "01/01/1970 00:00:00", now)
Wscript.Echo "<<<win_detect_virtual:sep(200):persist(" & (UntilDate + 14500) & ")>>>"

IsVM

Function IsVM

	' Check the WMI information against known values

	bIsVM = false
	sVMPlatform = ""

	sMake = GetWmiPropertyValue("root\cimv2", "Win32_ComputerSystem", "Manufacturer")
	sModel = GetWmiPropertyValue("root\cimv2", "Win32_ComputerSystem", "Model")
	sBIOSVersion = GetWmiPropertyValue("root\cimv2", "Win32_BIOS", "Version")

	WScript.Echo "Manufacturer : " & sMake
	WScript.Echo "Model : " & sModel
	WScript.Echo "BIOSVersion : " & sBIOSVersion

	If sModel = "Virtual Machine" then

		' Microsoft virtualization technology detected, assign defaults

		sVMPlatform = "Hyper-V"
		bIsVM = true

		' Try to determine more specific values

		Select Case sBIOSVersion
		Case "VRTUAL - 1000831"
			bIsVM = true
			sVMPlatform = "Hyper-V 2008 Beta or RC0"
		Case "VRTUAL - 5000805", "BIOS Date: 05/05/08 20:35:56  Ver: 08.00.02"
			bIsVM = true
			sVMPlatform = "Hyper-V 2008 RTM"
		Case "VRTUAL - 3000919"
			bIsVM = true
			sVMPlatform = "Hyper-V 2008 R2"
		Case "A M I  - 2000622"
			bIsVM = true
			sVMPlatform = "VS2005R2SP1 or VPC2007"
		Case "A M I  - 9000520"
			bIsVM = true
			sVMPlatform = "VS2005R2"
		Case "A M I  - 9000816", "A M I  - 6000901"
			bIsVM = true
			sVMPlatform = "Windows Virtual PC"
		Case "A M I  - 8000314"
			bIsVM = true
			sVMPlatform = "VS2005 or VPC2004"
		End Select

	ElseIf sModel = "VMware Virtual Platform" then

		' VMware detected

		sVMPlatform = "VMware"
		bIsVM = true

	ElseIf sModel  = "VirtualBox" then

		' VirtualBox detected

		bIsVM = true
		sVMPlatform = "VirtualBox"

	Else
		' This computer does not appear to be a virtual machine.
	End if

	' Set the return value

	If bIsVM Then
		WScript.Echo "IsVirtualMachine : True"
		WScript.Echo "VirtualMachinePlatform : " & sVMPlatform
	Else
		WScript.Echo "IsVirtualMachine : False"
	End If

	IsVM = bIsVM

End Function

Function GetWmiPropertyValue(strNameSpace, strClassName, strPropertyName)

	On Error Resume Next

	strPropertyValue = ""
	set oWmiClass = getobject("winmgmts:" & strNameSpace).get(strClassName,&h20000) 'amended
	set oWmiProperties = oWmiClass.Properties_

	Set objWMIService = GetObject("winmgmts:\\" & "." & "\" & strNameSpace)
	Set colItems = objWMIService.ExecQuery("Select * from " & strClassName,,48)

	For Each objItem in colItems
		For Each objProperty in oWmiProperties
			sLine = ""
			'WScript.Echo "- " & objProperty.name & ": " & strPropertyName

			If objProperty.Name = strPropertyName Then
				If objProperty.IsArray = True Then
					sLine = "str" & objProperty.Name & " = Join(objItem." & objProperty.Name & ", " & Chr(34) & "," & Chr(34) & ")" & vbCrLf
					sLine = sLine & "strPropertyValue =  str" & objProperty.Name
				'ElseIf objProperty.CIMTYPE = 101 Then
				'    bHasDates = True
				'    sLine =  "strPropertyValue =  WMIDateStringToDate(objItem." & objProperty.Name & ")"
				Else
					sLine =  "strPropertyValue =  objItem." & objProperty.Name
				End If

				'WScript.Echo sLine
				Execute sLine
			End If

		Next
	Next

	GetWmiPropertyValue = strPropertyValue

End Function

On Error Resume Next

strComputer = "."

Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\microsoftdfs")

colItems = Null
set colItems = objWMIService.ExecQuery("Select * from dfsrreplicatedfolderinfo")

If not IsNull(colItems) Then
  Wscript.Echo "<<<dfs_state>>>"
  For Each objItem in colItems
    Wscript.Echo objItem.replicatedfoldername & vbTab & objItem.replicationgroupname & vbTab & objItem.state
  Next
End If

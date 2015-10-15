# Configuration

$user = "DAILYREPORT"
$password = "dailytsm"
$delay = 3600 # execute agent only every $delay seconds

$workingdir = "C:\Progra~1\Tivoli\TSM\baclient\"
$command = ".\dsmadmc.exe -dataonly=YES -id=$user -password=$password -displaymode=table "

$serverdir = "C:\Progra~1\Tivoli\TSM\server\"
if (!(Test-Path $serverdir -pathType container)) { exit }

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
write-output "" # workaround to prevent the byte order mark to be at the beginning of the first section
# filename for timestamp
$remote_host = $env:REMOTE_HOST
$agent_dir   = $env:MK_CONFDIR

# Fallback if the (old) agent does not provide the MK_CONFDIR
if (!$agent_dir) {
    $agent_dir = "c:\Program Files (x86)\check_mk"
}

$timestamp = $agent_dir + "\tsm_timestamp."+ $remote_host

# does $timestamp exist?
If (Test-Path $timestamp){
    $filedate = (ls $timestamp).LastWriteTime
    $now = Get-Date
    $earlier = $now.AddSeconds(-$delay)
    # exit if timestamp to young
    if ( $filedate -gt $earlier ) {
        $Out = Get-Content $timestamp
        Foreach ($l in $Out) {
            echo ($l -replace '\s+',"`t")
        }
        Exit
    }
}

# create new timestamp file
New-Item $timestamp -type file -force | Out-Null

# calculate unix timestamp
$epoch=[int][double]::Parse($(Get-Date -date (Get-Date).ToUniversalTime()-uformat %s))

# convert it to integer and add $delay seconds plus 5 minutes
$until = [int]($epoch -replace ",.*", "") + $delay + 600

Set-Location -Path $workingdir
Add-Content $timestamp "<<<tsm_drives>>>"
$args = "select 'default', library_name, drive_name, drive_state, online, drive_serial from drives"
$cmd = $command + '"' + $args + '"'
$output = Invoke-Expression "$cmd"
Add-Content $timestamp $output

Add-Content $timestamp "<<<tsm_paths>>>"
$args = "select source_name, destination_name, online from paths"
$cmd = $command + '"' + $args + '"'
$output = Invoke-Expression "$cmd"
Add-Content $timestamp $output

Add-Content $timestamp "<<<tsm_sessions>>>"
$args = "select session_id, client_name, state, wait_seconds from sessions"
$cmd = $command + '"' + $args + '"'
$output = Invoke-Expression "$cmd"
Add-Content $timestamp $output

Add-Content $timestamp "<<<tsm_scratch>>>"
$args = "select 'default', count(library_name), library_name from libvolumes where status='Scratch' group by library_name"
$cmd = $command + '"' + $args + '"'
$output = Invoke-Expression "$cmd"
Add-Content $timestamp $output

Add-Content $timestamp "<<<tsm_storagepools>>>"
$args = "select 'default', type, stgpool_name, sum(logical_mb) from occupancy group by type, stgpool_name"
$cmd = $command + '"' + $args + '"'
$output = Invoke-Expression "$cmd"
Add-Content $timestamp $output

Add-Content $timestamp "<<<tsm_stagingpools>>>"
$args = "select 'default', stgpool_name, pct_utilized from volumes where access='READWRITE' and devclass_name<>'DISK'"
$cmd = $command + '"' + $args + '"'
$output = Invoke-Expression "$cmd"
Add-Content $timestamp $output

Add-Content $timestamp "<<<tsm_logs>>>"
$args = "SELECT DATE_TIME,MESSAGE FROM ACTLOG WHERE DATE_TIME>=current_timestamp - 60 minutes AND MSGNO IN (1410,1411,1417,1772,2578,2579,2580,2581,2752,8455,8779,8792,8840,8848,8943,8944,8954)"
$cmd = $command + '"' + $args + '"'
$output = Invoke-Expression "$cmd"
Add-Content $timestamp $output

$Out = Get-Content $timestamp
Foreach ($l in $Out) {
    echo ($l -replace '\s+',"`t")
}

Exit

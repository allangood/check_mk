@echo off
@echo ^<^<^<dfs_state^>^>^>
@wmic  /namespace:\\root\microsoftdfs path dfsrreplicatedfolderinfo get replicationgroupname,replicatedfoldername,state

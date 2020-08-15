/* C:\Users\Christine\Documents\GitHub\Technical\CWA\scenario3.sql */
/* To sync:
The mssql extension in Viz Studio can use SQL Server Data Tools to make a new schema comparison between the local database and the LAN one-- or between two server databases. 
This will identify any differences between the databases.  */

/* To delete duplicates:
I don't actually know if this will work, but you should be able to delete dupes within the CTE using the code below: */
WITH CTE AS(
   SELECT [col1], [col2], [col3], [col4], [col5], [col6], [col7],
       RN = ROW_NUMBER()OVER(PARTITION BY col1 ORDER BY col1)
   FROM dbo.Table1
)
DELETE FROM CTE WHERE RN > 1
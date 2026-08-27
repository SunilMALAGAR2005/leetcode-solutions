SELECT today.id FROM weather yesterday
CROSS JOIN weather today

where DATEDIFF(today.recordDate,yesterday.recordDate)=1
AND today.temperature>yesterday.temperature

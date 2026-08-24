CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
set M=N-1;
  RETURN (
    SELECT DISTINCT(salary) from Employee ORDER BY salary DESC Limit M,1
      

  );
END
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
set n=N-1;
  RETURN (
    SELECT DISTINCT(salary) from Employee ORDER BY salary DESC  Limit N, 1
      

  );
END
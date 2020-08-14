USE cmdev;
#SELECT ename, salary ,IF(salary>=3000, "高薪", "一般") AS "薪情" FROM emp;
SELECT ename, salary,
CASE 
     WHEN salary>=3000 THEN "高薪"
     WHEN salary>=1000 THEN "一般"
     ELSE "低薪"
END AS "薪情"
FROM emp;
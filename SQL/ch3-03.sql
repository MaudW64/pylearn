USE cmdev;
SELECT job, 
       MAX(salary) AS "最高薪資",
       MIN(salary) AS "最低薪資",
       AVG(salary) AS "平均薪資",
       SUM(salary) AS "所有薪資",
       COUNT(salary) AS "總人數"
FROM emp
GROUP BY job  # 以職業別分類(列)
HAVING COUNT(salary) > 1;  # 團體人數少於1者忽略
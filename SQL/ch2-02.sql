USE cmdev;
#SELECT job AS "職位", salary AS "月薪", salary*12 AS "年薪", (salary*12)+(salary DIV	2) AS "年薪(+獎金)" FROM emp;
#SELECT ename, job, salary, deptno FROM emp WHERE deptno IS NULL;
#SELECT ename, job, salary,deptno FROM emp WHERE ename LIKE "%d%" or ename like "%a";
#SELECT ename, job, salary,deptno FROM emp WHERE job IN ("analyst","salesman");
#SELECT ename, job, salary,deptno FROM emp WHERE salary BETWEEN 1000 AND 3000;
#SELECT ename, deptno FROM emp WHERE ename LIKE "____" order by ename ASC;  # 條件：文字數, 依名稱字母排序
SELECT ename, salary, deptno FROM emp ORDER BY salary DESC LIMIT 3,5;  
#SELECT DISTINCT job FROM emp;


USE cmdev;
#SELECT 1+2, '2'+1,'net'+'filx';
#SELECT UPPER(ename), LOWER(ename), LEFT(ename,2),SUBSTRING(ename,2,4), job FROM emp;
#SELECT CONCAT(LEFT(ename,1), SUBSTRING(LOWER(ENAME),2)) AS Stuff_Name, job FROM emp;
#SELECT CONCAT_WS('-',LEFT(ename,1), SUBSTRING(LOWER(ENAME),2)) AS Stuff_Name, job FROM emp;
#SELECT ename, salary, TRUNCATE(salary,-2),CEILING(salary) FROM emp;
#SELECT FLOOR(RAND()*100+1);  # 亂數1~100, RAND()=0~0.99..
#SELECT FLOOR(RAND()*101);  # 亂數0~100
SELECT ename, YEAR(hiredate), MONTHNAME(hiredate), DAYNAME(hiredate) FROM emp WHERE DAYNAME(hiredate) IN ('Sunday','Monday');

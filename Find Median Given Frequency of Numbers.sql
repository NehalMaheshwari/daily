#LeetCode #571 — Find Median Given Frequency of Numbers
SELECT ROUND(AVG(num), 1) AS median
FROM (
    SELECT
        num,
        frequency,
        SUM(frequency) OVER (ORDER BY num) AS running_total,
        SUM(frequency) OVER () AS total_count
    FROM Numbers
) t
WHERE running_total >= total_count / 2
AND running_total - frequency <= total_count / 2;

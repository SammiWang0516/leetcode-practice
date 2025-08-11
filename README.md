
# LeetCode Practice

This repository contains my **SQL** and **Python** solutions to LeetCode problems, organized by topic and difficulty.

## 📌 Purpose
- Document my problem-solving journey for Data Structures, Algorithms, and SQL.
- Build a reference library of solutions with clear explanations.
- Track my progress toward mastering technical interview skills.

## 📂 Structure
```
SQL/
  SELECT-WHERE/           # Filtering & selecting data
  Aggregation/            # GROUP BY, HAVING, aggregates
  JOINS/                  # INNER, LEFT, self-joins
  Window-Functions/       # RANK, ROW_NUMBER, etc.
  Date-Time/              # Date filtering & grouping
  Subqueries-CTEs/        # Nested queries & CTEs
  Conditional-Logic/      # CASE WHEN usage
  Multi-step/             # Complex interview-style problems

Python/
  Arrays-Strings/         # Array and string manipulation
  Hash-Map-Set/           # Dictionary & set usage
  Sorting/                # Sorting algorithms
  Binary-Search/          # Binary search & variations
  Stack/                  # Stack-based problems
  Queue-Deque/            # Queue & deque usage
  Linked-List/            # Linked list operations
  Trees/                  # Binary tree, BST problems
  Heaps/                  # Heap & priority queue
  Graphs/                 # Graph traversal & shortest path
  Recursion-Backtracking/ # Recursive & backtracking solutions
  Dynamic-Programming/    # DP techniques
  Greedy/                 # Greedy algorithms
  Math-Bit-Manipulation/  # Math tricks, bit operations
```

## 📝 Solution Format
Each solution file contains:
1. **Problem title & link**
2. **Topic & difficulty**
3. **Approach explanation**
4. **Code solution** (Python for algorithms, SQL for queries)

**Example (SQL):**
```sql
-- Problem: 175. Combine Two Tables
-- Topic: JOIN Basics
-- Difficulty: Easy
-- Approach: LEFT JOIN customers with orders
SELECT c.FirstName, c.LastName, a.City
FROM Customers c
LEFT JOIN Addresses a ON c.Id = a.CustomerId;
```

**Example (Python):**
```python
# Problem: Two Sum
# Topic: Hash Map
# Difficulty: Easy
# Approach: Use dict to store seen values and check complement
def twoSum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
```

## ✅ Naming Convention
- SQL: `175_combine_two_tables.sql`
- Python: `0001_two_sum.py`

## 🗂 Commit Message Style
- `feat(sql): add JOIN solution for Rising Temperature`
- `docs: update README with progress table`
- `refactor(py): optimize two-pointer solution for remove-duplicates`

## 📅 Progress Tracking
I plan to update this repository **weekly** with new solutions.

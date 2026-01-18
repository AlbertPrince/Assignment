# AI Code Review Assignment (Python)

## Candidate
- Name:
- Approximate time spent:

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- In the AI-
generated explanation, the average order value is calculated by summing the amount of non-cancelled orders by the total number of orders which in logic doesn't make sense. It should divide by the total number of non-cancelled orders which should make the logic correct. 

### Edge cases & risks
- There is a possibility of a zero division error if the total number of orders is zero.
- If all orders are cancelled, it may return a wrong value and this should be accounted for. 
- This implementation also assumes that orders have "status" and "amount" keys for each order.

### Code quality / design issues
- The denominator does not reflect the actual average being calculated. 
- There is a misalignment between the explanation given and the code written.

## 2) Proposed Fixes / Improvements
### Summary of changes
- The average should be calculated using only non-cancelled orders
- The orders should be filtered to include only non-cancelled orders. 
- There should be cheks for if the list is empty or if all orders are cancelled. 

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
- If I were to test this code I would test for edge cases first i.e. empty list, cancelled orders only and then normal cases that is all no cancelled orders or orders with a mix of cancelled and non-cancelled orders. There is also the case where some orders may not have values and this should also be taken into consideration. 


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- In the original explanation it doesn't mention how edge cases are handled. 
- In the original explantion the logic for the calculation for the average order doesn't make sense as it includes cancelled orders in the denominator. 

### Rewritten explanation
- This function calculates the average order value by summing all non-cancelled orders and dividing by the number of non-cancelled orders. If there are no valid orders or if the list is empty, it returns 0 to prevent a zero division error. 

## 4) Final Judgment
- Decision:  Request Changes
- Justification: The original implementation doesn't account for edge cases and contains a division-by-zero risk. The explanation is also misleading as it includes cancelled orders in the denominator.
- Confidence & unknowns: I have high confidence in the corrected logic. The only issue is if some of the keys are missing values, then this might cause some issues. 

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- There is no type safety so entering values like 'None' or lists of type integers, objects, etc would cause the function to crash. 

### Edge cases & risks
- It accepts invalid emails since the only thing it's checking for is the existence of "@". Emails only have one so for strings that have 2, it would still be valid. 
- This also doesn't account for the structure of an email as there's to be a string before and after the '@'.
- There's also no domain validation i.e. .com, .xyz, etc.
- It doesn't account for empty lists

### Code quality / design issues
- Using only '@' as validation would result in strings which are not emails passing as one. 
- The explanation doesn't account for what a valid email is. 
- Invalid entries are still counted.

## 2) Proposed Fixes / Improvements
### Summary of changes
- Add input validation to handle 'None' or empty input
- Add type checking to ensure the email is a string
- Enhance validation to account for multiple cases i.e. require exactly one '@', etc. 
- Add domain check by requiring at least one '.' after the '@'

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
If I were to test this function I would test for type safety, invalid formats, valid formats, edge cases, domain validation, white spaces, etc. 

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- No definition of what a valid email is.
- Assumption of what a correct email is is wrong as it's only checking for '@'.
- It does not safely ignore invalid entries.

### Rewritten explanation
- This function counts email addresses in the input list that meet basic structural validity: exactly one '@' symbol with non-empty content before and after it, and at least one '.' in the domain portion. It safely handles non-string items by skipping them, and returns 0 for empty or None input. Note: This is basic validation and does not guarantee RFC 5322 compliance or that the email address actually exists.


## 4) Final Judgment
- Decision:  Request Changes
- Justification: The original code has critical type safety bugs that cause crashes on common real-world inputs. Also the validation logic is very weak and doesn't account for a number of cases.
- Confidence & unknowns: High confidence in identified bugs and proposed fixes.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- The denominator includes 'None' or invalid entries which makes the average inaccurate.
- There is the possiblity of a ZeroDivisionError if all values are none or if list is empty. 
- Doesn't handle numbers that are of type string, e.g. "123" and this would raise an error as it is not of type none but also not a number as to the type. 

### Edge cases & risks
- All none entries would cause a zerodivisionerror
- An empty list would also cause a zerodivision error. 
Mixed valid numbers and 'None' would cause an incorrect average.
- Non-numeric or malformed entries would crash. 

### Code quality / design issues
- Denominator should reflect the count of valid measurements
- Unsafe assumptions that all non-None entries can be converted to float. 
- No error handling
- Explanation overstates safety and correctness of original function 

## 2) Proposed Fixes / Improvements
### Summary of changes
- Added input validation to handle `None` or empty input safely
- Changed validation logic from `if v is not None` + `float(v)` conversion to explicit type checking with `isinstance(v, (int, float))`
- Added boolean exclusion (`not isinstance(v, bool)`) to prevent `True`/`False` being treated as `1`/`0`
- Changed denominator to count only valid numeric values, not total input length
- Added division by zero protection with `if count > 0 else 0`
- Added comprehensive docstring explaining behavior and design decisions
- Removed type conversion entirely — only accept actual numeric types

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
If I were to test this function, I would first test for the edge cases i.e. all values being none, empty list, none input, etc.
I would also test for strings that are numbers
I would test for errors.
I would test for single valid values.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- Factually incorrect: Does NOT "ensure an accurate average" — it divides by the wrong denominator (total count instead of valid count), producing mathematically wrong results.
- Misleading claim: "safely handles mixed input types" is false — the function crashes on non-numeric strings with `ValueError`.
- Omits critical bugs: Doesn't mention it crashes on empty input or None input.
- Vague on "valid": Doesn't specify what constitutes a valid measurement beyond "not None".
- Overstates robustness: The word "safely" is used incorrectly when the function has multiple crash conditions.
- No caveats: Doesn't acknowledge limitations or edge case behavior (e.g., boolean handling, numeric string conversion).


### Rewritten explanation
- This function calculates the average of valid numeric measurements by filtering the input list to include only `int` and `float` types (excluding `bool`, which is a subclass of `int` in Python), then dividing the sum by the count of valid values. It ignores `None` values and any non-numeric types. If the input is empty, `None`, or contains no valid measurements, the function returns `0`. Note: This implementation requires measurements to be actual numeric types, not numeric strings — `"123"` will be ignored, not converted. This strict typing prevents silent data quality issues that could occur with permissive type coercion.


## 4) Final Judgment
- Decision: Request Changes
- Justification:The original implementation produces incorrect results for inputs containing None or non-numeric values and may raise runtime errors. The corrected function safely computes the average of valid numeric measurements only.
- Confidence & unknowns: High confidence in identified bugs and improved code. 

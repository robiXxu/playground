from fpdf import FPDF
import json

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'JavaScript Higher Order Function Exercises', 0, 1, 'C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Courier', '', 10) # Monospace for code
        self.multi_cell(0, 5, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# --- DATA GENERATION ---

data = {
    "Map": [
        {"title": "1. Basic Extraction (Beginner)", "desc": "Extract an array of just the product names.", "in": [{"id":1,"name":"Pen"},{"id":2,"name":"Pencil"}], "out": ["Pen","Pencil"]},
        {"title": "2. Simple Math (Beginner)", "desc": "Double every number in the array.", "in": [1, 2, 3, 4, 5], "out": [2, 4, 6, 8, 10]},
        {"title": "3. Fahrenheit to Celsius (Beginner)", "desc": "Convert temperatures: (F - 32) * 5/9.", "in": [32, 68, 100], "out": [0, 20, 37.7]},
        {"title": "4. HTML Wrapper (Intermediate)", "desc": "Wrap every string in an <h1> tag.", "in": ["Hello", "World"], "out": ["<h1>Hello</h1>", "<h1>World</h1>"]},
        {"title": "5. Object Reformatter (Intermediate)", "desc": "Rename keys: 'n' to 'name', 'a' to 'age'.", "in": [{"n":"Ali","a":20}], "out": [{"name":"Ali","age":20}]},
        {"title": "6. Boolean Flip (Intermediate)", "desc": "Invert the 'completed' status of tasks.", "in": [{"id":1,"completed":True},{"id":2,"completed":False}], "out": [{"id":1,"completed":False},{"id":2,"completed":True}]},
        {"title": "7. Extract Nested Data (Intermediate)", "desc": "Map to an array of just the city names from address objects.", "in": [{"user":"A","addr":{"city":"NY"}},{"user":"B","addr":{"city":"LA"}}], "out": ["NY","LA"]},
        {"title": "8. Conditional Logic (Expert)", "desc": "If age > 18, set isAdult: true, else false. Return objects.", "in": [{"age":10},{"age":25}], "out": [{"age":10,"isAdult":False},{"age":25,"isAdult":True}]},
        {"title": "9. Calculate Tax (Expert)", "desc": "Add a 'tax' property (10% of price) to each item.", "in": [{"price":100},{"price":50}], "out": [{"price":100,"tax":10},{"price":50,"tax":5}]},
        {"title": "10. Complex Transformation (Expert)", "desc": "Format full name and standardise dates (YYYY-MM-DD).", "in": [{"f":"John","l":"Doe","d":"10/02/2023"}], "out": [{"fullName":"John Doe","date":"2023-10-02"}]}
    ],
    "Filter": [
        {"title": "1. Evens Only (Beginner)", "desc": "Keep only even numbers.", "in": [1, 2, 3, 4, 5, 6], "out": [2, 4, 6]},
        {"title": "2. String Length (Beginner)", "desc": "Keep words longer than 3 characters.", "in": ["Hi", "Hello", "Yo", "World"], "out": ["Hello", "World"]},
        {"title": "3. Positive Numbers (Beginner)", "desc": "Remove negative numbers.", "in": [-10, 5, 0, -2, 8], "out": [5, 0, 8]},
        {"title": "4. Active Users (Intermediate)", "desc": "Filter users where isActive is true.", "in": [{"id":1,"isActive":True},{"id":2,"isActive":False}], "out": [{"id":1,"isActive":True}]},
        {"title": "5. Price Threshold (Intermediate)", "desc": "Keep items under $50.", "in": [{"p":100},{"p":20},{"p":49}], "out": [{"p":20},{"p":49}]},
        {"title": "6. Search Term (Intermediate)", "desc": "Keep strings that contain 'pro' (case insensitive).", "in": ["Profile", "Settings", "Product", "Home"], "out": ["Profile", "Product"]},
        {"title": "7. Null Remover (Intermediate)", "desc": "Remove null or undefined values from array.", "in": [1, None, 2, "undefined", 3], "out": [1, 2, 3]},
        {"title": "8. Array Intersection (Expert)", "desc": "Filter array A to only include items found in array B (Context: B=[1,3]).", "in": [1, 2, 3, 4], "out": [1, 3]},
        {"title": "9. Complex Nested Filter (Expert)", "desc": "Keep users who have 'admin' in their roles array.", "in": [{"u":"A","roles":["user"]},{"u":"B","roles":["user","admin"]}], "out": [{"u":"B","roles":["user","admin"]}]},
        {"title": "10. Date Range (Expert)", "desc": "Keep events occurring in 2024.", "in": [{"d":"2023-12-31"},{"d":"2024-01-01"},{"d":"2025-01-01"}], "out": [{"d":"2024-01-01"}]}
    ],
    "Find": [
        {"title": "1. Find Number (Beginner)", "desc": "Find the first number greater than 10.", "in": [5, 8, 12, 4, 20], "out": 12},
        {"title": "2. Specific String (Beginner)", "desc": "Find the string 'Waldo'.", "in": ["Tom", "Dick", "Waldo", "Harry"], "out": "Waldo"},
        {"title": "3. ID Search (Beginner)", "desc": "Find user with ID 3.", "in": [{"id":1},{"id":2},{"id":3}], "out": {"id":3}},
        {"title": "4. First Error (Intermediate)", "desc": "Find the first log with status 'ERROR'.", "in": [{"s":"OK"},{"s":"WARN"},{"s":"ERROR"},{"s":"ERROR"}], "out": {"s":"ERROR"}},
        {"title": "5. In Stock (Intermediate)", "desc": "Find the first product that is in stock.", "in": [{"n":"A","stock":0},{"n":"B","stock":5}], "out": [{"n":"B","stock":5}]},
        {"title": "6. Exact Match Object (Intermediate)", "desc": "Find item with x=10 and y=20.", "in": [{"x":10,"y":5},{"x":10,"y":20}], "out": {"x":10,"y":20}},
        {"title": "7. Undefined Checker (Intermediate)", "desc": "Find first element that is undefined.", "in": [1, 2, "undefined", 4], "out": "undefined"},
        {"title": "8. Nested ID (Expert)", "desc": "Find the group containing member ID 99.", "in": [{"g":1,"m":[10,20]},{"g":2,"m":[99,100]}], "out": {"g":2,"m":[99,100]}},
        {"title": "9. Calculation Search (Expert)", "desc": "Find the first rectangle with area > 100.", "in": [{"w":5,"h":5},{"w":10,"h":11},{"w":20,"h":20}], "out": {"w":10,"h":11}},
        {"title": "10. Regex Match (Expert)", "desc": "Find first email ending in .org.", "in": ["a@com", "b@org", "c@net"], "out": "b@org"}
    ],
    "Reduce": [
        {"title": "1. Sum (Beginner)", "desc": "Sum all numbers.", "in": [10, 20, 30], "out": 60},
        {"title": "2. Product (Beginner)", "desc": "Multiply all numbers.", "in": [2, 3, 4], "out": 24},
        {"title": "3. Concatenate (Beginner)", "desc": "Turn array of chars into string.", "in": ["h","e","l","l","o"], "out": "hello"},
        {"title": "4. Count Occurrences (Intermediate)", "desc": "Count how many times each fruit appears.", "in": ["apple", "banana", "apple"], "out": {"apple":2, "banana":1}},
        {"title": "5. Max Value (Intermediate)", "desc": "Find the maximum number.", "in": [10, 50, 30], "out": 50},
        {"title": "6. Flatten Array (Intermediate)", "desc": "Turn [[1,2], [3,4]] into [1,2,3,4].", "in": [[1,2], [3,4]], "out": [1,2,3,4]},
        {"title": "7. Array to Object (Intermediate)", "desc": "Map ID to Name: [{'id':1, 'n':'A'}] -> {1: 'A'}.", "in": [{"id":1,"n":"A"},{"id":2,"n":"B"}], "out": {"1":"A","2":"B"}},
        {"title": "8. Group By (Expert)", "desc": "Group people by age.", "in": [{"n":"A","age":20},{"n":"B","age":20},{"n":"C","age":21}], "out": {20:[{"n":"A","age":20},{"n":"B","age":20}], 21:[{"n":"C","age":21}]}},
        {"title": "9. Pipeline (Expert)", "desc": "Run a value through an array of functions (f(x) = x+1, x*2). Start: 5.", "in": ["plus1", "times2"], "out": 12},
        {"title": "10. Remove Duplicates (Expert)", "desc": "Reduce to unique values.", "in": [1, 2, 2, 3, 3, 3], "out": [1, 2, 3]}
    ],
    "Sort": [
        {"title": "1. Numeric Asc (Beginner)", "desc": "Sort numbers low to high.", "in": [10, 2, 5], "out": [2, 5, 10]},
        {"title": "2. Numeric Desc (Beginner)", "desc": "Sort numbers high to low.", "in": [10, 2, 5], "out": [10, 5, 2]},
        {"title": "3. Alphabetical (Beginner)", "desc": "Sort names A-Z.", "in": ["Zoe", "Ann", "Bob"], "out": ["Ann", "Bob", "Zoe"]},
        {"title": "4. String Length (Intermediate)", "desc": "Sort by word length (shortest first).", "in": ["Banana", "Apple", "Kiwi"], "out": ["Kiwi", "Apple", "Banana"]},
        {"title": "5. Object Property (Intermediate)", "desc": "Sort users by age (youngest first).", "in": [{"a":30},{"a":20},{"a":25}], "out": [{"a":20},{"a":25},{"a":30}]},
        {"title": "6. Boolean Sort (Intermediate)", "desc": "False first, True second.", "in": [True, False, True, False], "out": [False, False, True, True]},
        {"title": "7. Case Insensitive (Intermediate)", "desc": "Sort ignoring capitalization.", "in": ["apple", "Banana", "cherry"], "out": ["apple", "Banana", "cherry"]},
        {"title": "8. Date Sort (Expert)", "desc": "Sort by date string (oldest first).", "in": [{"d":"2023-01-01"},{"d":"2022-01-01"}], "out": [{"d":"2022-01-01"},{"d":"2023-01-01"}]},
        {"title": "9. Multiple Criteria (Expert)", "desc": "Sort by Score (High->Low), then Time (Low->High).", "in": [{"s":10,"t":5},{"s":10,"t":2},{"s":20,"t":10}], "out": [{"s":20,"t":10},{"s":10,"t":2},{"s":10,"t":5}]},
        {"title": "10. Custom Order (Expert)", "desc": "Sort by status priority: 'Active' > 'Pending' > 'Closed'.", "in": ["Closed", "Active", "Pending"], "out": ["Active", "Pending", "Closed"]}
    ]
}

# --- PDF GENERATION LOOP ---

for category, exercises in data.items():
    pdf.chapter_title(f"Array.prototype.{category.lower()}()")
    
    for ex in exercises:
        ex_text = f"{ex['title']}\n"
        ex_text += f"Goal: {ex['desc']}\n"
        ex_text += f"Input: {json.dumps(ex['in'])}\n"
        ex_text += f"Output: {json.dumps(ex['out'])}\n"
        ex_text += "-" * 60 + "\n"
        pdf.chapter_body(ex_text)
    
    pdf.add_page()

pdf.output("JS_HOF_Exercises.pdf")
print("PDF generated successfully: JS_HOF_Exercises.pdf")

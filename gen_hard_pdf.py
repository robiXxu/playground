from fpdf import FPDF
import json

# Initialize PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, '50 Deeply Nested JavaScript Exercises (Levels 2-6)', 0, 1, 'C')
        self.ln(5)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(220, 220, 220)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(2)

    def exercise_body(self, title, level, desc, input_data, output_data):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 6, f"{title} (Nesting Level: {level})", 0, 1)
        
        self.set_font('Arial', '', 9)
        self.multi_cell(0, 5, f"Goal: {desc}")
        self.ln(2)

        self.set_font('Courier', '', 8)
        self.set_text_color(0, 0, 0)
        
        # Format JSON
        try:
            inp_str = json.dumps(input_data, indent=2)
            out_str = json.dumps(output_data, indent=2)
        except:
            inp_str = str(input_data)
            out_str = str(output_data)

        # Print Input
        self.set_fill_color(245, 245, 245)
        self.multi_cell(0, 4, f"INPUT:\n{inp_str}", 0, 'L', True)
        self.ln(1)
        # Print Output
        self.set_fill_color(235, 255, 235)
        self.multi_cell(0, 4, f"OUTPUT:\n{out_str}", 0, 'L', True)
        self.ln(6)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(6)

pdf = PDF()
pdf.add_page()

# --- DATASET ---

data = {
    "Map": [
        {"t": "1. Extract Nested Email", "l": 2, "d": "Extract email from profile object.", "i": [{"id":1,"profile":{"email":"a@a.com"}},{"id":2,"profile":{"email":"b@b.com"}}], "o": ["a@a.com","b@b.com"]},
        {"t": "2. Format Address", "l": 3, "d": "Create string 'City, Country' from deep address.", "i": [{"user":{"details":{"addr":{"city":"NY","country":"USA"}}}},{"user":{"details":{"addr":{"city":"LDN","country":"UK"}}}}], "o": ["NY, USA","LDN, UK"]},
        {"t": "3. Normalize Product Tags", "l": 3, "d": "Extract tags array from meta object.", "i": [{"p":1,"meta":{"seo":{"tags":["new","sale"]}}},{"p":2,"meta":{"seo":{"tags":["old"]}}}], "o": [["new","sale"],["old"]]},
        {"t": "4. Matrix Flattening", "l": 3, "d": "Map a 2D grid to a list of coordinate strings 'x,y'.", "i": [[{"x":0,"y":0},{"x":1,"y":0}],[{"x":0,"y":1},{"x":1,"y":1}]], "o": [["0,0","1,0"],["0,1","1,1"]]},
        {"t": "5. Deep Value Scaling", "l": 4, "d": "Double the value inside data.payload.metrics.score.", "i": [{"data":{"payload":{"metrics":{"score":10}}}},{"data":{"payload":{"metrics":{"score":20}}}}], "o": [{"score":20},{"score":40}]},
        {"t": "6. Permission Extraction", "l": 4, "d": "Get list of permissions from user > role > config > perms.", "i": [{"u":"A","role":{"config":{"perms":["read","write"]}}}], "o": [["read","write"]]},
        {"t": "7. Tree Node Labeling", "l": 5, "d": "Extract label from node > child > child > label.", "i": [{"node":{"child":{"child":{"label":"Leaf A"}}}},{"node":{"child":{"child":{"label":"Leaf B"}}}}], "o": ["Leaf A","Leaf B"]},
        {"t": "8. Complex API Transform", "l": 5, "d": "Transform deeply nested error object into simple message string.", "i": [{"err":{"response":{"data":{"error":{"message":"Fail"}}}}},{"err":{"response":{"data":{"error":{"message":"Crash"}}}} }], "o": ["Fail","Crash"]},
        {"t": "9. The 6-Level Deep Extraction", "l": 6, "d": "Extract the 'secret' value found at level 6.", "i": [{"l1":{"l2":{"l3":{"l4":{"l5":{"l6":{"secret":"XYZ"}}}}}}}], "o": ["XYZ"]},
        {"t": "10. Recursive Structure Map", "l": 6, "d": "Flatten a comment thread (Root > Reply > Reply) into text only.", "i": [{"text":"A","r":[{"text":"B","r":[{"text":"C"}]}]}], "o": ["A","B","C"]}
    ],
    "Filter": [
        {"t": "1. Nested Status Check", "l": 2, "d": "Filter where meta.active is true.", "i": [{"meta":{"active":True}},{"meta":{"active":False}}], "o": [{"meta":{"active":True}}]},
        {"t": "2. Sub-array Length", "l": 3, "d": "Filter posts where comments array in 'eng' object is empty.", "i": [{"eng":{"comments":[]}},{"eng":{"comments":[1]}}], "o": [{"eng":{"comments":[]}}]},
        {"t": "3. Deep Property Existence", "l": 3, "d": "Filter items where details.specs.weight exists.", "i": [{"details":{"specs":{"color":"red"}}},{"details":{"specs":{"weight":10}}}], "o": [{"details":{"specs":{"weight":10}}}]},
        {"t": "4. Nested Array Match", "l": 4, "d": "Filter users who have 'admin' in role > config > types.", "i": [{"role":{"config":{"types":["user"]}}},{"role":{"config":{"types":["user","admin"]}}}], "o": [{"role":{"config":{"types":["user","admin"]}}}]},
        {"t": "5. Deep Math Condition", "l": 4, "d": "Filter orders where price > 100 in deep object.", "i": [{"ord":{"data":{"fin":{"price":50}}}},{"ord":{"data":{"fin":{"price":150}}}}], "o": [{"ord":{"data":{"fin":{"price":150}}}}]},
        {"t": "6. Anomaly Detection", "l": 5, "d": "Filter logs where trace > stack > 0 > file is 'error.js'.", "i": [{"trace":{"stack":[{"file":"app.js"}]}},{"trace":{"stack":[{"file":"error.js"}]}}], "o": [{"trace":{"stack":[{"file":"error.js"}]}}]},
        {"t": "7. Deep Null Check", "l": 5, "d": "Filter out objects where l1.l2.l3.l4.val is null.", "i": [{"l1":{"l2":{"l3":{"l4":{"val":1}}}}},{"l1":{"l2":{"l3":{"l4":{"val":None}}}}}], "o": [{"l1":{"l2":{"l3":{"l4":{"val":1}}}}}]},
        {"t": "8. The 6-Level Flag", "l": 6, "d": "Keep items where deep nested 'isCorrupt' flag is true.", "i": [{"a":{"b":{"c":{"d":{"e":{"f":{"isCorrupt":True}}}}}}},{"a":{"b":{"c":{"d":{"e":{"f":{"isCorrupt":False}}}}}}}], "o": [{"a":{"b":{"c":{"d":{"e":{"f":{"isCorrupt":True}}}}}}}]},
        {"t": "9. Dependency Tree", "l": 6, "d": "Filter modules that have 'vulnerable' flag in deep deps.", "i": [{"mod":"A","deps":{"d1":{"deps":{"d2":{"vulnerable":True}}}}}], "o": [{"mod":"A","deps":{"d1":{"deps":{"d2":{"vulnerable":True}}}}}]},
        {"t": "10. Complex Boolean", "l": 6, "d": "Filter if (deep.x > 10 AND deep.y < 5).", "i": [{"deep":{"l1":{"l2":{"l3":{"x":20,"y":2}}}}},{"deep":{"l1":{"l2":{"l3":{"x":20,"y":10}}}}}], "o": [{"deep":{"l1":{"l2":{"l3":{"x":20,"y":2}}}}}]}
    ],
    "Find": [
        {"t": "1. Find by ID", "l": 2, "d": "Find user where profile.id is 5.", "i": [{"profile":{"id":1}},{"profile":{"id":5}}], "o": {"profile":{"id":5}}},
        {"t": "2. Find in Sub-List", "l": 3, "d": "Find team where 'members' list contains 'John'.", "i": [{"members":["Alice"]},{"members":["John","Bob"]}], "o": {"members":["John","Bob"]}},
        {"t": "3. Deep Config Search", "l": 3, "d": "Find config where settings.display.theme is 'dark'.", "i": [{"settings":{"display":{"theme":"light"}}},{"settings":{"display":{"theme":"dark"}}}], "o": {"settings":{"display":{"theme":"dark"}}}},
        {"t": "4. First Failed Test", "l": 4, "d": "Find first test suite where results.summary.failed > 0.", "i": [{"results":{"summary":{"failed":0}}},{"results":{"summary":{"failed":2}}}], "o": {"results":{"summary":{"failed":2}}}},
        {"t": "5. Nested Comment ID", "l": 5, "d": "Find the comment object that contains reply ID 99.", "i": [{"id":1,"replies":[{"id":2}]},{"id":3,"replies":[{"id":99}]}], "o": {"id":3,"replies":[{"id":99}]}},
        {"t": "6. Deep Tree Search", "l": 5, "d": "Find the directory containing file 'secret.txt'.", "i": [{"dir":"A","files":["x.txt"]},{"dir":"B","files":["secret.txt"]}], "o": {"dir":"B","files":["secret.txt"]}},
        {"t": "7. The 6-Level Needle", "l": 6, "d": "Find object where l1.l2.l3.l4.l5.l6 is 'Found'.", "i": [{"l1":{"l2":{"l3":{"l4":{"l5":{"l6":"Found"}}}}}}], "o": {"l1":{"l2":{"l3":{"l4":{"l5":{"l6":"Found"}}}}}}},
        {"t": "8. Deep Version Match", "l": 6, "d": "Find package where deps.dev.core.version is '1.0.0'.", "i": [{"deps":{"dev":{"core":{"version":"0.9"}}}},{"deps":{"dev":{"core":{"version":"1.0.0"}}}}], "o": {"deps":{"dev":{"core":{"version":"1.0.0"}}}}},
        {"t": "9. Error Trace Finder", "l": 6, "d": "Find log entry where error.trace.origin.line is 404.", "i": [{"error":{"trace":{"origin":{"line":200}}}},{"error":{"trace":{"origin":{"line":404}}}}], "o": {"error":{"trace":{"origin":{"line":404}}}}},
        {"t": "10. Rare Attribute", "l": 6, "d": "Find user with 'super_admin' inside deeply nested attrs array.", "i": [{"attrs":{"l1":{"l2":{"tags":["user"]}}}},{"attrs":{"l1":{"l2":{"tags":["super_admin"]}}}}], "o": {"attrs":{"l1":{"l2":{"tags":["super_admin"]}}}}}
    ],
    "Reduce": [
        {"t": "1. Sum Nested Prices", "l": 2, "d": "Sum price from item.cost.", "i": [{"item":{"cost":10}},{"item":{"cost":20}}], "o": 30},
        {"t": "2. Flatten Categories", "l": 3, "d": "Reduce list of category objects (each has 'items' array) to single items array.", "i": [{"items":[1,2]},{"items":[3,4]}], "o": [1,2,3,4]},
        {"t": "3. Count Deep Status", "l": 3, "d": "Count occurrences of status in meta.status.", "i": [{"meta":{"status":"ok"}},{"meta":{"status":"fail"}},{"meta":{"status":"ok"}}], "o": {"ok":2,"fail":1}},
        {"t": "4. Merge Configs", "l": 4, "d": "Merge nested 'conf' objects into one.", "i": [{"conf":{"a":1}},{"conf":{"b":2}}], "o": {"a":1,"b":2}},
        {"t": "5. Max Nested Score", "l": 4, "d": "Find max value in data.results.score.", "i": [{"data":{"results":{"score":10}}},{"data":{"results":{"score":50}}}], "o": 50},
        {"t": "6. Deep Inventory Count", "l": 5, "d": "Sum stock from store > aisle > shelf > stock.", "i": [{"store":{"aisle":{"shelf":{"stock":5}}}},{"store":{"aisle":{"shelf":{"stock":10}}}}], "o": 15},
        {"t": "7. Path Builder", "l": 5, "d": "Construct path string from nodes.", "i": [{"node":{"val":"home"}},{"node":{"val":"user"}},{"node":{"val":"docs"}}], "o": "/home/user/docs"},
        {"t": "8. The 6-Level Aggregator", "l": 6, "d": "Sum values found at level 6.", "i": [{"a":{"b":{"c":{"d":{"e":{"f":1}}}}}},{"a":{"b":{"c":{"d":{"e":{"f":2}}}}}}], "o": 3},
        {"t": "9. Deep Array Union", "l": 6, "d": "Combine arrays found at deep level into one unique set.", "i": [{"d":{"d":{"d":{"d":{"d":{"arr":[1,2]}}}}}},{"d":{"d":{"d":{"d":{"d":{"arr":[2,3]}}}}}}], "o": [1,2,3]},
        {"t": "10. Recursive Size Calc", "l": 6, "d": "Calculate total size of file tree structure.", "i": [{"size":10,"files":[{"size":20,"files":[]},{"size":5,"files":[{"size":5}]}]}], "o": 40}
    ],
    "Sort": [
        {"t": "1. Nested Age Sort", "l": 2, "d": "Sort by info.age.", "i": [{"info":{"age":30}},{"info":{"age":20}}], "o": [{"info":{"age":20}},{"info":{"age":30}}]},
        {"t": "2. Deep Date Sort", "l": 3, "d": "Sort by meta.created.at date string.", "i": [{"meta":{"created":{"at":"2023"}}},{"meta":{"created":{"at":"2022"}}}], "o": [{"meta":{"created":{"at":"2022"}}},{"meta":{"created":{"at":"2023"}}}]},
        {"t": "3. Sub-array Length", "l": 3, "d": "Sort by number of tags in details.tags.", "i": [{"details":{"tags":[1]}},{"details":{"tags":[1,2,3]}}], "o": [{"details":{"tags":[1,2,3]}},{"details":{"tags":[1]}}]}, 
        {"t": "4. Nested Name Match", "l": 4, "d": "Sort alphabetically by profile.personal.name.", "i": [{"profile":{"personal":{"name":"B"}}},{"profile":{"personal":{"name":"A"}}}], "o": [{"profile":{"personal":{"name":"A"}}},{"profile":{"personal":{"name":"B"}}}]},
        {"t": "5. Calculated Metric", "l": 4, "d": "Sort by (stats.wins - stats.losses).", "i": [{"stats":{"wins":10,"losses":5}},{"stats":{"wins":20,"losses":2}}], "o": [{"stats":{"wins":20,"losses":2}},{"stats":{"wins":10,"losses":5}}]}, 
        {"t": "6. Deep Priority String", "l": 5, "d": "Sort by task.meta.priority (High > Low).", "i": [{"task":{"meta":{"priority":"Low"}}},{"task":{"meta":{"priority":"High"}}}], "o": [{"task":{"meta":{"priority":"High"}}},{"task":{"meta":{"priority":"Low"}}}]},
        {"t": "7. The 6-Level Value", "l": 6, "d": "Sort by value at l1.l2.l3.l4.l5.l6.", "i": [{"l1":{"l2":{"l3":{"l4":{"l5":{"l6":10}}}}}},{"l1":{"l2":{"l3":{"l4":{"l5":{"l6":1}}}}}}], "o": [{"l1":{"l2":{"l3":{"l4":{"l5":{"l6":1}}}}}},{"l1":{"l2":{"l3":{"l4":{"l5":{"l6":10}}}}}}]},
        {"t": "8. Deep Boolean", "l": 6, "d": "Sort: items with deep 'verified':true come first.", "i": [{"d":{"d":{"d":{"d":{"d":{"verified":False}}}}}},{"d":{"d":{"d":{"d":{"d":{"verified":True}}}}}}], "o": [{"d":{"d":{"d":{"d":{"d":{"verified":True}}}}}},{"d":{"d":{"d":{"d":{"d":{"verified":False}}}}}}]},
        {"t": "9. Version Depth", "l": 6, "d": "Sort by deep version string 'v1.0' vs 'v2.0'.", "i": [{"v":{"v":{"v":{"v":{"v":{"ver":"v2.0"}}}}}},{"v":{"v":{"v":{"v":{"v":{"ver":"v1.0"}}}}}}], "o": [{"v":{"v":{"v":{"v":{"v":{"ver":"v1.0"}}}}}},{"v":{"v":{"v":{"v":{"v":{"ver":"v2.0"}}}}}}]},
        {"t": "10. Multiple Deep Criteria", "l": 6, "d": "Sort by deep Category, then deep Price.", "i": [{"d":{"cat":"A","p":100}},{"d":{"cat":"A","p":10}},{"d":{"cat":"B","p":50}}], "o": [{"d":{"cat":"A","p":10}},{"d":{"cat":"A","p":100}},{"d":{"cat":"B","p":50}}]}
    ]
}

# --- GENERATION LOOP ---

for category, exercises in data.items():
    pdf.chapter_title(f"Array.prototype.{category.lower()}()")
    
    for ex in exercises:
        pdf.exercise_body(ex['t'], ex['l'], ex['d'], ex['i'], ex['o'])
        
    pdf.add_page()

pdf.output("Nested_HOF_Exercises.pdf")
print("PDF generated successfully: Nested_HOF_Exercises.pdf")

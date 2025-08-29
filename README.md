# DSA For Interview 🚀

A comprehensive collection of Data Structures and Algorithms (DSA) problems and solutions implemented in Python, designed to help you prepare for technical interviews at top tech companies.

## 📚 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Problems Included](#problems-included)
  - [Array Problems](#array-problems)
  - [Stack Problems](#stack-problems)
- [How to Use](#how-to-use)
- [Running the Code](#running-the-code)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository contains well-documented solutions to popular DSA problems frequently asked in technical interviews. Each solution is implemented with clear logic, optimal time and space complexity considerations, and includes test cases to verify correctness.

**Key Features:**
- ✅ Clean, readable Python implementations
- ✅ Optimized solutions with complexity analysis
- ✅ Test cases included with example outputs
- ✅ Organized by data structure type
- ✅ Interview-focused problem selection

## 📁 Repository Structure

```
DSA_For_Interview/
├── array/
│   ├── static/          # Static array problems
│   └── dynamic/         # Dynamic array problems
├── stack/               # Stack-based problems
└── README.md           # This file
```

## 💡 Problems Included

### Array Problems

#### Static Arrays (`array/static/`)

1. **Shuffle Array** (`shuffleArray.py`)
   - **Problem**: Given an array consisting of 2n elements in the form [x₁,x₂,...,xₙ,y₁,y₂,...,yₙ], shuffle it to [x₁,y₁,x₂,y₂,...,xₙ,yₙ]
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)
   - **Example**: `[2,5,1,3,4,7]` → `[2,3,5,4,1,7]`

2. **Remove Duplicates from Sorted Array** (`def remove_duplicate_sorted_array(array).py`)
   - **Problem**: Remove duplicates from a sorted array in-place
   - **Time Complexity**: O(n²)
   - **Space Complexity**: O(1)
   - **Example**: `[0,1,1,1,2,2]` → `[0,1,2,_,_,_]`

3. **Remove Element** (`def remove_element(array,value):.py.py`)
   - **Problem**: Remove all instances of a specific value from array in-place
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(1)
   - **Example**: Remove value `2` from `[0,1,2,2,3,0,4,2]`

#### Dynamic Arrays (`array/dynamic/`)

1. **Concatenation of Array** (`Concatenation of Array.py`)
   - **Problem**: Given an array nums, create array ans = [nums, nums] (concatenate with itself)
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)
   - **Example**: `[1,2,3]` → `[1,2,3,1,2,3]`

### Stack Problems (`stack/`)

1. **Valid Parentheses** (`valid_parenthesis.py`)
   - **Problem**: Determine if string of brackets is valid (properly opened and closed)
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)
   - **Example**: `"()"` → `True`, `"([)]"` → `False`

2. **Min Stack** (`minStack.py`)
   - **Problem**: Design a stack that supports push, pop, top, and retrieving minimum element in constant time
   - **Time Complexity**: O(1) for all operations
   - **Space Complexity**: O(n)
   - **Features**: Push, pop, top, getMin operations

3. **Baseball Game** (`BaseBal.py`)
   - **Problem**: Calculate final score based on baseball game operations
   - **Operations**: 
     - Integer: Record new score
     - `"+"`: Sum of last two scores
     - `"D"`: Double the last score
     - `"C"`: Cancel the last score
   - **Time Complexity**: O(n)
   - **Space Complexity**: O(n)

## 🚀 How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/TanzimHossainSafin/DSA_For_Interview.git
   cd DSA_For_Interview
   ```

2. **Navigate to specific problem:**
   ```bash
   cd array/static/
   # or
   cd stack/
   ```

3. **Study the problem and solution:**
   - Read the code comments and understand the approach
   - Analyze time and space complexity
   - Review the test cases

## 🏃‍♂️ Running the Code

All Python files can be run directly and include test cases:

```bash
# Example: Run the shuffle array problem
python array/static/shuffleArray.py

# Example: Run the valid parentheses checker
python stack/valid_parenthesis.py

# Example: Run the min stack implementation
python stack/minStack.py
```

**Prerequisites:**
- Python 3.x installed on your system
- No external dependencies required

## 🧪 Testing

Each file includes test cases at the bottom. Simply run the Python file to see the output:

```python
# Example output from shuffleArray.py
[2, 3, 5, 4, 1, 7]

# Example output from valid_parenthesis.py
True
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Add new problems:**
   - Choose problems commonly asked in interviews
   - Implement clean, optimal solutions
   - Include time/space complexity analysis
   - Add test cases with examples

2. **Improve existing solutions:**
   - Optimize time/space complexity
   - Add better comments and documentation
   - Fix bugs or edge cases

3. **Organize code:**
   - Follow the existing directory structure
   - Use descriptive file names
   - Include problem descriptions

**Steps to contribute:**
1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-problem`)
3. Commit your changes (`git commit -am 'Add new problem: XYZ'`)
4. Push to the branch (`git push origin feature/new-problem`)
5. Create a Pull Request

## 📋 Problem Categories Roadmap

**Planned additions:**
- [ ] Linked Lists
- [ ] Trees and Binary Search Trees
- [ ] Graphs and Graph Algorithms
- [ ] Dynamic Programming
- [ ] Sorting and Searching
- [ ] Hash Tables
- [ ] Heap/Priority Queue
- [ ] Two Pointers
- [ ] Sliding Window

## 💡 Tips for Interview Success

1. **Understand the problem** before coding
2. **Think about edge cases** and constraints
3. **Start with brute force**, then optimize
4. **Communicate your thought process** clearly
5. **Test your solution** with examples
6. **Analyze time and space complexity**

## 📖 Resources

- [LeetCode](https://leetcode.com/) - Practice problems
- [GeeksforGeeks](https://www.geeksforgeeks.org/) - Algorithms and data structures
- [Cracking the Coding Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850) - Book by Gayle McDowell

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Coding! 🎉**

Feel free to star ⭐ this repository if you find it helpful for your interview preparation!
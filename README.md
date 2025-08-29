# DSA For Interview 🚀

A comprehensive collection of Data Structures and Algorithms implementations in Python, specifically designed for technical interview preparation. This repository contains solutions to common coding problems organized by data structure categories.

## 📁 Repository Structure

```
DSA_For_Interview/
├── stack/              # Stack-based algorithms and problems
│   ├── minStack.py
│   ├── valid_parenthesis.py
│   └── BaseBal.py
└── array/              # Array-based algorithms and problems
    ├── static/         # Static array problems
    │   ├── shuffleArray.py
    │   ├── def remove_element(array,value):.py.py
    │   └── def remove_duplicate_sorted_array(array).py
    └── dynamic/        # Dynamic array problems
        └── Concatenation of Array.py
```

## 🔧 Stack Problems

### 1. MinStack (`minStack.py`)
**Problem**: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

**Features**:
- `push(val)`: Push element to stack
- `pop()`: Remove top element
- `top()`: Get top element
- `getMin()`: Get minimum element in O(1) time

**Example**:
```python
obj = MinStack()
obj.push(-2)
obj.push(-4)
obj.push(-3)
print(obj.top())     # Output: -3
print(obj.getMin())  # Output: -4
```

### 2. Valid Parentheses (`valid_parenthesis.py`)
**Problem**: Check if a string containing parentheses `()`, brackets `[]`, and braces `{}` is valid.

**Algorithm**: Uses stack to match opening and closing brackets.

**Example**:
```python
print(valid_parenthesis('()'))     # Output: True
print(valid_parenthesis('([)]'))   # Output: False
```

### 3. Baseball Game (`BaseBal.py`)
**Problem**: Calculate baseball game score based on operations.

**Operations**:
- Integer: Record a new score
- `+`: Sum of last two scores
- `D`: Double the last score  
- `C`: Cancel the last score

**Example**:
```python
print(BaseBall(["5","-2","4","C","D","9","+","+"]))  # Output: 27
```

## 📊 Array Problems

### Static Arrays

#### 1. Shuffle Array (`shuffleArray.py`)
**Problem**: Shuffle array `[x1,x2,...,xn,y1,y2,...,yn]` to `[x1,y1,x2,y2,...,xn,yn]`.

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

**Example**:
```python
print(shuffle([2,5,1,3,4,7], 3))  # Output: [2,3,5,4,1,7]
```

#### 2. Remove Element (`def remove_element(array,value):.py.py`)
**Problem**: Remove all instances of a specific value from array in-place.

**Algorithm**: Two-pointer technique with placeholder replacement.

**Example**:
```python
print(remove_element([0,1,2,2,3,0,4,2], 2))  # Output: ([0,1,3,0,4,'_','_','_'], 5)
```

#### 3. Remove Duplicates from Sorted Array (`def remove_duplicate_sorted_array(array).py`)
**Problem**: Remove duplicates from sorted array in-place.

**Time Complexity**: O(n²)  
**Space Complexity**: O(1)

**Example**:
```python
a, b = remove_duplicate_sorted_array([0,1,1,1,2,2])
print(a)  # Output: 3 (unique elements count)
print(b)  # Output: [0,1,2,'_','_','_']
```

### Dynamic Arrays

#### 1. Array Concatenation (`Concatenation of Array.py`)
**Problem**: Concatenate array with itself.

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

**Example**:
```python
print(Concatenation_of_Array([1,2,3]))  # Output: [1,2,3,1,2,3]
```

## 🚀 How to Run

1. **Clone the repository**:
```bash
git clone https://github.com/TanzimHossainSafin/DSA_For_Interview.git
cd DSA_For_Interview
```

2. **Run individual files**:
```bash
# Stack problems
python3 stack/minStack.py
python3 stack/valid_parenthesis.py
python3 stack/BaseBal.py

# Array problems
python3 array/static/shuffleArray.py
python3 array/dynamic/"Concatenation of Array.py"
```

3. **Import and use in your code**:
```python
# Example: Using MinStack
from stack.minStack import MinStack

stack = MinStack()
stack.push(5)
stack.push(2)
print(stack.getMin())  # Output: 2
```

## 📚 Problem Categories

| Category | Problems | Difficulty |
|----------|----------|------------|
| **Stack** | MinStack, Valid Parentheses, Baseball Game | Easy-Medium |
| **Array (Static)** | Shuffle, Remove Element, Remove Duplicates | Easy-Medium |
| **Array (Dynamic)** | Array Concatenation | Easy |

## 🎯 Interview Tips

1. **Time Complexity**: Each solution includes time complexity analysis
2. **Space Complexity**: Consider space trade-offs for optimal solutions
3. **Edge Cases**: Solutions handle empty inputs and boundary conditions
4. **Code Style**: Clean, readable Python code following best practices

## 🤝 Contributing

This repository is designed for interview preparation. Feel free to:
- Add new problem solutions
- Optimize existing algorithms
- Add test cases
- Improve documentation

## 📝 Notes

- All implementations are in Python 3
- Solutions focus on clarity and interview-friendliness
- Time and space complexities are noted where applicable
- Each file contains working examples with expected outputs

---

**Happy Coding! 🎉**  
*Good luck with your technical interviews!*
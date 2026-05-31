# My Python Learning Journey

## Goal
Become an SDET in 18-24 months

## Background
- Currently a Manual QA
- Learning Python and Java in parallel
- Starting from scratch in programming

## Day 1 — 29 April 2026
- Installed Python 3.12 via Homebrew
- Set up Git and GitHub account (drodionichev)
- Created first repository: python-learning-journey
- First steps with terminal, nano/pico editor, git config
- Tomorrow: Python data types and mutable default arguments trap

## Day 1 Reflection
- Made first git push by myself, without instructions
- Started feeling less afraid of terminal
- Lesson: I remember more than I think

## Day 2 30 April 2026
- Learned basic data types
- Understood the difference between mutable and immutable
- Practiced using the .append method
- Completed a logic challenge on mutability

## Day 3 — 1 May 2026 — Strings Deep

**What I learned:**
- String slicing: s[start:end], s[::-1] (reverse), s[::2]
- String methods: .upper(), .lower(), .strip(), .replace(), .split(), .join(), .count(), .startswith(), .endswith(), .isalnum()
- Strings are immutable — methods return new string
- F-strings: variable substitution, expressions, formatting (:.2f, :.0%)
- *args — variable number of positional arguments
- isinstance(), all(), tuple unpacking
- Early return pattern, DRY principle

**Practice tasks:**
- is_image(filename) — file extension validator
- is_valid_email(email) — email validator
- parse_user(csv_line) — CSV parser to dict
- build_url(domain, *paths) — URL builder

**Files created:** day_3_f-strocks.py, day_3_practice.py
**Commits:** 3+

## Day 4 — 2 May 2026 — Lists, Loops, Comprehensions

**What I learned:**
- List methods: .append(), .insert(), .remove(), .pop(), .sort(), sorted()
- For loops, range(), enumerate()
- Loop patterns: accumulator, filter, transform
- While loops, break, continue
- List comprehensions
- Built-ins: max(), min(), sum(), round()
- Dict basics: .get(key, default), counter pattern

**Practice tasks:**
- analyze_words(words) — word statistics
- count_letters(text) — letter frequency counter

**Files created:** day_4_lists_loops.py, day_4_practice.py
**Commits:** 2+

## Day 6 — 31 May 2026 — Dictionaries Deep

**What I learned:**
- Dict iteration: .items(), .keys(), .values()
- .update() — add/update multiple keys at once
- .pop(key) — remove and return value
- Nested dicts — accessing data with double []
- Nested loops — outer loop over users, inner over skills
- .join() inside f-strings
- Counter pattern applied to nested data structures

**Practice tasks:**
- get_skill_summary(users) — nested dict + join
- count_skills(users) — nested loop + counter pattern
- merge_users(users1, users2) — merging dicts with .update()

**Files created:** day_6_dicts.py
**Commits:** 1
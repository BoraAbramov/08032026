
'''
The Challenge: "The Social Bridge"
Write a function called get_shared_interests that takes two lists of strings as input (e.g., interests of Person A and Person B).
The function should:

**bonus: Identify only the interests that both people share, using a set for an efficient comparison, or set functions

Return a tuple containing:
The sorted list of shared interests
The integer count of how many interests they have in common
Input:
  person_a = ["coding", "hiking", "cooking", "surfing"]
  person_b = ["hiking", "gaming", "coding"]
Output:
  (['coding', 'hiking'], 2)

def find_common(person_a, person_b) -> tuple(list, int):
    pass

'''

person_a = ["coding", "hiking", "cooking", "surfing"]
person_b = ["hiking", "gaming", "coding"]

def common_count(person_a, person_b) -> tuple:
    person_a = set(person_a)
    person_b = set(person_b)

    _common = person_a & person_b
    _count = len(_common)
    return list(_common), _count

print(common_count(person_a, person_b))
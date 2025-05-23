import os

parent_path = os.path.join(os.getcwd(), "..", "..")
print(parent_path)
parent_path = os.path.abspath(parent_path)
print(parent_path)

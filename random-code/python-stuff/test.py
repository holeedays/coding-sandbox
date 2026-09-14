test_string: str = "Hello World"
print(test_string)

# Create a list containing three course tools.
# Print the second item.
# Add a fourth item.
# Create a dictionary describing one class meeting with keys for class_number, topic, and completed.
# Print only the topic.

course_tools: list[str] = ["slack", "canvas", "google colab"]
print(f"The second term is {course_tools[1]}")
course_tools.append("github")
this_my_dictionary: dict[str, str | int | bool] = {
    "class_number": 612,
    "topic": "data science",
    "completed": False
}
print(f"The topic of our class is {this_my_dictionary['topic']}")

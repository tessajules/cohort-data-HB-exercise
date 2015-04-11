def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army"
            ])

    """

    houses = set()

    # Code goes here
    cohort_info = open(filename)

    for line in cohort_info:
        person_info = line.rstrip().split("|")
        house = person_info[2]
        if len(house) > 0:
            houses.add(house)

    return houses

#print unique_houses("cohort_data.txt")


def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]5 80q
        ex. all_students = [winter_15, spring_15, tas]

    """

    all_students = []
    winter_15 = []
    spring_15 = []
    tas = []

    # Code goes here
    cohort_info = open(filename)
    for person_info in cohort_info:
        person_info = person_info.rstrip().split("|")
        cohort = person_info[4]
        first_and_last_name = person_info[0] + " " + person_info[1]
        if cohort == "Winter 2015":
            winter_15.append([first_and_last_name])
        elif cohort == "Spring 2015":
            spring_15.append(first_and_last_name)
        elif len(cohort) > 0:
            tas.append(first_and_last_name)
        else:
            print first_and_last_name, "is an instructor"

    winter_15.sort()
    spring_15.sort()
    tas.sort()

    all_students.extend([winter_15, spring_15, tas])

    return all_students

#print sort_by_cohort("cohort_data.txt")

def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Wiedl", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. houses_tas = [ hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        tas
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    ravenclaw = []
    tas = []

    # Code goes here
    cohort_info = open(filename)
    for person_info in cohort_info:
            person_info = person_info.rstrip().split("|")
            last_name = person_info[1]
            house = person_info[2]
            cohort = person_info[4]
            if cohort == "Spring 2015" or cohort == "Winter 2015":
                if house == "Gryffindor":
                    gryffindor.append(last_name)
                elif house == "Hufflepuff":
                    hufflepuff.append(last_name)
                elif house == "Slytherin":
                    slytherin.append(last_name)
                elif house == "Dumbledore's Army":
                    dumbledores_army.append(last_name)
                elif house == "Ravenclaw":
                    ravenclaw.append(last_name)
            elif len(cohort) > 0:
                tas.append(last_name)
            else:
                print last_name, "is an instructor"

    all_students.extend([gryffindor, hufflepuff, slytherin, dumbledores_army, ravenclaw, tas])

    return all_students

#print students_by_house("cohort_data.txt")

def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """

    student_list = []

    # Code goes here

    cohort_info = open(filename)
    for person_info in cohort_info:
        person_info_list = person_info.rstrip().split("|")

        cohort = person_info_list[4]
        if cohort == "Winter 2015" or cohort == "Spring 2015":
            full_name = person_info_list[0] + " " + person_info_list[1]
            house = person_info_list[2]
            advisor = person_info_list[3]

            person_info_tuple = (full_name, house, advisor, cohort)
            student_list.append(person_info_tuple)

    return student_list


def find_cohort_by_student_name(student_list, student_name):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    # Code goes here

    for person_info_tuple in student_list:
        if student_name == person_info_tuple[0]:
            return person_info_tuple[3]

    else:

        return "Student not found."

student_list = all_students_tuple_list("cohort_data.txt")
#print find_cohort_by_student_name(student_list, "Angela Castanieto")
#print find_cohort_by_student_name(student_list, "slkdjfld klfjlds")
##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Sarah", "Nicole"])

    """
    winter_names = set()
    spring_names = set()
    cohort_info = open(filename)

    for person_info in cohort_info:
        person_info = person_info.rstrip().split("|")

        if person_info[4] == "Winter 2015":
            winter_names.add(person_info[0])
        elif person_info[4] == "Spring 2015":
            spring_names.add(person_info[0])

    duplicate_names = winter_names & spring_names

    return duplicate_names

#print find_name_duplicates("cohort_data.txt")

def find_house_members_by_student_name(student_list, student_full_name):
    """TODO: Create a function that, when given a name, returns everyone in
    their house that's in their cohort.  Use the list of tuples generated by
    all_students_tuple_list to make a small function that,
    when given a student's first and last name, returns students that are in
    both that student's cohort and that student's house.
    ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015")"""

    students_in_cohort_and_house = []

    for student_info_tuple in student_list:
        if student_full_name == student_info_tuple[0]:
            student_cohort = student_info_tuple[3]
            student_house = student_info_tuple[1]
            break

    for student_info_tuple in student_list:
        if student_full_name != student_info_tuple[0]:
            if student_cohort == student_info_tuple[3] and student_house == student_info_tuple[1]:
                students_in_cohort_and_house.append(student_info_tuple[0])

    return students_in_cohort_and_house

student_list = all_students_tuple_list("cohort_data.txt")
print find_house_members_by_student_name(student_list, "Angela Castanieto")

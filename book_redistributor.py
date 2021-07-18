import json
import csv


def parse_books():  # Collecting all books dictionaries into list
    with open('books.csv') as book:
        csvfile = csv.DictReader(book)
        booklist = [book_dict for book_dict in csvfile]
        return booklist


def parse_users():  # Collecting all necessary user data into dictionaries, putting all dictionaries into list
    with open('users.json') as jsonfile:
        data = json.load(jsonfile)

    resultinglist = [{"name": user_object["name"],
                      "gender": user_object["gender"],
                      "address": user_object["address"],
                      "age": user_object["age"],
                      "books": []}
                     for user_object in data]

    return resultinglist


def redistribute_books(users, books):  # evenly redistributing all books to users
    user_id = 0
    while len(books) > 0:
        users[user_id]["books"].append(books.pop())
        if user_id != len(users) - 1:
            user_id += 1
        else:
            user_id = 0
    return users


def make_output_json(userswithbooks):  # creating output .json file
    with open('outputfile.json', "w") as writer:
        json.dump(userswithbooks, writer)


make_output_json(redistribute_books(parse_users(), parse_books()))  # calling all functions to create output file

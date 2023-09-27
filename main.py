# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



students = [
        {"id":1, "name":'Noha', "image":"pic1.jpg", 'grade':10 },
        {"id":2, "name":'Noha', "image":"pic2.png", "grade":20 },
        {"id": 3, "name": 'Salma', "image": "pic3.png","grade":30},
        {"id": 4, "name": 'Norhan', "image": "pic4.png","grade":40}
    ]


stds = filter(lambda std:std["id"]==1, students)

print(list(stds))
# def findstudent(id):
#     for std in students:
#         if std['id']==id:
#             return  std
#
#
#
# # lambd --> function without name
#
# nums=[4,5,6,5]
# numm= filter(lambda num: num%2==0, nums)
# print(list(numm))
#
